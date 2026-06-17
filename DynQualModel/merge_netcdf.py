#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

#
# PCR-GLOBWB (PCRaster Global Water Balance) Global Hydrological Model
# (adapted from original by Edwin H. Sutanudjaja et al.)
#
# Merges per-clone NetCDF files into a single global file.
# Outputs exact LDD 5-arcmin grid (4320 x 2160) with zlib compression.

import os, sys, datetime, calendar
import time as tm
import numpy as np
import netCDF4 as nc
from multiprocessing import Pool
from dateutil.relativedelta import relativedelta


# ---------------------------------------------------------------------------
# Known LDD grid definitions keyed by approximate resolution in degrees.
# These hardcoded values avoid the np.arange floating-point artefact that
# produces an extra row/column at the boundary for 5-arcmin files.
# 30-arcmin files are unaffected (0.5° step is exact in floating point) but
# are included here for completeness.
# ---------------------------------------------------------------------------
LDD_GRIDS = {
    # 5-arcmin  (1/12 degree)
    round(5.0 / 60.0, 6): dict(
        xsize=4320, ysize=2160,
        xfirst=-179.9583, yfirst=89.95834,
        xinc=0.08333333,  yinc=-0.08333334,
    ),
    # 30-arcmin  (0.5 degree)
    0.5: dict(
        xsize=720,  ysize=360,
        xfirst=-179.75, yfirst=89.75,
        xinc=0.5,       yinc=-0.5,
    ),
}


def make_ldd_grid(deltaLon, deltaLat):
    """
    Return (lons, lats) arrays for the nearest known LDD grid,
    or fall back to np.arange if the resolution is not recognised.
    """
    key = round(float(deltaLon), 6)
    if key in LDD_GRIDS:
        g = LDD_GRIDS[key]
        lons = np.array([g['xfirst'] + i * g['xinc'] for i in range(g['xsize'])], dtype='f4')
        lats = np.array([g['yfirst'] + i * g['yinc'] for i in range(g['ysize'])], dtype='f4')
        print('  Using hardcoded LDD grid for %.6f° resolution: %d x %d' % (key, g['xsize'], g['ysize']))
    else:
        # Unknown resolution — fall back to arange (may have off-by-one for
        # some step sizes; fixable later with fix_grid.sh if needed)
        print('  WARNING: unknown resolution %.6f° — using np.arange (may produce extra boundary cell)' % key)
        latMin = -90  + deltaLat / 2.0
        latMax =  90  - deltaLat / 2.0
        lonMin = -180 + deltaLon / 2.0
        lonMax =  180 - deltaLon / 2.0
        lons = np.around(np.arange(lonMin, lonMax + deltaLon, deltaLon), decimals=6).astype('f4')
        lats = np.around(np.arange(latMax, latMin - deltaLat, -deltaLat), decimals=6).astype('f4')
    return lons, lats


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def calculate_monthdelta(date1, date2):
    def is_last_day_of_the_month(date):
        days_in_month = calendar.monthrange(date.year, date.month)[1]
        return date.day == days_in_month
    imaginary_day_2 = 31 if is_last_day_of_the_month(date2) else date2.day
    return (
        (date2.month - date1.month)
        + (date2.year - date1.year) * 12
        + (-1 if date1.day > imaginary_day_2 else 0)
    )


def ncFileNameDict(inputDirRoot, areas, ncFileName, fileType):
    folder = 'states' if fileType == 'outStates' else 'netcdf'
    return {i: os.path.join(inputDirRoot, area, folder, ncFileName)
            for i, area in enumerate(areas, start=1)}


# ---------------------------------------------------------------------------
# Core merge function
# ---------------------------------------------------------------------------

def mergeNetCDF(inputTuple):

    ncName      = inputTuple[0]
    startDate   = inputTuple[1]
    endDate     = inputTuple[2]
    ncFormat    = inputTuple[3]
    using_zlib  = inputTuple[4]
    using_MV    = inputTuple[5]
    fileType    = inputTuple[6]

    if using_zlib == "True":  using_zlib = True
    if using_zlib == "False": using_zlib = False
    if using_MV   == "True":  using_MV   = True
    if using_MV   == "False": using_MV   = False

    scriptStartTime = tm.time()
    print('\n=== combining files for %s ===' % ncName)

    netCDFInput  = ncFileNameDict(inputDirRoot, areas, ncName, fileType)
    netCDFOutput = os.path.join(
        outputDir,
        "%s_%s_to_%s.nc" % (ncName.split(".")[0], startDate, endDate)
    )
    print('Output: %s' % netCDFOutput)

    # ── Pass 1: collect metadata ──────────────────────────────────────────
    attributes   = {}
    dimensions   = {}
    var_meta     = {}
    variableName = None
    calendar_used = {}
    MV           = None
    varUnits     = None

    for index, ncFile in netCDFInput.items():
        if not os.path.isfile(ncFile):
            print("  WARNING: file not found, skipping: %s" % ncFile)
            continue

        rootgrp = nc.Dataset(ncFile)
        dimensions[index] = rootgrp.dimensions.copy()
        var_meta[index]   = rootgrp.variables.copy()
        attributes[index] = rootgrp.__dict__.copy()

        if 'time' in var_meta[index]:
            for name in rootgrp.variables['time'].ncattrs():
                val = getattr(rootgrp.variables['time'], name)
                if name not in calendar_used:
                    calendar_used[name] = val
                elif val != calendar_used[name]:
                    rootgrp.close()
                    sys.exit('ERROR: incompatible time attribute "%s" in %s' % (name, ncFile))

        data_keys = [k for k in var_meta[index] if k not in dimensions[index]]
        if not data_keys:
            rootgrp.close()
            sys.exit('ERROR: no data variable found in %s' % ncFile)
        key = data_keys[0]
        if variableName is None:
            variableName = key
        elif key != variableName:
            rootgrp.close()
            sys.exit('ERROR: variable name mismatch ("%s" vs "%s")' % (variableName, key))

        MV       = -999.9000244140625 if using_MV is True else float(rootgrp.variables[key]._FillValue)
        varUnits = str(rootgrp.variables[variableName].units)
        rootgrp.close()

    if variableName is None:
        print('ERROR: no valid clone files found for %s, skipping.' % ncName)
        return

    # ── Build output time axis ────────────────────────────────────────────
    time_units    = calendar_used.get('units', 'days since 1901-01-01 00:00:00')
    time_calendar = calendar_used.get('calendar', 'standard')

    first_nc = next((p for p in netCDFInput.values() if os.path.isfile(p)), None)
    with nc.Dataset(first_nc) as f:
        t_var = f.variables['time']
        if len(t_var) > 1:
            gap = float(t_var[1] - t_var[0])
            if   gap > 305: timeStepType = "yearly"
            elif gap > 25:  timeStepType = "monthly"
            elif gap > 5:   timeStepType = "weekly"
            else:           timeStepType = "daily"
        else:
            timeStepType = "single"

    print('Temporal resolution: %s' % timeStepType)

    sd = str(startDate).split('-')
    startTime = datetime.datetime(int(sd[0]), int(sd[1]), int(sd[2]))
    ed = str(endDate).split('-')
    endTime   = datetime.datetime(int(ed[0]), int(ed[1]), int(ed[2]))

    if timeStepType == "daily":
        n = (endTime - startTime).days + 1
        datetime_range = [startTime + datetime.timedelta(days=x) for x in range(n)]
    elif timeStepType == "weekly":
        datetime_range = []
        for year in range(startTime.year, endTime.year + 1):
            current = datetime.datetime(year, 1, 7)
            end_of_year = datetime.datetime(year, 12, 31)
            while current <= end_of_year:
                datetime_range.append(current)
                current += datetime.timedelta(weeks=1)
            if datetime_range[-1] != end_of_year:
                datetime_range.append(end_of_year)
    elif timeStepType == "monthly":
        n = calculate_monthdelta(startTime, endTime) + 1
        datetime_range = [startTime + relativedelta(months=x) for x in range(n)]
        for i, dt in enumerate(datetime_range):
            last_day = calendar.monthrange(dt.year, dt.month)[1]
            day = 1 if fileType == "outStates" else last_day
            datetime_range[i] = datetime.datetime(dt.year, dt.month, day)
    elif timeStepType == "yearly":
        n = endTime.year - startTime.year + 1
        datetime_range = [datetime.datetime(startTime.year + x, 12, 31) for x in range(n)]
    else:
        datetime_range = [startTime]

    uniqueTimes = nc.date2num(datetime_range, time_units, time_calendar).tolist()
    nT = len(uniqueTimes)
    print('Output time steps: %d  (%s to %s)' % (nT, datetime_range[0], datetime_range[-1]))

    # ── Create output NetCDF on exact LDD grid ────────────────────────────
    # Auto-detect resolution from the first clone file
    with nc.Dataset(first_nc) as _f:
        for _k in _f.dimensions:
            if 'lat' in _k.lower(): _lv = _k
            if 'lon' in _k.lower(): _lo = _k
        _lats = _f.variables[_lv][:]
        _lons = _f.variables[_lo][:]
        deltaLat = abs(float(_lats[1] - _lats[0])) if len(_lats) > 1 else 0.5
        deltaLon = abs(float(_lons[1] - _lons[0])) if len(_lons) > 1 else 0.5

    LDD_LONS, LDD_LATS = make_ldd_grid(deltaLon, deltaLat)
    nLat, nLon = len(LDD_LATS), len(LDD_LONS)
    print('Output grid: %d x %d' % (nLon, nLat))

    out = nc.Dataset(netCDFOutput, 'w', format=ncFormat)
    out.createDimension('time',      nT)
    out.createDimension('latitude',  nLat)
    out.createDimension('longitude', nLon)

    time_var = out.createVariable('time', 'f8', ('time',))
    for attr, val in calendar_used.items():
        if attr != '_FillValue':
            setattr(time_var, attr, str(val))
    time_var[:] = uniqueTimes

    lat_var = out.createVariable('latitude',  'f4', ('latitude',))
    lat_var.standard_name = 'Latitude'
    lat_var.long_name     = 'Latitude cell centres'
    lat_var[:] = LDD_LATS

    lon_var = out.createVariable('longitude', 'f4', ('longitude',))
    lon_var.standard_name = 'Longitude'
    lon_var.long_name     = 'Longitude cell centres'
    lon_var[:] = LDD_LONS

    varStructure = ('time', 'latitude', 'longitude') if len(calendar_used) > 0 else ('latitude', 'longitude')
    data_var = out.createVariable(
        variableName, 'f4', varStructure,
        fill_value=MV, zlib=using_zlib, complevel=4
    )
    data_var.units = varUnits

    first_idx = list(attributes.keys())[0]
    for name in var_meta[first_idx][variableName].ncattrs():
        try:
            setattr(data_var, name, str(getattr(var_meta[first_idx][variableName], name)))
        except Exception:
            pass
    for attr, val in attributes[first_idx].items():
        setattr(out, attr, str(val))

    # pre-fill with MV
    CHUNK_T = 100
    mv_slab = np.full((CHUNK_T, nLat, nLon), MV, dtype='f4')
    for t0 in range(0, nT, CHUNK_T):
        t1 = min(t0 + CHUNK_T, nT)
        out.variables[variableName][t0:t1, :, :] = mv_slab[:t1 - t0]
    out.sync()
    out.close()
    print('Output file created and pre-filled.')

    # ── Build time lookup ─────────────────────────────────────────────────
    out_time_index = {round(float(t), 4): i for i, t in enumerate(uniqueTimes)}

    # ── Pass 2: merge clone files ─────────────────────────────────────────
    for index, ncFile in netCDFInput.items():
        if not os.path.isfile(ncFile):
            continue
        print('  Merging: %s' % ncFile)
        clone = nc.Dataset(ncFile, 'r')

        latVar = lonVar = None
        for key in dimensions[index]:
            if 'lat' in key.lower(): latVar = key
            if 'lon' in key.lower(): lonVar = key

        # Map clone lat/lon to LDD grid indices using nearest neighbour
        lat0_val = float(var_meta[index][latVar][0])
        lon0_val = float(var_meta[index][lonVar][0])
        row0   = int(np.argmin(np.abs(LDD_LATS - lat0_val)))
        col0   = int(np.argmin(np.abs(LDD_LONS - lon0_val)))
        n_rows = len(var_meta[index][latVar])
        n_cols = len(var_meta[index][lonVar])

        clone_t_raw  = clone.variables['time'][:]
        clone_t_units = clone.variables['time'].units
        clone_t_cal   = clone.variables['time'].calendar
        clone_datetimes  = nc.num2date(clone_t_raw, clone_t_units, clone_t_cal)
        clone_t_out_vals = nc.date2num(clone_datetimes, time_units, time_calendar)

        clone_idx_list = []
        out_idx_list   = []
        skipped = 0
        for ci, ct in enumerate(clone_t_out_vals):
            key = round(float(ct), 4)
            if key in out_time_index:
                clone_idx_list.append(ci)
                out_idx_list.append(out_time_index[key])
            else:
                nearest_key = min(out_time_index.keys(), key=lambda k: abs(k - key))
                if abs(nearest_key - key) < 0.5:
                    clone_idx_list.append(ci)
                    out_idx_list.append(out_time_index[nearest_key])
                else:
                    skipped += 1

        if skipped:
            print('    WARNING: %d timesteps skipped (no match)' % skipped)
        if not clone_idx_list:
            print('    No matching timesteps — clone skipped.')
            clone.close()
            continue

        clone_data = clone.variables[variableName][clone_idx_list, :, :]
        clone.close()

        if hasattr(clone_data, 'mask'):
            clone_arr = np.ma.filled(clone_data.astype('f4'), MV)
        else:
            clone_arr = np.array(clone_data, dtype='f4')

        valid = (clone_arr != MV) & ~np.isnan(clone_arr)

        out = nc.Dataset(netCDFOutput, 'a', format=ncFormat)
        out_var = out.variables[variableName]
        for local_i, out_i in enumerate(out_idx_list):
            vm = valid[local_i]
            if not vm.any():
                continue
            patch    = clone_arr[local_i]
            existing = np.array(out_var[out_i, row0:row0 + n_rows, col0:col0 + n_cols], dtype='f4')
            existing[vm] = patch[vm]
            out_var[out_i, row0:row0 + n_rows, col0:col0 + n_cols] = existing
        out.sync()
        out.close()
        print('    rows %d:%d  cols %d:%d  (%d timesteps written)'
              % (row0, row0 + n_rows, col0, col0 + n_cols, len(out_idx_list)))

    secs = int(tm.time() - scriptStartTime)
    print("Processing %s took %s hh:mm:ss\n" % (ncName, str(datetime.timedelta(seconds=secs))))


# ===========================================================================
# Command-line interface  (identical to original)
# ===========================================================================

inputDirRoot = sys.argv[1]
outputDir    = sys.argv[2]

try:
    os.makedirs(outputDir)
except OSError:
    pass

file_type  = str(sys.argv[3])
startDate  = str(sys.argv[4])
endDate    = str(sys.argv[5])

netcdfList = list(set(str(sys.argv[6]).split(",")))
print('Raw variable list: %s' % netcdfList)

if file_type == "outDailyTotNC":    netcdfList = ['%s_dailyTot_output.nc'  % v for v in netcdfList]
if file_type == "outWeekTotNC":     netcdfList = ['%s_weekTot_output.nc'   % v for v in netcdfList]
if file_type == "outWeekAvgNC":     netcdfList = ['%s_weekAvg_output.nc'   % v for v in netcdfList]
if file_type == "outMonthTotNC":    netcdfList = ['%s_monthTot_output.nc'  % v for v in netcdfList]
if file_type == "outMonthAvgNC":    netcdfList = ['%s_monthAvg_output.nc'  % v for v in netcdfList]
if file_type == "outMonthEndNC":    netcdfList = ['%s_monthEnd_output.nc'  % v for v in netcdfList]
if file_type == "outAnnuaTotNC":    netcdfList = ['%s_annuaTot_output.nc'  % v for v in netcdfList]
if file_type == "outAnnuaAvgNC":    netcdfList = ['%s_annuaAvg_output.nc'  % v for v in netcdfList]
if file_type == "outAnnuaEndNC":    netcdfList = ['%s_annuaEnd_output.nc'  % v for v in netcdfList]
if file_type == "outMonthMaxNC":    netcdfList = ['%s_monthMax_output.nc'  % v for v in netcdfList]
if file_type == "outAnnuaMaxNC":    netcdfList = ['%s_annuaMax_output.nc'  % v for v in netcdfList]
if file_type == "out_month_totNC":  netcdfList = ['%s_monthly_tot.nc'      % v for v in netcdfList]
if file_type == "out_month_avgNC":  netcdfList = ['%s_monthly_avg.nc'      % v for v in netcdfList]
if file_type == "outStates":        netcdfList = ['%s.nc'                  % v for v in netcdfList]

ncFormat            = str(sys.argv[7])
using_zlib          = str(sys.argv[8])
max_number_of_cores = int(sys.argv[9])
number_of_clones    = int(sys.argv[10])

all_areas    = ['M%02d' % i for i in range(1, number_of_clones + 1)]
folder_check = 'states' if file_type == 'outStates' else 'netcdf'
areas = [a for a in all_areas
         if os.path.isdir(os.path.join(inputDirRoot, a, folder_check))]
print("Requested %d clone areas, found %d existing: %s"
      % (number_of_clones, len(areas), areas))

using_MV = str(sys.argv[12])

ncores = min(len(netcdfList), max_number_of_cores)
ll = []
for ncName in netcdfList:
    ll.append((ncName, startDate, endDate, ncFormat, using_zlib, using_MV, file_type))

pool = Pool(processes=ncores)
pool.map(mergeNetCDF, ll)
pool.terminate()
pool.join()

sys.exit()
