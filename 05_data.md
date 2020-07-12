# Access to eNATL60 data


 - The entire 3D outputs of both tidal and non-tidal simulations are permanently stored at CINES supercomputing center in Montpellier, France (https://www.cines.fr/). The 3D variables are stored in netcdf4 daily files, 1 file per variable : gridT, gridS, gridU, gridV, gridW, gridZ, the 2D variables are regrouped under gridT-2D, gridU-2D,gridV-2D, flxT and icemod. Access to this dataset is possible through GENCI for registered participants to [eDARI](https://www.edari.fr) projects. 
 
 - Surface fields in zarr format (ssh, ssu, ssv for both simulations) and SWOT virtual observations based on NEMO-eNATL60 are available to the french SWOT Science Team on HAL cluster at [CNES](https://cnes.fr).  

 - Surface fields in zarr format (ssh, ssu, ssv for both simulations) are also available on the cloud on [pangeo catalogue] (https://catalog.pangeo.io/browse/master/ocean/MEOM_NEMO/);  registered members of pangeo can access the data for cloud-based analyses on https://ocean.pangeo.io/

 - Some geographic or surface extractions are also available on the MEOM-IGE group cluster ige-meom-cal1 and can be downloaded through opendap upon request. The available regional extractions include: GULFSTREAM, ACORES, OSMOSIS, WESTMED, LABRADOR, GIBRALTAR
 
 - You can ask for your personnalised dataset at aurelie.albert(at)ocean-next.fr
 

## License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
