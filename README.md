This GitHub branch contains the python scripts associated with (i) the development of the hybrid DynQual_Random Forest model; and (ii) the analyses of the dissolved oxygen output from the hybrid model. The scripts can be followed in chronological order: 

Folder “DynQualModel” contains the process-based DynQual model (Jones et al. 2023), including the Streeter-Phelps equation to simulate dissolved oxygen concentration.

Folder “Historic_analyses.zip” 
- Script_1.py: Merging the process-based simulated dissolved oxygen with monitoring data from 7 water quality databases. Note: the data processing is consistent with the procedure from Graham et al. (https://doi.org/10.1016/j.jhydrol.2023.130590) and the scripts can be found at (https://doi.org/10.5281/zenodo.7558906).
- Script_2.py: Training the Random Forest component of the hybrid model. The random forest that was used throughout the analyses is provided as a .joblib file in the folder “Random_Forest.zip” at https://doi.org/10.5281/zenodo.13329996.
- Script_3a.py to Script_3e.py: Running the hybrid DynQual_Random Forest model globally over the period 1980-2019.
- Script_4_pt1.py to Script_4_pt5.py: Conversion to NetCDF.
- Script_S_Historic.py to Script_Z_Historic.py: These scripts are associated with the analysis of the study over the period 1980-2019 using the hybrid model output.

Folder “Future_analyses.zip” 
- .sh and .ini files are the job scripts for running the process-based DynQual model with 5 Global Climate Models (GCMs) over the period 2005-2100.
- Script_3a_snell.py to Script_3e_snell.py are the scripts that were used to run the hybrid DynQual_Random Forest model for 5 GCMs over the period 2005-2100.
- Script_4_snell.py to Script_8_snell.py: Conversion to NetCDF.
- Script_R1.py to Script_Z1.py: These scripts are for the analysis of this study over the period 2020-2100 using the hybrid model output.

References
Jones, E. R., Bierkens, M. F. P., Wanders, N., Sutanudjaja, E. H., van Beek, L. P. H., and van Vliet, M. T. H.: DynQual v1.0: a high-resolution global surface water quality model, Geosci. Model Dev., 16, 4481–4500, https://doi.org/10.5194/gmd-16-4481-2023, 2023.
Graham, D.J., Bierkens, M.F.P., van Vliet, M.T.H. Impacts of droughts and heatwaves on river water quality worldwide. Journal of Hydrology 629, 130590, https://doi.org/10.1016/j.jhydrol.2023.130590, 2024
