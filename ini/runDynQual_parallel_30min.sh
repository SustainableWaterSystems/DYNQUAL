#!/bin/bash
#SBATCH -N 1
#SBATCH -n 64
#SBATCH -p rome
#SBATCH -t 24:00:00
#SBATCH -J dynqual_v2.0_30min_parallel

# setting input files and directories ...................................
# folder containing .ini file
INI_FILE="/gpfs/home6/ejones/ini/DynQual_30min_parallel.ini"

# starting and end dates
START_YEAR="2000"
START_DATE="${START_YEAR}-01-01"

END_YEAR="2000"
END_DATE="${END_YEAR}-12-31"

# location/folder, where you will store output files of your 
OUTPUT_DIR="/scratch-shared/dynql/DynQual_v2.0_30min_GlobalParallel/"

# initial conditions
# - PS: for continuing runs (including the transition from the historical to SSP runs), please use the output files from the previous period model runs.
MAIN_INITIAL_STATE_FOLDER="/gpfs/work4/0/dynql/input_30min/ini_states/"
DATE_FOR_INITIAL_STATES="$((START_YEAR - 1))-12-31"

# number of spinup years
# - PS: For continuing runs, please set it to zero
NUMBER_OF_SPINUP_YEARS="0"

# directory of pcrglobwb model scripts
PCRGLOBWB_MODEL_SCRIPT_FOLDER="/gpfs/home6/ejones/DynQualModel/"

# PCR-GLOBWB2 and DynQual output variables' names
OUTPUT_NETCDFS=baseflow,interflowTotal,directRunoff,discharge,channelStorage,gwRecharge,storGroundwaterTotal,storGroundwater,storGroundwaterFossil,irrGrossDemand,domesticGrossDemand,livestockGrossDemand,manufactureGrossDemand,thermoelectricGrossDemand,surfaceWaterAbstraction,totalGroundwaterAbstraction,desalinationAbstraction,irrigationWaterWithdrawal,domesticWaterWithdrawal,livestockWaterWithdrawal,manufactureWaterWithdrawal,thermoelectricWaterWithdrawal,waterTemp,iceThickness,salinity,organic,dissolved_oxygen,pathogen,atenolol,naproxen,propranolol,diclofenac,carbamazepine,sulfamethoxazole,ibuprofen,amoxicillin,sedimentLoad,routedsedimentLoad,TSS,nonIrrGrossDemand,totalGrossDemand,nonFossilGroundwaterAbstraction,fossilGroundwaterAbstraction,totalAbstraction,waterBodyStorage,nonIrrWaterConsumption,nonIrrReturnFlow,domesticReturnFlow,livestockReturnFlow,manufactureReturnFlow,thermoelectricReturnFlow,irrWaterConsumption,irrReturnFlow,TDSload,Dom_TDSload,Man_TDSload,USR_TDSload,Irr_TDSload,BODload,Dom_BODload,Man_BODload,USR_BODload,intLiv_BODload,extLiv_BODload,FCload,Dom_FCload,Man_FCload,USR_FCload,intLiv_FCload,extLiv_FCload,routedTDS,TDSflux,routedDomTDS,routedManTDS,routedUSRTDS,routedIrrTDS,routedDomBOD,routedManBOD,routedUSRBOD,routedintLivBOD,routedextLivBOD,routedFC,FCflux,routedDomFC,routedManFC,routedUSRFC,routedintLivFC,routedextLivFC,ATLload,NPXload,PPLload,DFCload,CBZload,SMXload,IBPload,AMXload,routedATL,routedNPX,routedPPL,routedDFC,routedCBZ,routedSMX,routedIBP,routedAMX,ATLflux,NPXflux,PPLflux,DFCflux,CBZflux,SMXflux,IBPflux,AMXflux,sedimentConcentration,availableSedimentStock,floodplainSedimentStock,sedimentUptake,sedimentDeposition,sedimentTrapped,waterBodySedimentStorage

# running model ........................................................
unset PCRASTER_NR_WORKER_THREADS
export OPENBLAS_NUM_THREADS=1

# go to the folder that contain PCR-GLOBWB scripts
cd ${PCRGLOBWB_MODEL_SCRIPT_FOLDER}

# update directory where PCRGLOBWB2 outputs will be stored
YEAR_OUTPUT_DIR=${OUTPUT_DIR}/${START_YEAR}_${END_YEAR}

# run the model for all clones, from 1 to 53
for i in {01..53}
  do
  # set the clone code
  CLONE_CODE=${i}
  
  # run modelling framework
  python3 deterministic_runner_with_arguments.py ${INI_FILE} parallel ${CLONE_CODE} -mod ${YEAR_OUTPUT_DIR} -sd ${START_DATE} -ed ${END_DATE} -misd ${MAIN_INITIAL_STATE_FOLDER} -dfis ${DATE_FOR_INITIAL_STATES} -num_of_sp_years ${NUMBER_OF_SPINUP_YEARS} &
  done
wait

###folder for merging outputs
mkdir -p ${OUTPUT_DIR}/states
mkdir -p ${OUTPUT_DIR}/netcdf

#merge state variables
python3 merge_pcraster_maps.py ${END_DATE} ${YEAR_OUTPUT_DIR}/ ${OUTPUT_DIR}/states states 8 Global &
wait

# merge outputs
python merge_netcdf.py ${YEAR_OUTPUT_DIR} ${OUTPUT_DIR}/netcdf outDailyTotNC ${START_YEAR}-01-01 ${END_YEAR}-12-31 ${OUTPUT_NETCDFS} NETCDF4 True 53 53 all_lats True &
python merge_netcdf.py ${YEAR_OUTPUT_DIR} ${OUTPUT_DIR}/netcdf outMonthAvgNC ${START_YEAR}-01-31 ${END_YEAR}-12-31 ${OUTPUT_NETCDFS} NETCDF4 True 53 53 all_lats True &
python merge_netcdf.py ${YEAR_OUTPUT_DIR} ${OUTPUT_DIR}/netcdf outAnnuaAvgNC ${START_YEAR}-12-31 ${END_YEAR}-12-31 ${OUTPUT_NETCDFS} NETCDF4 True 53 53 all_lats True &
wait

echo "\n... End of model runs (please check your results)."