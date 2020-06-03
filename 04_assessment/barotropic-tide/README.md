## eNATL60 and FES2014 harmonic analysis of sea surface height

### Motivation

We want to check if the tides modelled with NEMO are adequate regarding FES2014

### Authors

Aurélie Albert ([Ocean Next](https://ocean-next.fr)), Jean-Marc Molines ([MEOM-IGE](https://github.com/meom-group.io)), Laurent Brodeau ([Ocean Next](https://ocean-next.fr))

### Date

17/03/2020

### Practical Steps

  - The harmonic analysis is computed for eNATL60 ssh from 01/07/2009 to 30/06/2010 using [TIDAL_TOOLS](https://github.com/molines/TIDAL_TOOLS), script [here](https://github.com/ocean-next/eNATL60/tree/master/04_assessment/barotropic-tide/scripts/make_tidal_amp_phase.ksh)
  - Maps of amplitude with phase as contours are produced for M2, S2, N2, O1 and K1 frequencies [here](https://github.com/ocean-next/eNATL60/blob/master/04_assessment/barotropic-tide/notebooks/2020-03-17-AA-maps-amp-phase-M2-eNATL60-FES2014.ipynb)
  
### Results

![plot](https://github.com/ocean-next/eNATL60/blob/master/04_assessment/barotropic-tide/plots/maps_amp_phi_M2N2S2K1O1_eNATL60-FES2014_noblack0.png)
  

### External librairies needed

  - the `TIDAL_TOOLS` :  https://github.com/molines/TIDAL_TOOLS
  - [python librairies](environment.yaml)

### License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
