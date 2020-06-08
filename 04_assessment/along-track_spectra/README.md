## Spectral analysis of along-track altimetry: eNATL60 vs SARAL-AltiKa

### Rationale

We want to check if the tides modelled with NEMO are adequate regarding FES2014

### Authors

Laurent Brodeau ([Ocean Next](https://ocean-next.fr))

### Date

08/06/2020




### Practical Steps


#### Software

  - [SOSIE](https://github.com/brodeau/sosie), script
  
#### Data

Model data:
- netCDF file containing hourly SSH on the relevant region.
  - continents are masked (netCDF attribute `_FillValue`)
  - time record dimension is `UNLIMITED`
  - unit for time variable is `seconds since <DATE>`

Satelite data:
- netCDF file containing hourly SSH on the relevant region.
  - continents are masked (netCDF attribute `_FillValue`)
  - time record dimension is `UNLIMITED`
  - ubit for time variable is `seconds since <DATE>`




### Results

![plot](https://github.com/ocean-next/eNATL60/blob/master/04_assessment/barotropic-tide/plots/maps_amp_phi_M2N2S2K1O1_eNATL60-FES2014_noblack0.png)
  

### External librairies needed

  - the `TIDAL_TOOLS` :  https://github.com/molines/TIDAL_TOOLS
  - [python librairies](environment.yaml)

### License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
