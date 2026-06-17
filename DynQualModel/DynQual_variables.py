netcdf_short_name = {}
netcdf_unit       = {}
netcdf_weekly_total_unit = {} 
netcdf_monthly_total_unit = {} 
netcdf_yearly_total_unit  = {}
netcdf_standard_name= {}
netcdf_long_name  = {}
description       = {}
comment           = {}
latex_symbol      = {}
pcr_short_name = {}     

#############################################################################################################
# DynQual 
#############################################################################################################

# Water temperature
pcrglobwb_variable_name = 'waterTemp'
netcdf_short_name[pcrglobwb_variable_name] = 'waterTemperature'
netcdf_unit[pcrglobwb_variable_name]       = 'K'
netcdf_weekly_total_unit[pcrglobwb_variable_name] = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'Temperature_of_surface_water'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Surface water temperature assuming fully mixed conditions'
latex_symbol[pcrglobwb_variable_name]      = None

# ice Thickness
pcrglobwb_variable_name = 'iceThickness'
netcdf_short_name[pcrglobwb_variable_name] = 'iceThickness'
netcdf_unit[pcrglobwb_variable_name]       = 'm'
netcdf_weekly_total_unit[pcrglobwb_variable_name] = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'Thickness_of_ice_layer'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Thickness of ice layer on channel network'
latex_symbol[pcrglobwb_variable_name]      = None

# powerplant demands (minimum) for temperature dependent technologies
pcrglobwb_variable_name = 'powerplants_fw_qmin'
netcdf_short_name[pcrglobwb_variable_name] = 'powerplants_fw_qmin'
netcdf_unit[pcrglobwb_variable_name]       = 'm3.s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name] = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'minimum_freshwater_demands_powerplants'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'powerplants minimum demands in m3 s-1 (temperature-dependent technologies)'
latex_symbol[pcrglobwb_variable_name]      = None

# powerplant demands for temperature dependent technologies
pcrglobwb_variable_name = 'powerplants_fw_q'
netcdf_short_name[pcrglobwb_variable_name] = 'powerplants_fw_q'
netcdf_unit[pcrglobwb_variable_name]       = 'm3.s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name] = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'freshwater_demands_powerplants'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'powerplants demands in m3 s-1 (temperature-dependent technologies)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted Tw loads from powerplants
pcrglobwb_variable_name = 'PowTwload'
netcdf_short_name[pcrglobwb_variable_name] = 'PowTwload'
netcdf_unit[pcrglobwb_variable_name]       = 'W'
netcdf_weekly_total_unit[pcrglobwb_variable_name] = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_temperature_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'heat dumps from thermoelectric powerplants (for temperature pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted TDS loads
pcrglobwb_variable_name = 'TDSload'
netcdf_short_name[pcrglobwb_variable_name] = 'TDSload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_TDS_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted TDS loadings (for salinity pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted Domestic TDS loads
pcrglobwb_variable_name = 'Dom_TDSload'
netcdf_short_name[pcrglobwb_variable_name] = 'DomTDSload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_DomTDS_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Domestic TDS loadings (for salinity pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted Manufacturing TDS loads
pcrglobwb_variable_name = 'Man_TDSload'
netcdf_short_name[pcrglobwb_variable_name] = 'ManTDSload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_ManTDS_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Manufacturing TDS loadings (for salinity pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted Urban Surface Runoff TDS loads
pcrglobwb_variable_name = 'USR_TDSload'
netcdf_short_name[pcrglobwb_variable_name] = 'USRTDSload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_USRTDS_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Urban Surface Runoff TDS loadings (for salinity pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# Irr RF
pcrglobwb_variable_name = 'Irr_RF'
netcdf_short_name[pcrglobwb_variable_name] = 'Irr_RF'
netcdf_unit[pcrglobwb_variable_name]       = 'm3.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'm3.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'm3.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'm3.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'irrigation_return_flow'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'irrigation return flows'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted Irr TDS loads
pcrglobwb_variable_name = 'Irr_TDSload'
netcdf_short_name[pcrglobwb_variable_name] = 'IrrTDSload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_IrrTDS_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted irrigation TDS loadings (for salinity pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted BOD loads
pcrglobwb_variable_name = 'BODload'
netcdf_short_name[pcrglobwb_variable_name] = 'BODload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_BOD_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted BOD loadings (for organic pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted Domestic BOD loads
pcrglobwb_variable_name = 'Dom_BODload'
netcdf_short_name[pcrglobwb_variable_name] = 'DomBODload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_DomBOD_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Domestic BOD loadings (for organic pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted Manufacturing BOD loads
pcrglobwb_variable_name = 'Man_BODload'
netcdf_short_name[pcrglobwb_variable_name] = 'ManBODload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_ManBOD_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Manufacturing BOD loadings (for organic pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted Urban Surface Runoff BOD loads
pcrglobwb_variable_name = 'USR_BODload'
netcdf_short_name[pcrglobwb_variable_name] = 'USRBODload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_USRBOD_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Urban Surface Runoff BOD loadings (for organic pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted intensive livestock BOD loads
pcrglobwb_variable_name = 'intLiv_BODload'
netcdf_short_name[pcrglobwb_variable_name] = 'intLivBODload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_intLivBOD_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Intensive Livestock BOD loadings (for organic pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted extensive livestock BOD loads
pcrglobwb_variable_name = 'extLiv_BODload'
netcdf_short_name[pcrglobwb_variable_name] = 'extLivBODload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_extLivBOD_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Extensive Livestock BOD loadings (for organic pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted FC loads
pcrglobwb_variable_name = 'FCload'
netcdf_short_name[pcrglobwb_variable_name] = 'FCload'
netcdf_unit[pcrglobwb_variable_name]       = 'million_cfu.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'million_cfu.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'million_cfu.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'million_cfu.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_FC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted FC loadings (for pathogen pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted Domestic FC loads
pcrglobwb_variable_name = 'Dom_FCload'
netcdf_short_name[pcrglobwb_variable_name] = 'DomFCload'
netcdf_unit[pcrglobwb_variable_name]       = 'million_cfu.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'million_cfu.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'million_cfu.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'million_cfu.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_DomFC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Domestic FC loadings (for pathogen pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted Manufacturing FC loads
pcrglobwb_variable_name = 'Man_FCload'
netcdf_short_name[pcrglobwb_variable_name] = 'ManFCload'
netcdf_unit[pcrglobwb_variable_name]       = 'million_cfu.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'million_cfu.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'million_cfu.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'million_cfu.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_ManFC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Manufacturing FC loadings (for pathogen pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted Urban Surface Runoff FC loads
pcrglobwb_variable_name = 'USR_FCload'
netcdf_short_name[pcrglobwb_variable_name] = 'USRFCload'
netcdf_unit[pcrglobwb_variable_name]       = 'million_cfu.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'million_cfu.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'million_cfu.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'million_cfu.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_USRFC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Urban Surface Runoff FC loadings (for pathogen pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted Intensive Livestock FC loads
pcrglobwb_variable_name = 'intLiv_FCload'
netcdf_short_name[pcrglobwb_variable_name] = 'intLivFCload'
netcdf_unit[pcrglobwb_variable_name]       = 'million_cfu.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'million_cfu.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'million_cfu.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'million_cfu.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_intLivFC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Intensive Livestock FC loadings (for pathogen pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted extensive Livestock FC loads
pcrglobwb_variable_name = 'extLiv_FCload'
netcdf_short_name[pcrglobwb_variable_name] = 'extLivFCload'
netcdf_unit[pcrglobwb_variable_name]       = 'million_cfu.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'million_cfu.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'million_cfu.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'million_cfu.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_extLivFC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted Extensive Livestock FC loadings (for pathogen pollution)'
latex_symbol[pcrglobwb_variable_name]      = None

# routed TDS loads
pcrglobwb_variable_name = 'routedTDS'
netcdf_short_name[pcrglobwb_variable_name] = 'routedTDS'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_TDS_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'TDS loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# in stream TDS loadings (flux)
pcrglobwb_variable_name = 'TDSflux'
netcdf_short_name[pcrglobwb_variable_name] = 'TDSflux'
netcdf_unit[pcrglobwb_variable_name]       = 'g s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'instream_TDS_flux'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'TDS loadings routed through surface water network per unit time'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Domestic TDS loads
pcrglobwb_variable_name = 'routedDomTDS'
netcdf_short_name[pcrglobwb_variable_name] = 'routedDomTDS'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_DomTDS_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Domestic TDS loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Manufacturing TDS loads
pcrglobwb_variable_name = 'routedManTDS'
netcdf_short_name[pcrglobwb_variable_name] = 'routedManTDS'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_ManTDS_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Manufacturing TDS loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Urban Surface Runoff TDS loads
pcrglobwb_variable_name = 'routedUSRTDS'
netcdf_short_name[pcrglobwb_variable_name] = 'routedUSRTDS'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_USRTDS_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Urban Surface Runoff TDS loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Irrigation TDS loads
pcrglobwb_variable_name = 'routedIrrTDS'
netcdf_short_name[pcrglobwb_variable_name] = 'routedIrrTDS'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_IrrTDS_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Irrigation TDS loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed BOD loads
pcrglobwb_variable_name = 'routedBOD'
netcdf_short_name[pcrglobwb_variable_name] = 'routedBOD'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_BOD_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'BOD loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# in stream BOD loadings (flux)
pcrglobwb_variable_name = 'BODflux'
netcdf_short_name[pcrglobwb_variable_name] = 'BODflux'
netcdf_unit[pcrglobwb_variable_name]       = 'g s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'instream_BOD_flux'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'BOD loadings routed through surface water network per unit time'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Domestic BOD loads
pcrglobwb_variable_name = 'routedDomBOD'
netcdf_short_name[pcrglobwb_variable_name] = 'routedDomBOD'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_DomBOD_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Domestic BOD loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Manufacturing BOD loads
pcrglobwb_variable_name = 'routedManBOD'
netcdf_short_name[pcrglobwb_variable_name] = 'routedManBOD'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_ManBOD_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Manufacturing BOD loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Urban Surface Runoff BOD loads
pcrglobwb_variable_name = 'routedUSRBOD'
netcdf_short_name[pcrglobwb_variable_name] = 'routedUSRBOD'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_USRBOD_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Urban Surface Runoff BOD loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Intensive Livestock BOD loads
pcrglobwb_variable_name = 'routedintLivBOD'
netcdf_short_name[pcrglobwb_variable_name] = 'routedintLivBOD'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_intLivBOD_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Intensive Livestock BOD loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Extensive Livestock BOD loads
pcrglobwb_variable_name = 'routedextLivBOD'
netcdf_short_name[pcrglobwb_variable_name] = 'routedextLivBOD'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_extLivBOD_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Extensive Livestock BOD loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed FC loads
pcrglobwb_variable_name = 'routedFC'
netcdf_short_name[pcrglobwb_variable_name] = 'routedFC'
netcdf_unit[pcrglobwb_variable_name]       = 'million_cfu'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_FC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'FC loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# in stream TDS loadings (flux)
pcrglobwb_variable_name = 'FCflux'
netcdf_short_name[pcrglobwb_variable_name] = 'FCflux'
netcdf_unit[pcrglobwb_variable_name]       = 'million cfu s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'instream_TDS_flux'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'FC loadings routed through surface water network per unit time'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Domestic FC loads
pcrglobwb_variable_name = 'routedDomFC'
netcdf_short_name[pcrglobwb_variable_name] = 'routedDomFC'
netcdf_unit[pcrglobwb_variable_name]       = 'million_cfu'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_DomFC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Domestic FC loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Manufacturing FC loads
pcrglobwb_variable_name = 'routedManFC'
netcdf_short_name[pcrglobwb_variable_name] = 'routedManFC'
netcdf_unit[pcrglobwb_variable_name]       = 'million_cfu'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_ManFC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Manufacturing FC loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Urban Surface Runoff FC loads
pcrglobwb_variable_name = 'routedUSRFC'
netcdf_short_name[pcrglobwb_variable_name] = 'routedUSRFC'
netcdf_unit[pcrglobwb_variable_name]       = 'million_cfu'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_USRFC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Urban Surface Runoff FC loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Intensive Livestock FC loads
pcrglobwb_variable_name = 'routedintLivFC'
netcdf_short_name[pcrglobwb_variable_name] = 'routedintLivFC'
netcdf_unit[pcrglobwb_variable_name]       = 'million_cfu'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_intLivFC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Intensive Livestock FC loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routed Extensive Livestock FC loads
pcrglobwb_variable_name = 'routedextLivFC'
netcdf_short_name[pcrglobwb_variable_name] = 'routedextLivFC'
netcdf_unit[pcrglobwb_variable_name]       = 'million_cfu'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_extLivFC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Extensive Livestock FC loadings routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# Salinity pollution (concentration in TDS mg.l)
pcrglobwb_variable_name = 'salinity'
netcdf_short_name[pcrglobwb_variable_name] = 'salinity'
netcdf_unit[pcrglobwb_variable_name]       = 'mg.l'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'salinity_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream salinity (TDS) concentration in mg.l'
latex_symbol[pcrglobwb_variable_name]      = None

# Organic pollution (concentration in BOD mg.l)
pcrglobwb_variable_name = 'organic'
netcdf_short_name[pcrglobwb_variable_name] = 'organic'
netcdf_unit[pcrglobwb_variable_name]       = 'mg.l'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'organic_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream organic (BOD) concentration in mg.l'
latex_symbol[pcrglobwb_variable_name]      = None

# Dissolved oxygen (concentration in DO mg.l)
pcrglobwb_variable_name = 'dissolved_oxygen'
netcdf_short_name[pcrglobwb_variable_name] = 'dissolved_oxygen'
netcdf_unit[pcrglobwb_variable_name]       = 'mg.l'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'dissolved_oxygen_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream DO concentration in mg.l'
latex_symbol[pcrglobwb_variable_name]      = None

# Pathogen pollution (concentration in FC cfu.100ml)
pcrglobwb_variable_name = 'pathogen'
netcdf_short_name[pcrglobwb_variable_name] = 'pathogen'
netcdf_unit[pcrglobwb_variable_name]       = 'cfu.100ml'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'pathogen_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream pathogen (FC) concentration in cfu.100ml'
latex_symbol[pcrglobwb_variable_name]      = None

###---------------------------------------###
###Pharmaceuticals
###---------------------------------------###

# unrouted ATL loads
pcrglobwb_variable_name = 'ATLload'
netcdf_short_name[pcrglobwb_variable_name] = 'ATLload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_ATL_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted ATL loadings (for atenolol concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted NPX loads
pcrglobwb_variable_name = 'NPXload'
netcdf_short_name[pcrglobwb_variable_name] = 'NPXload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_NPX_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted NPX loadings (for naproxen concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted PPL loads
pcrglobwb_variable_name = 'PPLload'
netcdf_short_name[pcrglobwb_variable_name] = 'PPLload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_PPL_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted PPL loadings (for propranolol concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted DFC loads
pcrglobwb_variable_name = 'DFCload'
netcdf_short_name[pcrglobwb_variable_name] = 'DFCload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_DFC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted DFC loadings (for diclofenac concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted CBZ loads
pcrglobwb_variable_name = 'CBZload'
netcdf_short_name[pcrglobwb_variable_name] = 'CBZload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_CBZ_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted CBZ loadings (for carbamazepine concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted SMX loads
pcrglobwb_variable_name = 'SMXload'
netcdf_short_name[pcrglobwb_variable_name] = 'SMXload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_SMX_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted SMX loadings (for sulfamethoxazole concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted IBP loads
pcrglobwb_variable_name = 'IBPload'
netcdf_short_name[pcrglobwb_variable_name] = 'IBPload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_IBP_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted IBP loadings (for ibuprofen concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# unrouted AMX loads
pcrglobwb_variable_name = 'AMXload'
netcdf_short_name[pcrglobwb_variable_name] = 'AMXload'
netcdf_unit[pcrglobwb_variable_name]       = 'g.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'g.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'g.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'g.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'unrouted_AMX_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'unrouted AMX loadings (for amoxicillin concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# routed ATL loads
pcrglobwb_variable_name = 'routedATL'
netcdf_short_name[pcrglobwb_variable_name] = 'routedATL'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_ATL_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'ATL loadings routed through surface water network (for atenolol concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# routed NPX loads
pcrglobwb_variable_name = 'routedNPX'
netcdf_short_name[pcrglobwb_variable_name] = 'routedNPX'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_NPX_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'NPX loadings routed through surface water network (for naproxen concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# routed PPL loads
pcrglobwb_variable_name = 'routedPPL'
netcdf_short_name[pcrglobwb_variable_name] = 'routedPPL'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_PPL_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'PPL loadings routed through surface water network (for propranolol concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# routed DFC loads
pcrglobwb_variable_name = 'routedDFC'
netcdf_short_name[pcrglobwb_variable_name] = 'routedDFC'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_DFC_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'DFC loadings routed through surface water network (for diclofenac concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# routed CBZ loads
pcrglobwb_variable_name = 'routedCBZ'
netcdf_short_name[pcrglobwb_variable_name] = 'routedCBZ'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_CBZ_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'CBZ loadings routed through surface water network (for carbamazepine concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# routed SMX loads
pcrglobwb_variable_name = 'routedSMX'
netcdf_short_name[pcrglobwb_variable_name] = 'routedSMX'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_SMX_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'SMX loadings routed through surface water network (for sulfamethoxazole concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# routed IBP loads
pcrglobwb_variable_name = 'routedIBP'
netcdf_short_name[pcrglobwb_variable_name] = 'routedIBP'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_IBP_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'IBP loadings routed through surface water network (for ibuprofen concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# routed AMX loads
pcrglobwb_variable_name = 'routedAMX'
netcdf_short_name[pcrglobwb_variable_name] = 'routedAMX'
netcdf_unit[pcrglobwb_variable_name]       = 'g'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'routed_AMX_loadings'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'AMX loadings routed through surface water network (for amoxicillin concentrations)'
latex_symbol[pcrglobwb_variable_name]      = None

# in stream ATL loadings (flux)
pcrglobwb_variable_name = 'ATLflux'
netcdf_short_name[pcrglobwb_variable_name] = 'ATLflux'
netcdf_unit[pcrglobwb_variable_name]       = 'g s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'instream_ATL_flux'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'ATL loadings routed through surface water network per unit time'
latex_symbol[pcrglobwb_variable_name]      = None

# in stream NPX loadings (flux)
pcrglobwb_variable_name = 'NPXflux'
netcdf_short_name[pcrglobwb_variable_name] = 'NPXflux'
netcdf_unit[pcrglobwb_variable_name]       = 'g s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'instream_NPX_flux'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'NPX loadings routed through surface water network per unit time'
latex_symbol[pcrglobwb_variable_name]      = None

# in stream PPL loadings (flux)
pcrglobwb_variable_name = 'PPLflux'
netcdf_short_name[pcrglobwb_variable_name] = 'PPLflux'
netcdf_unit[pcrglobwb_variable_name]       = 'g s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'instream_PPL_flux'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'PPL loadings routed through surface water network per unit time'
latex_symbol[pcrglobwb_variable_name]      = None

# in stream DFC loadings (flux)
pcrglobwb_variable_name = 'DFCflux'
netcdf_short_name[pcrglobwb_variable_name] = 'DFCflux'
netcdf_unit[pcrglobwb_variable_name]       = 'g s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'instream_DFC_flux'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'DFC loadings routed through surface water network per unit time'
latex_symbol[pcrglobwb_variable_name]      = None

# in stream CBZ loadings (flux)
pcrglobwb_variable_name = 'CBZflux'
netcdf_short_name[pcrglobwb_variable_name] = 'CBZflux'
netcdf_unit[pcrglobwb_variable_name]       = 'g s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'instream_CBZ_flux'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'CBZ loadings routed through surface water network per unit time'
latex_symbol[pcrglobwb_variable_name]      = None

# in stream SMX loadings (flux)
pcrglobwb_variable_name = 'SMXflux'
netcdf_short_name[pcrglobwb_variable_name] = 'SMXflux'
netcdf_unit[pcrglobwb_variable_name]       = 'g s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'instream_SMX_flux'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'SMX loadings routed through surface water network per unit time'
latex_symbol[pcrglobwb_variable_name]      = None

# in stream IBP loadings (flux)
pcrglobwb_variable_name = 'IBPflux'
netcdf_short_name[pcrglobwb_variable_name] = 'IBPflux'
netcdf_unit[pcrglobwb_variable_name]       = 'g s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'instream_IBP_flux'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'IBP loadings routed through surface water network per unit time'
latex_symbol[pcrglobwb_variable_name]      = None

# in stream AMX loadings (flux)
pcrglobwb_variable_name = 'AMXflux'
netcdf_short_name[pcrglobwb_variable_name] = 'AMXflux'
netcdf_unit[pcrglobwb_variable_name]       = 'g s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'instream_AMX_flux'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'AMX loadings routed through surface water network per unit time'
latex_symbol[pcrglobwb_variable_name]      = None

# Atenolol (concentration in ATL ug.l)
pcrglobwb_variable_name = 'atenolol'
netcdf_short_name[pcrglobwb_variable_name] = 'atenolol'
netcdf_unit[pcrglobwb_variable_name]       = 'ug.l'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'atenolol_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream atenolol (ATL) concentration in ug.l'
latex_symbol[pcrglobwb_variable_name]      = None

# Naproxen (concentration in NPX ug.l)
pcrglobwb_variable_name = 'naproxen'
netcdf_short_name[pcrglobwb_variable_name] = 'naproxen'
netcdf_unit[pcrglobwb_variable_name]       = 'ug.l'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'naproxen_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream naproxen (NPX) concentration in ug.l'
latex_symbol[pcrglobwb_variable_name]      = None

# Propranolol (concentration in PPL ug.l)
pcrglobwb_variable_name = 'propranolol'
netcdf_short_name[pcrglobwb_variable_name] = 'propranolol'
netcdf_unit[pcrglobwb_variable_name]       = 'ug.l'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'propranolol_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream propranolol (PPL) concentration in ug.l'
latex_symbol[pcrglobwb_variable_name]      = None

# Diclofenac (concentration in DFC ug.l)
pcrglobwb_variable_name = 'diclofenac'
netcdf_short_name[pcrglobwb_variable_name] = 'diclofenac'
netcdf_unit[pcrglobwb_variable_name]       = 'ug.l'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'diclofenac_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream diclofenac (DFC) concentration in ug.l'
latex_symbol[pcrglobwb_variable_name]      = None

# Carbamazepine (concentration in CBZ ug.l)
pcrglobwb_variable_name = 'carbamazepine'
netcdf_short_name[pcrglobwb_variable_name] = 'carbamazepine'
netcdf_unit[pcrglobwb_variable_name]       = 'ug.l'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'carbamazepine_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream carbamazepine (CBZ) concentration in ug.l'
latex_symbol[pcrglobwb_variable_name]      = None

# Sulfamethoxazole (concentration in SMX ug.l)
pcrglobwb_variable_name = 'sulfamethoxazole'
netcdf_short_name[pcrglobwb_variable_name] = 'sulfamethoxazole'
netcdf_unit[pcrglobwb_variable_name]       = 'ug.l'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'sulfamethoxazole_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream sulfamethoxazole (SMX) concentration in ug.l'
latex_symbol[pcrglobwb_variable_name]      = None

# Ibuprofen (concentration in IBP ug.l)
pcrglobwb_variable_name = 'ibuprofen'
netcdf_short_name[pcrglobwb_variable_name] = 'ibuprofen'
netcdf_unit[pcrglobwb_variable_name]       = 'ug.l'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'ibuprofen_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream ibuprofen (IBP) concentration in ug.l'
latex_symbol[pcrglobwb_variable_name]      = None

# Amoxicillin (concentration in AMX ug.l)
pcrglobwb_variable_name = 'amoxicillin'
netcdf_short_name[pcrglobwb_variable_name] = 'amoxicillin'
netcdf_unit[pcrglobwb_variable_name]       = 'ug.l'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'amoxicillin_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream amoxicillin (AMX) concentration in ug.l'
latex_symbol[pcrglobwb_variable_name]      = None

###---------------------------------------###
###TSS (Total suspended sediments) variables
###---------------------------------------###

# sedimentLoad (sediment delivered to surface water network)
pcrglobwb_variable_name = 'sedimentLoad'
netcdf_short_name[pcrglobwb_variable_name] = 'sedimentLoad'
netcdf_unit[pcrglobwb_variable_name]       = 'kg.day'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'sediment_delivery_to_water'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Total suspended sediment load delivered to surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# routedsedimentLoad (routed sediment in water)
pcrglobwb_variable_name = 'routedsedimentLoad'
netcdf_short_name[pcrglobwb_variable_name] = 'routedsedimentLoad'
netcdf_unit[pcrglobwb_variable_name]       = 'kg'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'sediment_load_in_water'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Total suspended sediment load routed through surface water network'
latex_symbol[pcrglobwb_variable_name]      = None

# sedimentConcentration (TSS concentration in kg/m3)
pcrglobwb_variable_name = 'sedimentConcentration'
netcdf_short_name[pcrglobwb_variable_name] = 'sedimentConcentration'
netcdf_unit[pcrglobwb_variable_name]       = 'kg.m-3'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'total_suspended_sediment_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream TSS concentration in kg/m3'
latex_symbol[pcrglobwb_variable_name]      = None

# TSS (sediment concentration in mg/L)
pcrglobwb_variable_name = 'TSS'
netcdf_short_name[pcrglobwb_variable_name] = 'TSS'
netcdf_unit[pcrglobwb_variable_name]       = 'mg.l-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'total_suspended_sediment_concentration'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'In-stream TSS concentration in mg/L'
latex_symbol[pcrglobwb_variable_name]      = None

# availableSedimentStock (riverbed sediment available for entrainment)
pcrglobwb_variable_name = 'availableSedimentStock'
netcdf_short_name[pcrglobwb_variable_name] = 'availableSedimentStock'
netcdf_unit[pcrglobwb_variable_name]       = 'kg'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'available_riverbed_sediment_stock'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Riverbed sediment stock available for entrainment'
latex_symbol[pcrglobwb_variable_name]      = None

# floodplainSedimentStock (floodplain sediment storage)
pcrglobwb_variable_name = 'floodplainSedimentStock'
netcdf_short_name[pcrglobwb_variable_name] = 'floodplainSedimentStock'
netcdf_unit[pcrglobwb_variable_name]       = 'kg'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'floodplain_sediment_stock'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Sediment deposited on floodplains'
latex_symbol[pcrglobwb_variable_name]      = None

# transportCapacity (maximum transportable TSS)
pcrglobwb_variable_name = 'transportCapacity'
netcdf_short_name[pcrglobwb_variable_name] = 'transportCapacity'
netcdf_unit[pcrglobwb_variable_name]       = 'kg.m-3'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'sediment_transport_capacity'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Maximum sediment concentration that can be transported (Govers 1990)'
latex_symbol[pcrglobwb_variable_name]      = None

# flow velocity
pcrglobwb_variable_name = 'flowVelocity'
netcdf_short_name[pcrglobwb_variable_name] = 'flowVelocity'
netcdf_unit[pcrglobwb_variable_name]       = 'm.day'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'flow velocity'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'flow velocity'
latex_symbol[pcrglobwb_variable_name]      = None

# unitStreamPower (flow erosive power)
pcrglobwb_variable_name = 'unitStreamPower'
netcdf_short_name[pcrglobwb_variable_name] = 'unitStreamPower'
netcdf_unit[pcrglobwb_variable_name]       = 'm.s-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'unit_stream_power'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Unit stream power (velocity * gradient) for sediment transport'
latex_symbol[pcrglobwb_variable_name]      = None

# sedimentUptake (entrainment rate)
pcrglobwb_variable_name = 'sedimentUptake'
netcdf_short_name[pcrglobwb_variable_name] = 'sedimentUptake'
netcdf_unit[pcrglobwb_variable_name]       = 'kg.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'kg.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'kg.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'kg.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'sediment_entrainment_rate'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Rate of sediment entrainment from riverbed'
latex_symbol[pcrglobwb_variable_name]      = None

# sedimentDeposition (settling/deposition rate)
pcrglobwb_variable_name = 'sedimentDeposition'
netcdf_short_name[pcrglobwb_variable_name] = 'sedimentDeposition'
netcdf_unit[pcrglobwb_variable_name]       = 'kg.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'kg.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'kg.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'kg.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'sediment_deposition_rate'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Rate of sediment deposition (negative values indicate settling)'
latex_symbol[pcrglobwb_variable_name]      = None

# Sediment trapping efficiency (fraction)
pcrglobwb_variable_name = 'sedimentTrappingEfficiency'
netcdf_short_name[pcrglobwb_variable_name] = 'sedimentTrappingEfficiency'
netcdf_unit[pcrglobwb_variable_name]       = '1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'sediment_trapping_efficiency'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Fraction of sediment trapped in water bodies (0-1)'
latex_symbol[pcrglobwb_variable_name]      = None

# Sediment trapped daily (kg/day)
pcrglobwb_variable_name = 'sedimentTrapped'
netcdf_short_name[pcrglobwb_variable_name] = 'sedimentTrapped'
netcdf_unit[pcrglobwb_variable_name]       = 'kg.day-1'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = 'kg.week-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'kg.month-1'
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'kg.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'sediment_trapped'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Rate of sediment trapping in water bodies'
latex_symbol[pcrglobwb_variable_name]      = None

# Water body sediment storage (kg)
pcrglobwb_variable_name = 'waterBodySedimentStorage'
netcdf_short_name[pcrglobwb_variable_name] = 'waterBodySedimentStorage'
netcdf_unit[pcrglobwb_variable_name]       = 'kg'
netcdf_weekly_total_unit[pcrglobwb_variable_name]  = None
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'water_body_sediment_storage'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Cumulative sediment stored in water bodies'
latex_symbol[pcrglobwb_variable_name]      = None

#~ # remove/clear pcrglobwb_variable_name 
#~ pcrglobwb_variable_name = None
#~ del pcrglobwb_variable_name
