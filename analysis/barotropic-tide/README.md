## Requisite
The harmonic analysis of the eNATL60 outputs needs :

  - the `TIDAL_TOOLS` :  https://github.com/molines/TIDAL_TOOLS

## Steps
  - the harmonic analysis is performed by submitting a job to visu (large memory needed) : script [make_tidal_amp_phase.ksh](https://github.com/ocean-next/eNATL60/tree/master/analysis/barotropic-tide/make_tidal_amp_phase.ksh) and providing the [namelist](https://github.com/AurelieAlbert/eNATL60-plots-paper/blob/master/amp-phase-tides-FES/namelist_tideharm) to the TIDAL_TOOLS
  - the first plots are produced in the notebook : [2020-03-17-AA-maps-amp-phase-M2-eNATL60-FES2014.ipynb](https://github.com/AurelieAlbert/eNATL60-plots-paper/blob/master/amp-phase-tides-FES/2020-03-17-AA-maps-amp-phase-M2-eNATL60-FES2014.ipynb), the reference plot is [here](https://github.com/ocean-next/eNATL60/tree/master/analysis/barotropic-tide/maps_amp_phi_M2N2S2K1O1_eNATL60-FES2014.png)
  - option is to not have a black line for the phase=0 : [here](https://github.com/ocean-next/eNATL60/tree/master/analysis/barotropic-tide/maps_amp_phi_M2N2S2K1O1_eNATL60-FES2014_noblack0.png)
  - option is to change the colormap, test with inferno [here](https://github.com/ocean-next/eNATL60/tree/master/analysis/barotropic-tide/maps_amp_phi_M2_eNATL60_noblack0inferno.png) and magma [here](https://github.com/ocean-next/eNATL60/tree/master/analysis/barotropic-tide/maps_amp_phi_M2_eNATL60_noblack0magma.png) and cmocean-amp [here]()
