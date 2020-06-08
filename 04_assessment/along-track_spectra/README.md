## Spectral analysis of along-track altimetry: eNATL60 vs SARAL-AltiKa

### Rationale

Compare the spectrum of along-track SSH between a model output and satellite altimeter data

### Method

- Hourly model SSH extracted on a rectangular region is interpolated in space and time on the along-track trajectory read into the satellite data (lon[t], lat[t], time[t])

- Fast Fourier transform is applied to all continuous (tappered) along-track segments, with at leas *Np* points, included in the rectangular box

- Average of all these FFTs provides the spectrum

### Authors

Laurent Brodeau ([Ocean Next](https://ocean-next.fr))

### Date

08/06/2020




### Practical Steps


#### Software dependency

*Script to download satellite data from CMEMS servers and pre-process them*:
- `motuclient` (python 2.7) https://marine.copernicus.eu/faq/what-are-the-motu-and-python-requirements/
- `nco` http://nco.sourceforge.net/

*Script to interpolate ocean model SSH output onto satellite alongtrack*:
- `interp_to_ground_track.x` of [SOSIE](https://github.com/brodeau/sosie) (`make i2gt`)

  
#### Model data:
- netCDF file containing hourly SSH on the relevant region.
  - continents are masked (netCDF attribute `_FillValue`)
  - time record dimension is `UNLIMITED`
  - unit for time variable is `seconds since <DATE>`

#### Satellite data:

The script `download_saral.sh` allows the user to directly download the relevant satellite data
from the [CMEMS](https://resources.marine.copernicus.eu/?option=com_csw&task=results) data archive, provided the user has registered on the CMEMS site.

- netCDF file containing hourly SSH on the relevant region.
  - continents are masked (netCDF attribute `_FillValue`)
  - time record dimension is `UNLIMITED`
  - unit for time variable is `seconds since <DATE>`




### Results

![plot](https://github.com/ocean-next/eNATL60/blob/master/04_assessment/barotropic-tide/plots/maps_amp_phi_M2N2S2K1O1_eNATL60-FES2014_noblack0.png)
  

### External libraries needed

  - the `TIDAL_TOOLS` :  https://github.com/molines/TIDAL_TOOLS
  - [python libraries](environment.yaml)

### License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
