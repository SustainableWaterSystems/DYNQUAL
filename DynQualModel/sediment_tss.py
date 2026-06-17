#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pcraster as pcr
import virtualOS as vos

###----------------------------------------------------------##
#  RUSLE sediment delivery functions (adapted from PCR-GLOBST #
###----------------------------------------------------------##

def computeSlopeFactor(slopeLength, slopeGradient):
    #LS factor: slope length (m) * steepness (m/m) (Renard 1997 / Nearing 1997)
    
    gamma = pcr.min(1.0, 1.183156498 * slopeGradient ** 0.351920534)
    slopeLengthFactor = (slopeLength / 22.13) ** gamma
    slopeAngle = pcr.atan(slopeGradient)
    slopeSteepnessFactor = -1.5 + (17.0 / (1.0 + pcr.exp(2.3 - 6.1 * pcr.sin(slopeAngle))))
    return slopeLengthFactor * slopeSteepnessFactor

def computeAnnualErosivity(annualPrecipitation_mm):
    #annual erosivity R factor (MJ*mm/ha/hr/yr) from annual rainfall (Renard & Freimund 1994)

    return pcr.ifthenelse(
        annualPrecipitation_mm <= 850.0,
        0.0483 * annualPrecipitation_mm ** 1.61,
        587.8 - 1.219 * annualPrecipitation_mm + 0.00415 * annualPrecipitation_mm ** 2
    )

def computeDefaultSoilErodibility(massFractionSand, massFractionSilt, massFractionClay, organicMatterContent=None):
    #soil erodibility K factor (t*ha*h/ha/MJ/mm) from soil texture (Yang et al. 2003)
    
    if organicMatterContent is None:
        organicMatterContent = pcr.scalar(1.0)
    dg = -3.5 * massFractionSand - 2.0 * massFractionSilt - 0.5 * massFractionClay
    omc = pcr.ifthenelse(massFractionClay > 0.001,
        organicMatterContent / pcr.max(0.001, massFractionClay), pcr.scalar(0.0))
    e_omc = (-0.0021 * omc - 0.00037 * omc ** 2
             - 4.02 * massFractionClay + 1.72 * massFractionClay ** 2)
    return 0.0293 * (0.65 - dg + 0.24 * dg ** 2) * pcr.exp(e_omc)

def computeKFactorSeasonality(massFractionSand, massFractionSilt, massFractionClay):
    #seasonal K factor ratio (-) by soil texture class (Hoch 2014)
    
    kSeasonal = pcr.scalar(1.44)
    kSeasonal = pcr.ifthenelse(massFractionClay > 0.35, pcr.scalar(1.17), kSeasonal)
    kSeasonal = pcr.ifthenelse(
        (massFractionClay < 0.18) & (massFractionSand > 0.65),
        pcr.scalar(4.50), kSeasonal)
    kSeasonal = pcr.ifthenelse(
        (massFractionClay <= 0.35) & (massFractionSand <= 0.65),
        pcr.scalar(1.44), kSeasonal)
    return kSeasonal

def computeMeltTimeFraction(tMin, tMax):
    #melt time fraction of day above freezing (used for K factor seasonality)
    
    tRange = pcr.max(0.001, tMax - tMin)
    meltFrac = pcr.max(0.0, tMax) / tRange
    return pcr.min(1.0, pcr.max(0.0, meltFrac))

def computeKFactorDaily(kYear, kSeasonal, meltTimeFraction):
    #daily K factor with seasonality correction
    
    return kYear * (1.0 + (kSeasonal - 1.0) * (1.0 - meltTimeFraction))

def computeErosivityDaily(precipDay_mm, precipAnnual_mm, rYear):
    #partition annual erosivity to daily (MJ*mm/ha/hr/day) timestep based on rainfall fraction
    
    avgDaily_mm = precipAnnual_mm / 365.25
    fraction = pcr.ifthenelse(precipAnnual_mm > 0.0,
        precipDay_mm / pcr.max(precipDay_mm, avgDaily_mm), pcr.scalar(0.0))
    return pcr.max(0.0, fraction) * rYear

def computeVegCoverFactor(ndvi, alpha=2.0, beta=1.0):
    #Vegetation cover factor C (-) based on NDVI (Van der Knijff et al. 1999)
    
    return pcr.min(1.0, pcr.exp(-alpha * ndvi / pcr.max(0.01, beta - ndvi)))

def computeManningWithNDVI(slopeGradient, ndvi):
    #Mannings roughness coefficient [s/m^(1/3)] n combining slope-based roughness and vegetation influence
    
    slopePerc = slopeGradient * 100.0
    
    n1 = pcr.ifthenelse(slopePerc < 0.5, pcr.scalar(0.20),
         pcr.ifthenelse(slopePerc < 2.0, pcr.scalar(0.10),
         pcr.ifthenelse(slopePerc < 5.0, pcr.scalar(0.07),
         pcr.scalar(0.05))))
    n2 = pcr.scalar(0.049) #channel base roughness
    nVeg = pcr.max(0.0, ndvi) * 0.10 #vegetation contribution
    return n1 + n2 + nVeg

def computeHydroCoefficient(surfaceRunoff_mm, rainfall_mm):
    #Hydrological coefficient (-): ratio of surface runoff to rainfall [0-1]
    
    ratio = pcr.cover(surfaceRunoff_mm / pcr.max(0.001, rainfall_mm), pcr.scalar(0.0001))
    return pcr.min(1.0, pcr.max(0.0, ratio))

def computeDeliveryRatio(hydroCoeff, slopeGradient, manningN, slopeLength):
    #Sediment delivery ratio (Van Dijk 2001): delivery ratio = min(1, alpha * ((H * sqrt(S)) / (n * L))^beta)
    
    alpha = pcr.scalar(9.53)
    beta = pcr.scalar(0.79)
    slopePerc = slopeGradient * 100.0
    tmp = (hydroCoeff * pcr.sqrt(slopePerc)) / pcr.max(0.001, manningN * slopeLength)
    return pcr.min(1.0, pcr.max(0.0, alpha * tmp ** beta))

def computeSoilLoss(erosivity, erodibility, slopeFactor, vegCoverFactor, conservationFactor, cellArea_m2):
    #RUSLE soil loss [tonnes/day] (Renard et al. 1997): A = R * K * LS * C * P * (cellArea / 10000)
    ##erosivity: Daily R factor [MJ*mm/ha/hr/day]
    ##erodibility: K factor [t*ha*h/ha/MJ/mm]
    ##slopeFactor: LS factor [-]
    ##vegCoverFactor: C factor [-]
    ##conservationFactor: P factor [-]
    ##cellArea_m2: Cell area [m2]
    
    return (erosivity * erodibility * slopeFactor * vegCoverFactor * conservationFactor * cellArea_m2 / 10000.0)

###----------------------------------------------##
#    Transport capacity functions (Govers 1990)   #
###----------------------------------------------##

def computeStreamPowerCoefficients(particleDiameter):
    #compute c, d coefficients for transport capacity (Govers 1990); needs particle diameter in m
    
    cOmega = ((1.0e6 * particleDiameter + 5.0) / 0.32) ** -0.6
    dOmega = min(1.0, ((1.0e6 * particleDiameter + 5.0) / 300.0) ** 0.25)
    return cOmega, dOmega

def computeUnitStreamPower(flowVelocity, gradient):
    #compute unit stream power (m/s) using flow velocity (m/s) and channel gradient (-)
    
    return flowVelocity * gradient

def correctLowTransportCapacity(unitStreamPower, thresholdUnitStreamPower):
    #correction for low stream power (Woolhiser/Kineros)
    
    return pcr.ifthenelse(
        unitStreamPower <= thresholdUnitStreamPower,
        (3.0 - 2.0 * unitStreamPower / thresholdUnitStreamPower) * 
        (unitStreamPower / thresholdUnitStreamPower) ** 2,
        1.0
    )

def computeTransportCapacity(particleDiameter, particleDensity, unitStreamPower, criticalUnitStreamPower, thresholdUnitStreamPower, applyScaling=False):
    #compute transport capacity (kg/m3) using Govers (1990) equation
    ##needs: particleDiameter (m), particle density (km/m3), unitStreamPower (m/s),
    ##       criticalUnitStreamPower (m/s), thresholdUnitStreamPower (m/s)
 
    cOmega, dOmega = computeStreamPowerCoefficients(particleDiameter)
    
    if applyScaling:
        transportCapacity = particleDensity * cOmega * (
            pcr.max(0.0, pcr.max(unitStreamPower, thresholdUnitStreamPower) - criticalUnitStreamPower)
        ) ** dOmega
        correction = correctLowTransportCapacity(unitStreamPower, 
                                               pcr.max(criticalUnitStreamPower, thresholdUnitStreamPower))
        transportCapacity *= correction
    else:
        transportCapacity = particleDensity * cOmega * (
            pcr.max(0.0, unitStreamPower - criticalUnitStreamPower)
        ) ** dOmega
        correction = pcr.scalar(0.0)
    
    return transportCapacity, cOmega, dOmega, correction

def computeTrappingEfficiency(vFlow, vSettle, method='linear'):
    #compute trapping efficiency for sediment settling (m/s) based on velocity (m/s)
    
    vFlow = pcr.max(1.0e-6, vFlow)
    velocityRatio = vSettle / vFlow
    velocityRatio = pcr.min(velocityRatio, 100.0) #cap very high ratios
    
    if method == 'linear':
        fractionTE = pcr.min(0.99, velocityRatio) #cap at 99%
        
    elif method == 'exponential':
        fractionTE = 1.0 - pcr.exp(-velocityRatio)
        fractionTE = pcr.min(0.99, fractionTE) #cap at 99%
        
    else:
        fractionTE = pcr.scalar(0.99) #99%
     
    fractionTE = pcr.max(0.0, fractionTE) #ensure trapping efficiency is not negative
    
    return fractionTE


def computeEffectiveSettlingVelocity(particleDiameter, a=710.0, b=1.57):
    #effective settling velocity in m/s (Thonon 2006); v_s = a * D^b
    
    return a * particleDiameter ** b


###----------------------------------------------##
#          Hydraulic channel functions            #
###----------------------------------------------##

def computeChannelAlpha(wettedPerimeter, manningN, channelGradient, channelBeta):
    #compute alpha coefficient for Q-area relationship
    
    return (wettedPerimeter ** (2.0 / 3.0) * manningN * channelGradient ** -0.5) ** channelBeta

def estimateWaterDepth(discharge, channelAlpha, channelWidth, channelGradient, manningN, channelBeta, convergenceCrit=0.0001):
    #estimate water depth for rectangular channel, iteratively
    
    iCnt = 0
    convergence = 2 * convergenceCrit
    waterDepth = (channelAlpha * discharge ** channelBeta) / channelWidth
    wettedPerimeter = channelWidth + 2 * waterDepth
    
    while convergence > convergenceCrit and iCnt < 100:
        iCnt += 1
        waterDepthOld = waterDepth
        channelAlpha = computeChannelAlpha(wettedPerimeter, manningN, channelGradient, channelBeta)
        waterDepth = (channelAlpha * discharge ** channelBeta) / channelWidth
        wettedPerimeter = channelWidth + 2 * waterDepth
        convergence = pcr.cellvalue(pcr.mapmaximum(pcr.abs(waterDepth - waterDepthOld)), 1)[0]
    
    return waterDepth, channelAlpha


###----------------------------------------------##
#    Sediment trapping efficiency methods         #
###----------------------------------------------##

def computeBruneTrappingEfficiency(capacity, inflow):
    #Brune (1953); TE = 1 - 1/(1 + k*C/I) where k = 0.046
    ##capacity is reservoir storage capacity in m3; inflow is annual inflow in m3/yr
    
    k_brune = 0.046 #Brunes empirical coefficient
    
    #Input validation
    capacity = pcr.max(capacity, 1.0)
    inflow = pcr.max(inflow, 1.0)
    
    CI_ratio = capacity / inflow
    CI_ratio = pcr.max(CI_ratio, 1e-4)
    CI_ratio = pcr.min(CI_ratio, 1000.0)
    
    #Brune formula
    TE = 1.0 - 1.0 / (1.0 + k_brune * CI_ratio)
    
    return pcr.max(0.0, pcr.min(0.99, TE)) #max 99%

def computeChurchillTrappingEfficiency(capacity, area, outflow, settlingVelocity):
    #Churchill (1948); TE = 1 - 1/(1 + alpha*SI^beta) where alpha=0.0021, beta=0.58 and SI = (Volume x Depth) / (Discharge x Settling_velocity)
    ##capacity in m3, area in m2, outflow in m3/s and settling velocity in m/s
    
    #coefficients
    alpha_churchill = 0.0021
    beta_churchill = 0.58
    
    #Input validation
    capacity = pcr.max(capacity, 1.0)
    area = pcr.max(area, 1.0)
    outflow = pcr.max(outflow, 1e-3)
    settlingVelocity = pcr.max(settlingVelocity, 1e-6)

    avgDepth = capacity / area
    avgDepth = pcr.max(avgDepth, 0.1)
    avgDepth = pcr.min(avgDepth, 100.0)
    
    SI = (capacity * avgDepth) / (outflow * settlingVelocity)
    SI = pcr.max(SI, 0.1)
    SI = pcr.min(SI, 10000.0)
    
    #Churchill formula
    TE = 1.0 - 1.0 / (1.0 + alpha_churchill * SI**beta_churchill)
    
    return pcr.max(0.0, pcr.min(0.99, TE)) #max 99%

def computeBrownTrappingEfficiency(capacity, inflow):
    #Brown (1943) hyperbolic relationship; TE = (C/I) / (1 + C/I)
    ##capacity in m3; inflow in m3/yr
    
    #Input validation
    capacity = pcr.max(capacity, 1.0)
    inflow = pcr.max(inflow, 1.0)
    
    CI_ratio = capacity / inflow
    CI_ratio = pcr.max(CI_ratio, 1e-4)
    CI_ratio = pcr.min(CI_ratio, 1000.0)
    
    #Brown formula
    TE = CI_ratio / (1.0 + CI_ratio)
    
    return pcr.max(0.0, pcr.min(0.99, TE)) #max 99%


###----------------------------------------------##
#            TSS debugging functions              #
###----------------------------------------------##

def debugTSSRouting(day, i_loop, number_of_loops, sedimentLoad, availableSedimentStock,
                   subDischarge, yMean, wMean, wettedArea, flowVelocity, unitStreamPower, 
                   transportCapacity, sedimentConcentration, capacityExcess, capacityDeficit,
                   sedimentUptakeBeforeLimit, sedimentUptake, sedimentDeposition,
                   entrainment_kg, deposition_kg, netSedimentChange,
                   sedimentLoadBefore, sedimentLoadAfter, stockBefore, stockAfter,
                   sedimentUptakeFactor, landmask, waterBodies):

    if day > 3:
        return
    
    if i_loop == 0:
        _debugSedimentInput(day, number_of_loops, sedimentLoad, availableSedimentStock)
    
    if i_loop == 1:
        _debugHydraulics(day, i_loop, subDischarge, yMean, wMean, wettedArea, 
                        flowVelocity, unitStreamPower, transportCapacity)
        
        _debugEntrainment(day, i_loop, sedimentConcentration, capacityExcess,
                         sedimentUptakeBeforeLimit, sedimentUptake, availableSedimentStock,
                         sedimentUptakeFactor, landmask, waterBodies)
        
        _debugDeposition(capacityDeficit, sedimentDeposition)
        
        _debugMassBalance(day, i_loop, entrainment_kg, deposition_kg, netSedimentChange,
                         sedimentLoadBefore, sedimentLoadAfter, stockBefore, stockAfter)

def debugTSSRoutingFinal(day, i_loop, maxTransFrac, totalTransport, loadBeforeRouting, loadAfterRouting):

    if day <= 3 and i_loop == 1:
        print(f"TSS DEBUG - Day {day} - SUBSTEP {i_loop+1} - ROUTING")
        print(f"  Transport fraction: max={maxTransFrac:.4f}")
        print(f"  Sediment transport: {totalTransport:.4f} kg")
        print(f"  Load after routing: before={loadBeforeRouting:.2f}, after={loadAfterRouting:.2f} kg")
        print()

def debugTrappingEfficiency(day, method, waterBodies, landmask, flowVelocity, settlingVelocity, 
                           trapping_eff, constantTrappingEfficiency=None):

    if day > 3:
        return
    
    waterBodyMask = pcr.scalar(waterBodies.waterBodyIds) > 0
    waterBodyCount = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse(waterBodyMask, pcr.scalar(1), pcr.scalar(0))), 1)[0]
    
    if waterBodyCount == 0:
        print(f"\n=== {method.upper()} TRAPPING DEBUG - Day {day} ===")
        print("  No water bodies found!")
        return
    
    wbEfficiency = pcr.ifthen(waterBodyMask, trapping_eff)
    totalEfficiency = pcr.cellvalue(pcr.maptotal(wbEfficiency), 1)[0]
    validCells = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse(pcr.defined(wbEfficiency), pcr.scalar(1), pcr.scalar(0))), 1)[0]
    
    effStats = {
        'min': pcr.cellvalue(pcr.mapminimum(wbEfficiency), 1)[0],
        'max': pcr.cellvalue(pcr.mapmaximum(wbEfficiency), 1)[0], 
        'avg': totalEfficiency / max(validCells, 1)  # Manual average calculation
    }
    
    print(f"\n=== {method.upper()} TRAPPING DEBUG - Day {day} ===")
    print(f"  Water Bodies: {waterBodyCount:.0f} cells")
    print(f"  Trapping Efficiency: min={effStats['min']:.4f}, max={effStats['max']:.4f}, avg={effStats['avg']:.4f}")
    
    #Method specific debugging
    if method in ['velocity_lin', 'velocity_exp']:
        _debugVelocityMethod(method, waterBodyMask, flowVelocity, settlingVelocity)
        
    elif method == 'brune':
        _debugBruneMethod(waterBodies, waterBodyMask)
        
    elif method == 'churchill':
        _debugChurchillMethod(waterBodies, waterBodyMask, settlingVelocity)
        
    elif method == 'brown':
        _debugBrownMethod(waterBodies, waterBodyMask)
        
    elif method == 'constant':
        print(f"  CONSTANT EFFICIENCY: {constantTrappingEfficiency:.3f} ({100*constantTrappingEfficiency:.1f}%)")
    
    #efficiency distribution
    _debugEfficiencyDistribution(wbEfficiency)

def _debugSedimentInput(day, number_of_loops, sedimentLoad, availableSedimentStock):

    totalDaily = pcr.cellvalue(pcr.maptotal(sedimentLoad), 1)[0]
    perSubstep = totalDaily / float(number_of_loops)
    totalStock = pcr.cellvalue(pcr.maptotal(availableSedimentStock), 1)[0]
    
    print(f"\nTSS DEBUG - Day {day} - DRIP-FEED")
    print(f"  Daily input: {totalDaily:.2f} kg/day")
    print(f"  Per substep: {perSubstep:.2f} kg ({number_of_loops} substeps)")
    print(f"  Total available stock: {totalStock:.2f} kg")
    print()

def _debugHydraulics(day, i_loop, subDischarge, yMean, wMean, wettedArea, flowVelocity, unitStreamPower, transportCapacity):

    hydraulic_stats = {
        'discharge': pcr.cellvalue(pcr.mapmaximum(subDischarge), 1)[0],
        'depth': pcr.cellvalue(pcr.mapmaximum(yMean), 1)[0],
        'width': pcr.cellvalue(pcr.mapmaximum(wMean), 1)[0],
        'wetted_area_max': pcr.cellvalue(pcr.mapmaximum(wettedArea), 1)[0],
        'wetted_area_min': pcr.cellvalue(pcr.mapminimum(wettedArea), 1)[0],
        'velocity_max': pcr.cellvalue(pcr.mapmaximum(flowVelocity), 1)[0],
        'velocity_min': pcr.cellvalue(pcr.mapminimum(flowVelocity), 1)[0],
        'stream_power': pcr.cellvalue(pcr.mapmaximum(unitStreamPower), 1)[0],
        'transport_capacity': pcr.cellvalue(pcr.mapmaximum(transportCapacity), 1)[0]
    }
    
    print(f"TSS DEBUG - Day {day} - SUBSTEP {i_loop+1} - HYDRAULICS")
    print(f"  Discharge: max={hydraulic_stats['discharge']:.3f} m3/s")
    print(f"  Channel depth: max={hydraulic_stats['depth']:.3f} m")
    print(f"  Channel width: max={hydraulic_stats['width']:.1f} m")
    print(f"  Wetted area: max={hydraulic_stats['wetted_area_max']:.3f}, min={hydraulic_stats['wetted_area_min']:.3f} m2")
    print(f"  Flow velocity: max={hydraulic_stats['velocity_max']:.2f}, min={hydraulic_stats['velocity_min']:.2f} m/s")
    print(f"  Unit stream power: max={hydraulic_stats['stream_power']:.4f} m/s")
    print(f"  Transport capacity: max={hydraulic_stats['transport_capacity']:.6f} kg/m3")

def _debugEntrainment(day, i_loop, sedimentConcentration, capacityExcess, sedimentUptakeBeforeLimit, 
                     sedimentUptake, availableSedimentStock, sedimentUptakeFactor, landmask, waterBodies):

    entrainment_stats = {
        'concentration_total': pcr.cellvalue(pcr.maptotal(sedimentConcentration), 1)[0],
        'concentration_max': pcr.cellvalue(pcr.mapmaximum(sedimentConcentration), 1)[0],
        'capacity_excess_total': pcr.cellvalue(pcr.maptotal(capacityExcess), 1)[0],
        'capacity_excess_max': pcr.cellvalue(pcr.mapmaximum(capacityExcess), 1)[0],
        'uptake_before_limit': pcr.cellvalue(pcr.maptotal(sedimentUptakeBeforeLimit), 1)[0],
        'uptake_after_limit': pcr.cellvalue(pcr.maptotal(sedimentUptake), 1)[0],
        'available_stock': pcr.cellvalue(pcr.maptotal(availableSedimentStock), 1)[0]
    }
    
    channelCells = pcr.cellvalue(pcr.maptotal(pcr.scalar(pcr.ifthen(
        landmask, pcr.cover(pcr.scalar(waterBodies.waterBodyIds) == 0, pcr.boolean(True))
    ))), 1)[0]
    waterBodyCells = pcr.cellvalue(pcr.maptotal(pcr.scalar(
        pcr.scalar(waterBodies.waterBodyIds) > 0
    )), 1)[0]
    
    print(f"TSS DEBUG - Day {day} - SUBSTEP {i_loop+1} - ENTRAINMENT")
    print(f"  Sediment concentration: total={entrainment_stats['concentration_total']:.4f}, "
          f"max={entrainment_stats['concentration_max']:.6f} kg/m3")
    print(f"  Capacity excess: total={entrainment_stats['capacity_excess_total']:.4f}, "
          f"max={entrainment_stats['capacity_excess_max']:.6f} kg/m3")
    print(f"  Uptake factor: {sedimentUptakeFactor:.4f}")
    print(f"  Available stock: {entrainment_stats['available_stock']:.2f} kg")
    print(f"  Uptake: before limit={entrainment_stats['uptake_before_limit']:.4f}, "
          f"after limit={entrainment_stats['uptake_after_limit']:.4f} kg/s")
    print(f"  Cells: channels={channelCells:.0f}, water bodies={waterBodyCells:.0f}")

def _debugDeposition(capacityDeficit, sedimentDeposition):

    totalCapacityDeficit = pcr.cellvalue(pcr.maptotal(capacityDeficit), 1)[0]
    totalDeposition = pcr.cellvalue(pcr.maptotal(sedimentDeposition), 1)[0]
    
    print(f"  Capacity deficit: {totalCapacityDeficit:.4f} kg/m3")
    print(f"  Sediment deposition: {totalDeposition:.4f} kg/s")

def _debugMassBalance(day, i_loop, entrainment_kg, deposition_kg, netSedimentChange,
                     sedimentLoadBefore, sedimentLoadAfter, stockBefore, stockAfter):

    totalEntrainment = pcr.cellvalue(pcr.maptotal(entrainment_kg), 1)[0]
    totalDeposition = pcr.cellvalue(pcr.maptotal(deposition_kg), 1)[0]
    netChange = pcr.cellvalue(pcr.maptotal(netSedimentChange), 1)[0]
    
    print(f"TSS DEBUG - Day {day} - SUBSTEP {i_loop+1} - MASS BALANCE")
    print(f"  Entrainment: {totalEntrainment:.4f} kg (bed -> water)")
    print(f"  Deposition: {totalDeposition:.4f} kg (water -> bed)")
    print(f"  Net change to water column: {netChange:.4f} kg")
    print(f"  Load: before={sedimentLoadBefore:.2f}, after={sedimentLoadAfter:.2f} kg")
    print(f"  Stock: before={stockBefore:.2f}, after={stockAfter:.2f} kg")

def _debugVelocityMethod(method, waterBodyMask, flowVelocity, settlingVelocity):

    import math
    
    #Flow velocity stats
    wbFlowVel = pcr.ifthen(waterBodyMask, flowVelocity)
    totalFlowVel = pcr.cellvalue(pcr.maptotal(wbFlowVel), 1)[0]
    validFlowCells = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse(pcr.defined(wbFlowVel), pcr.scalar(1), pcr.scalar(0))), 1)[0]
    
    flowStats = {
        'min': pcr.cellvalue(pcr.mapminimum(wbFlowVel), 1)[0],
        'max': pcr.cellvalue(pcr.mapmaximum(wbFlowVel), 1)[0],
        'avg': totalFlowVel / max(validFlowCells, 1)
    }
    
    #Settling velocity (constant)
    settlingVel = pcr.cellvalue(pcr.mapmaximum(settlingVelocity), 1)[0]
    
    #Velocity ratio stats
    velocityRatio = pcr.ifthen(waterBodyMask, settlingVelocity / pcr.max(1e-6, flowVelocity))
    totalRatio = pcr.cellvalue(pcr.maptotal(velocityRatio), 1)[0]
    validRatioCells = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse(pcr.defined(velocityRatio), pcr.scalar(1), pcr.scalar(0))), 1)[0]
    
    ratioStats = {
        'min': pcr.cellvalue(pcr.mapminimum(velocityRatio), 1)[0],
        'max': pcr.cellvalue(pcr.mapmaximum(velocityRatio), 1)[0],
        'avg': totalRatio / max(validRatioCells, 1)
    }
    
    methodType = method.split('_')[1].upper()
    print(f"  VELOCITY-BASED METHOD ({methodType}):")
    print(f"    Settling velocity: {settlingVel:.6f} m/s")
    print(f"    Flow velocity: min={flowStats['min']:.6f}, max={flowStats['max']:.4f}, avg={flowStats['avg']:.4f} m/s")
    print(f"    Velocity ratio (vs/vf): min={ratioStats['min']:.2f}, max={ratioStats['max']:.2f}, avg={ratioStats['avg']:.2f}")
    
    if methodType == 'LINEAR':
        print(f"    Formula: TE = min(vs/vf, 0.99)")
        print(f"    Expected max TE: {min(0.99, ratioStats['max']):.4f}")
    else:
        print(f"    Formula: TE = 1 - exp(-vs/vf)")
        expectedMaxTE = 1.0 - math.exp(-ratioStats['max'])
        print(f"    Expected max TE: {expectedMaxTE:.4f}")

def _debugBruneMethod(waterBodies, waterBodyMask):

    import virtualOS as vos
    
    #calculate C/I ratios
    annualInflow = waterBodies.avgInflow * vos.secondsPerDay() * 365.25
    wbCapacity = pcr.ifthen(waterBodyMask, waterBodies.waterBodyStorage)  
    wbInflow = pcr.ifthen(waterBodyMask, annualInflow)
    CI_ratio = pcr.ifthen(waterBodyMask, waterBodies.waterBodyStorage / pcr.max(1.0, annualInflow))
    
    #statistics
    totalCapacity = pcr.cellvalue(pcr.maptotal(wbCapacity), 1)[0]
    validCapCells = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse(pcr.defined(wbCapacity), pcr.scalar(1), pcr.scalar(0))), 1)[0]
    
    totalInflow = pcr.cellvalue(pcr.maptotal(wbInflow), 1)[0]
    validInflowCells = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse(pcr.defined(wbInflow), pcr.scalar(1), pcr.scalar(0))), 1)[0]
    
    totalRatio = pcr.cellvalue(pcr.maptotal(CI_ratio), 1)[0]
    validRatioCells = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse(pcr.defined(CI_ratio), pcr.scalar(1), pcr.scalar(0))), 1)[0]
    
    capStats = {
        'min': pcr.cellvalue(pcr.mapminimum(wbCapacity), 1)[0],
        'max': pcr.cellvalue(pcr.mapmaximum(wbCapacity), 1)[0],
        'avg': totalCapacity / max(validCapCells, 1)
    }
    
    inflowStats = {
        'min': pcr.cellvalue(pcr.mapminimum(wbInflow), 1)[0],
        'max': pcr.cellvalue(pcr.mapmaximum(wbInflow), 1)[0],
        'avg': totalInflow / max(validInflowCells, 1)
    }
    
    ratioStats = {
        'min': pcr.cellvalue(pcr.mapminimum(CI_ratio), 1)[0],
        'max': pcr.cellvalue(pcr.mapmaximum(CI_ratio), 1)[0],
        'avg': totalRatio / max(validRatioCells, 1)
    }
    
    print(f"  BRUNE (1953) METHOD:")
    print(f"    Formula: TE = 1 - 1/(1 + 0.046*C/I)")
    print(f"    Capacity: min={capStats['min']:.2e}, max={capStats['max']:.2e}, avg={capStats['avg']:.2e} m3")
    print(f"    Annual inflow: min={inflowStats['min']:.2e}, max={inflowStats['max']:.2e}, avg={inflowStats['avg']:.2e} m/year")
    print(f"    C/I ratio: min={ratioStats['min']:.4f}, max={ratioStats['max']:.4f}, avg={ratioStats['avg']:.4f}")
    
    if ratioStats['max'] < 0.1:
        print(f"    ??  Very low C/I ratios ? expect low trapping efficiencies")
    elif ratioStats['max'] > 10.0:
        print(f"    ? High C/I ratios ? expect good trapping efficiencies")
    else:
        print(f"    ? Moderate C/I ratios ? expect medium trapping efficiencies")

def _debugChurchillMethod(waterBodies, waterBodyMask, settlingVelocity):

    import virtualOS as vos
    
    #calculate parameters
    outflowM3PerSec = waterBodies.waterBodyOutflow / vos.secondsPerDay()
    wbCapacity = pcr.ifthen(waterBodyMask, waterBodies.waterBodyStorage)
    wbArea = pcr.ifthen(waterBodyMask, waterBodies.waterBodyArea)  
    wbOutflow = pcr.ifthen(waterBodyMask, outflowM3PerSec)
    avgDepth = pcr.ifthen(waterBodyMask, waterBodies.waterBodyStorage / pcr.max(1.0, waterBodies.waterBodyArea))
    
    SI = pcr.ifthen(waterBodyMask, 
        (waterBodies.waterBodyStorage * avgDepth) / 
        (pcr.max(0.1, outflowM3PerSec) * settlingVelocity)
    )
    
    #statistics
    totalDepth = pcr.cellvalue(pcr.maptotal(avgDepth), 1)[0]
    validDepthCells = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse(pcr.defined(avgDepth), pcr.scalar(1), pcr.scalar(0))), 1)[0]
    
    totalSI = pcr.cellvalue(pcr.maptotal(SI), 1)[0]
    validSICells = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse(pcr.defined(SI), pcr.scalar(1), pcr.scalar(0))), 1)[0]
    
    depthStats = {
        'min': pcr.cellvalue(pcr.mapminimum(avgDepth), 1)[0],
        'max': pcr.cellvalue(pcr.mapmaximum(avgDepth), 1)[0],
        'avg': totalDepth / max(validDepthCells, 1)
    }
    
    siStats = {
        'min': pcr.cellvalue(pcr.mapminimum(SI), 1)[0],
        'max': pcr.cellvalue(pcr.mapmaximum(SI), 1)[0],
        'avg': totalSI / max(validSICells, 1)
    }
    
    settlingVel = pcr.cellvalue(pcr.mapmaximum(settlingVelocity), 1)[0]
    
    print(f"  CHURCHILL (1948) METHOD:")
    print(f"    Formula: TE = 1 - 1/(1 + 0.0021*SI^0.58), SI = (V*H)/(Q*vs)")
    print(f"    Avg depth: min={depthStats['min']:.2f}, max={depthStats['max']:.2f}, avg={depthStats['avg']:.2f} m")
    print(f"    Settling velocity: {settlingVel:.6f} m/s")
    print(f"    Sedimentation Index: min={siStats['min']:.2e}, max={siStats['max']:.2e}, avg={siStats['avg']:.2e}")

def _debugBrownMethod(waterBodies, waterBodyMask):

    import virtualOS as vos
    
    #calculate C/I ratio
    annualInflow = waterBodies.avgInflow * vos.secondsPerDay() * 365.25
    CI_ratio = pcr.ifthen(waterBodyMask, waterBodies.waterBodyStorage / pcr.max(1.0, annualInflow))
    
    #manual average calculation
    totalRatio = pcr.cellvalue(pcr.maptotal(CI_ratio), 1)[0]
    validRatioCells = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse(pcr.defined(CI_ratio), pcr.scalar(1), pcr.scalar(0))), 1)[0]
    
    ratioStats = {
        'min': pcr.cellvalue(pcr.mapminimum(CI_ratio), 1)[0],
        'max': pcr.cellvalue(pcr.mapmaximum(CI_ratio), 1)[0],
        'avg': totalRatio / max(validRatioCells, 1)
    }
    
    print(f"  BROWN (1943) METHOD:")
    print(f"    Formula: TE = (C/I) / (1 + C/I)")
    print(f"    C/I ratio: min={ratioStats['min']:.4f}, max={ratioStats['max']:.4f}, avg={ratioStats['avg']:.4f}")
    print(f"    Note: Generally predicts higher efficiency than Brune method")

def _debugEfficiencyDistribution(wbEfficiency):

    veryLow = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse(wbEfficiency < 0.1, pcr.scalar(1), pcr.scalar(0))), 1)[0]  # <10%
    low = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse((wbEfficiency >= 0.1) & (wbEfficiency < 0.3), pcr.scalar(1), pcr.scalar(0))), 1)[0]  # 10-30%
    medium = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse((wbEfficiency >= 0.3) & (wbEfficiency < 0.7), pcr.scalar(1), pcr.scalar(0))), 1)[0]  # 30-70%
    high = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse((wbEfficiency >= 0.7) & (wbEfficiency < 0.9), pcr.scalar(1), pcr.scalar(0))), 1)[0]  # 70-90%
    veryHigh = pcr.cellvalue(pcr.maptotal(pcr.ifthenelse(wbEfficiency >= 0.9, pcr.scalar(1), pcr.scalar(0))), 1)[0]  # >90%
    
    total = veryLow + low + medium + high + veryHigh
    if total > 0:
        print(f"  Efficiency Distribution:")
        print(f"    <10%: {veryLow:.0f} cells ({100*veryLow/total:.1f}%)")
        print(f"    10-30%: {low:.0f} cells ({100*low/total:.1f}%)")  
        print(f"    30-70%: {medium:.0f} cells ({100*medium/total:.1f}%)")
        print(f"    70-90%: {high:.0f} cells ({100*high/total:.1f}%)")
        print(f"    >90%: {veryHigh:.0f} cells ({100*veryHigh/total:.1f}%)")
