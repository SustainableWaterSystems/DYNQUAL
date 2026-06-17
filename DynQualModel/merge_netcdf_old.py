#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

#
# PCR-GLOBWB (PCRaster Global Water Balance) Global Hydrological Model
#
# Copyright (C) 2016, Edwin H. Sutanudjaja, Rens van Beek, Niko Wanders, Yoshihide Wada,
# Joyce H. C. Bosmans, Niels Drost, Ruud J. van der Ent, Inge E. M. de Graaf, Jannis M. Hoch,
# Kor de Jong, Derek Karssenberg, Patricia López López, Stefanie Peßenteiner, Oliver Schmitz,
# Menno W. Straatsma, Ekkamol Vannametee, Dominik Wisser, and Marc F. P. Bierkens
# Faculty of Geosciences, Utrecht University, Utrecht, The Netherlands
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os, sys, datetime, glob, calendar
import time as tm
import numpy as np
import netCDF4 as nc
from multiprocessing import Pool
from dateutil.relativedelta import relativedelta


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


def getMax(x, a):
    m = float(np.max(a))
    return m if x is None else max(m, x)


def getMin(x, a):
    m = float(np.min(a))
    return m if x is None else min(m, x)


def ncFileNameDict(inputDirRoot, areas, ncFileName, fileType):
    """Creates an ordered dict {1: path, 2: path, ...} of per-clone files."""
    folder = 'states' if fileType == 'outStates' else 'netcdf'
    d = {}
    for i, area in enumerate(areas, start=1):
        d[i] = os.path.join(inputDirRoot, area, folder, ncFileName)
    return d


# ---------------------------------------------------------------------------
# Core merge function  (one call per variable name, runs in a worker process)
# ---------------------------------------------------------------------------

def mergeNetCDF(inputTuple):

    ncName      = inputTuple[0]
    latMin      = inputTuple[1]
    latMax      = inputTuple[2]
    lonMin      = inputTuple[3]
    lonMax      = inputTuple[4]
    deltaLat    = inputTuple[5]
    deltaLon    = inputTuple[6]
    startDate   = inputTuple[7]
    endDate     = inputTuple[8]
    ncFormat    = inputTuple[9]
    using_zlib  = inputTuple[10]
    using_MV    = inputTuple[11]
    fileType    = inputTuple[12]

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

    # -----------------------------------------------------------------------
    # Pass 1: collect metadata from every clone file (no data arrays yet)
    # -----------------------------------------------------------------------
    attributes    = {}
    dimensions    = {}
    var_meta      = {}       # stores Variable proxy objects for coord info
    variableName  = None
    calendar_used = {}
    MV            = None
    varUnits      = None

    for index, ncFile in netCDFInput.items():
        if not os.path.isfile(ncFile):
            print("  WARNING: file not found, skipping: %s" % ncFile)
            continue

        rootgrp = nc.Dataset(ncFile)
        dimensions[index] = rootgrp.dimensions.copy()
        var_meta[index]   = rootgrp.variables.copy()
        attributes[index] = rootgrp.__dict__.copy()

        # identify lat/lon dimension names (handles 'lat', 'latitude', etc.)
        latVar = lonVar = None
        for key in dimensions[index]:
            if 'lat' in key.lower(): latVar = key
            if 'lon' in key.lower(): lonVar = key

        latMin = getMin(latMin, var_meta[index][latVar][:])
        latMax = getMax(latMax, var_meta[index][latVar][:])
        lonMin = getMin(lonMin, var_meta[index][lonVar][:])
        lonMax = getMax(lonMax, var_meta[index][lonVar][:])

        # calendar / time units — must be consistent across clones
        if 'time' in var_meta[index]:
            for name in rootgrp.variables['time'].ncattrs():
                val = getattr(rootgrp.variables['time'], name)
                if name not in calendar_used:
                    calendar_used[name] = val
                else:
                    if val != calendar_used[name]:
                        rootgrp.close()
                        sys.exit(
                            'ERROR: incompatible time attribute "%s" in %s'
                            % (name, ncFile)
                        )

        # identify the data variable (everything that is not a dimension coord)
        data_keys = [k for k in var_meta[index] if k not in dimensions[index]]
        if not data_keys:
            rootgrp.close()
            sys.exit('ERROR: no data variable found in %s' % ncFile)
        key = data_keys[0]
        if variableName is None:
            variableName = key
        elif key != variableName:
            rootgrp.close()
            sys.exit(
                'ERROR: variable name mismatch ("%s" vs "%s") in %s'
                % (variableName, key, ncFile)
            )

        # fill value
        if using_MV is True:
            MV = -999.9000244140625
        else:
            MV = float(rootgrp.variables[key]._FillValue)

        varUnits = str(rootgrp.variables[variableName].units)
        rootgrp.close()

    if variableName is None:
        print('ERROR: no valid clone files found for %s, skipping.' % ncName)
        return

    # -----------------------------------------------------------------------
    # Build output time axis
    # -----------------------------------------------------------------------
    time_units    = calendar_used.get('units', 'days since 1901-01-01 00:00:00')
    time_calendar = calendar_used.get('calendar', 'standard')

    # detect temporal resolution from the first available file
    first_nc = next(
        (p for p in netCDFInput.values() if os.path.isfile(p)), None
    )
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

    print('Temporal resolution detected: %s' % timeStepType)

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
            current     = datetime.datetime(year, 1, 7)
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
        datetime_range = [
            datetime.datetime(startTime.year + x, 12, 31) for x in range(n)
        ]

    else:  # single
        datetime_range = [startTime]

    uniqueTimes = nc.date2num(datetime_range, time_units, time_calendar).tolist()
    nT = len(uniqueTimes)
    print('Output time steps: %d  (%s to %s)' % (nT, datetime_range[0], datetime_range[-1]))

    # -----------------------------------------------------------------------
    # Create output netCDF (pre-filled with MV)
    # -----------------------------------------------------------------------
    longitudes = np.around(
        np.arange(lonMin, lonMax + deltaLon, deltaLon), decimals=3
    )
    latitudes  = np.around(
        np.arange(latMax, latMin - deltaLat, -deltaLat), decimals=3
    )
    nLat, nLon = len(latitudes), len(longitudes)

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
    lat_var[:] = latitudes

    lon_var = out.createVariable('longitude', 'f4', ('longitude',))
    lon_var.standard_name = 'Longitude'
    lon_var.long_name     = 'Longitude cell centres'
    lon_var[:] = longitudes

    varStructure = (
        ('time', 'latitude', 'longitude') if len(calendar_used) > 0
        else ('latitude', 'longitude')
    )
    data_var = out.createVariable(
        variableName, 'f4', varStructure,
        fill_value=MV, zlib=using_zlib
    )
    data_var.units = varUnits

    # copy variable and global attributes from the first valid clone
    first_idx = list(attributes.keys())[0]
    for name in var_meta[first_idx][variableName].ncattrs():
        try:
            setattr(data_var, name,
                    str(getattr(var_meta[first_idx][variableName], name)))
        except Exception:
            pass
    for attr, val in attributes[first_idx].items():
        setattr(out, attr, str(val))

    # pre-fill with MV in manageable chunks (avoids one giant allocation)
    CHUNK_T = 100
    mv_slab = np.full((CHUNK_T, nLat, nLon), MV, dtype='f4')
    for t0 in range(0, nT, CHUNK_T):
        t1 = min(t0 + CHUNK_T, nT)
        out.variables[variableName][t0:t1, :, :] = mv_slab[:t1 - t0]

    out.sync()
    out.close()
    print('Output file created and pre-filled.')

    # -----------------------------------------------------------------------
    # Build a fast output-time lookup:  rounded_numeric_value -> output index
    # Using 4 decimal-place rounding (< 2 minutes precision for daily data)
    # -----------------------------------------------------------------------
    out_time_index = {round(float(t), 4): i for i, t in enumerate(uniqueTimes)}

    # -----------------------------------------------------------------------
    # Pass 2: one clone at a time — read ALL timesteps in a single array call
    # -----------------------------------------------------------------------
    for index, ncFile in netCDFInput.items():
        if not os.path.isfile(ncFile):
            continue
        print('  Merging: %s' % ncFile)

        clone = nc.Dataset(ncFile, 'r')

        # --- spatial position in the output grid ---
        latVar = lonVar = None
        for key in dimensions[index]:
            if 'lat' in key.lower(): latVar = key
            if 'lon' in key.lower(): lonVar = key

        lat0_val = round(float(var_meta[index][latVar][0]),  3)
        lon0_val = round(float(var_meta[index][lonVar][0]),  3)
        row0   = int(np.argmin(np.abs(latitudes  - lat0_val)))
        col0   = int(np.argmin(np.abs(longitudes - lon0_val)))
        n_rows = len(var_meta[index][latVar])
        n_cols = len(var_meta[index][lonVar])

        # --- map clone time indices to output time indices ---
        clone_t_raw   = clone.variables['time'][:]
        clone_t_units = clone.variables['time'].units
        clone_t_cal   = clone.variables['time'].calendar

        # re-express clone times in the OUTPUT time units (avoids unit mismatch)
        clone_datetimes   = nc.num2date(clone_t_raw, clone_t_units, clone_t_cal)
        clone_t_out_vals  = nc.date2num(clone_datetimes, time_units, time_calendar)

        clone_idx_list = []
        out_idx_list   = []
        skipped = 0
        for ci, ct in enumerate(clone_t_out_vals):
            key = round(float(ct), 4)
            if key in out_time_index:
                clone_idx_list.append(ci)
                out_idx_list.append(out_time_index[key])
            else:
                # nearest-neighbour fallback within 0.5-day tolerance
                nearest_key = min(out_time_index.keys(), key=lambda k: abs(k - key))
                if abs(nearest_key - key) < 0.5:
                    clone_idx_list.append(ci)
                    out_idx_list.append(out_time_index[nearest_key])
                else:
                    skipped += 1

        if skipped:
            print('    WARNING: %d clone timesteps had no match in output '
                  'and were skipped.' % skipped)

        if not clone_idx_list:
            print('    No matching timesteps - clone skipped entirely.')
            clone.close()
            continue

        # --- single read: all matched timesteps, full spatial extent ---
        clone_data = clone.variables[variableName][clone_idx_list, :, :]
        clone.close()

        # convert masked array to plain numpy, replacing masked values with MV
        if hasattr(clone_data, 'mask'):
            clone_arr = np.ma.filled(clone_data.astype('f4'), MV)
        else:
            clone_arr = np.array(clone_data, dtype='f4')

        # valid = not MV and not NaN
        valid = (clone_arr != MV) & ~np.isnan(clone_arr)

        # --- write into output (read-modify-write per timestep) ---
        out = nc.Dataset(netCDFOutput, 'a', format=ncFormat)
        out_var = out.variables[variableName]

        for local_i, out_i in enumerate(out_idx_list):
            vm = valid[local_i]      # [n_rows, n_cols] boolean
            if not vm.any():
                continue
            patch    = clone_arr[local_i]                                    # [n_rows, n_cols]
            existing = np.array(
                out_var[out_i, row0:row0 + n_rows, col0:col0 + n_cols],
                dtype='f4'
            )
            existing[vm] = patch[vm]
            out_var[out_i, row0:row0 + n_rows, col0:col0 + n_cols] = existing

        out.sync()
        out.close()

        print('    rows %d:%d  cols %d:%d  (%d timesteps written)'
              % (row0, row0 + n_rows, col0, col0 + n_cols, len(out_idx_list)))

    secs = int(tm.time() - scriptStartTime)
    print("Processing %s took %s hh:mm:ss\n"
          % (ncName, str(datetime.timedelta(seconds=secs))))


# ===========================================================================
#  User input (command-line arguments — identical interface to original)
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

# list of variable names / file names
netcdfList = str(sys.argv[6])
print('Raw variable list: %s' % netcdfList)
netcdfList = list(set(netcdfList.split(",")))

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

ncFormat         = str(sys.argv[7])
using_zlib       = str(sys.argv[8])
max_number_of_cores = int(sys.argv[9])
number_of_clones    = int(sys.argv[10])

# Build clone list, filtering to only directories that actually exist
all_areas   = ['M%02d' % i for i in range(1, number_of_clones + 1)]
folder_check = 'states' if file_type == 'outStates' else 'netcdf'
areas = [a for a in all_areas
         if os.path.isdir(os.path.join(inputDirRoot, a, folder_check))]
print("Requested %d clone areas, found %d existing: %s"
      % (number_of_clones, len(areas), areas))

# Auto-detect resolution from the first available input file
folder    = 'states' if file_type == 'outStates' else 'netcdf'
first_nc  = os.path.join(inputDirRoot, areas[0], folder, netcdfList[0])
with nc.Dataset(first_nc) as _f:
    for _key in _f.dimensions.keys():
        if 'lat' in _key.lower(): _latVar = _key
        if 'lon' in _key.lower(): _lonVar = _key
    _lats = _f.variables[_latVar][:]
    _lons = _f.variables[_lonVar][:]
    deltaLat = round(float(abs(_lats[1] - _lats[0])), 8)
    deltaLon = round(float(abs(_lons[1] - _lons[0])), 8)
print("Auto-detected resolution: deltaLat=%.8f  deltaLon=%.8f" % (deltaLat, deltaLon))

latMin = -90  + deltaLat / 2.0
latMax =  90  - deltaLat / 2.0
lonMin = -180 + deltaLon / 2.0
lonMax =  180 - deltaLon / 2.0

# optional extent override
if sys.argv[11] == "all_lats":
    latMin = -90  + deltaLat / 2.0
    latMax =  90  - deltaLat / 2.0

if sys.argv[11] == "defined":
    cellsize_in_arcsec = float(sys.argv[12])
    xmin = float(sys.argv[13])
    ymin = float(sys.argv[14])
    xmax = float(sys.argv[15])
    ymax = float(sys.argv[16])
    half = cellsize_in_arcsec / (2.0 * 3600.0)
    lonMin = xmin + half
    latMin = ymin + half
    lonMax = xmax - half
    latMax = ymax - half

using_MV = str(sys.argv[12])

# Build task list and dispatch
ncores = min(len(netcdfList), max_number_of_cores)
ll = []
for ncName in netcdfList:
    ll.append((
        ncName, latMin, latMax, lonMin, lonMax,
        deltaLat, deltaLon,
        startDate, endDate,
        ncFormat, using_zlib, using_MV, file_type
    ))

pool = Pool(processes=ncores)
pool.map(mergeNetCDF, ll)
pool.terminate()
pool.join()

sys.exit()
