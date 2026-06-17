#!/bin/bash
#SBATCH -t 59:00
#SBATCH -p rome
#SBATCH -N 1
#SBATCH -n 64

cd /gpfs/home6/ejones/

python DynQualModel/deterministic_runner.py ini/DynQual_30min.ini & #single landmask/global, 30min
#python DynQualModel/deterministic_runner.py ini/DynQual_05min.ini & #single landmask, 5min

wait

