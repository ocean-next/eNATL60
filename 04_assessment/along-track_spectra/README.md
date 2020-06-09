# Spectral analysis of along-track altimetry: eNATL60 vs SARAL-AltiKa

## Rationale

Compare the spectrum of along-track SSH between a model output and satellite altimeter data

## Method

- Hourly model SSH extracted on a rectangular region is interpolated in space and time on the along-track trajectory read into the satellite data (lon[t], lat[t], time[t])

- Fast Fourier transform is applied to all continuous (tappered) along-track segments, with at leas *Np* points, included in the rectangular box

- Average of all these FFTs provides the spectrum

## Authors

Laurent Brodeau ([Ocean Next](https://ocean-next.fr))

## Date

08/06/2020




## Technical aspects

###  Model data:

A netCDF file containing hourly (preferably) SSH on the rectangular region and the time window of your choice.

**Requirements:**
- field of SSH is time-dependent and two-dimensional in space (ex: `SSH(x,y,t)`)
- spatial coordinates (*i.e.* arrays of longitude and latitude) are NOT time-dependent and must be included in the file (ex: `lon(x,y)` & `lat(x,y)`)
- for the field of SSH, land points are flagged by means of the`_FillValue` netCDF attribute 
- time/record dimension `t` (or any other name) is `UNLIMITED` !
- time/calendar variable `time` (or any other name) must be included in the file  (ex: `time(t)`)
- unit for time variable `time` must be of the kind: `seconds since <DATE>` (ex: `seconds since 1950-01-01 00:00:00`)
- time/calendar variable must be consistent with the time window of the satellite data you plan to use!

### Satellite data:

The script `download_saral.sh` allows the user to directly download the relevant satellite data
from the [CMEMS](https://resources.marine.copernicus.eu/?option=com_csw&task=results) data archive, provided the user has previously registered on the CMEMS website.

Technically, this script downloads the netCDF data hosted by CMEMS for the requested period and convert it to a usable netCDF files:

- make the record dimension 'UNLIMITED' as it should always be
- unpack fields
- generate one single netCDF file for the whole period
- ensure efficient netCDF-4 deflation

**Software dependency:**
- `python 2.7`
- `motuclient` https://marine.copernicus.eu/faq/what-are-the-motu-and-python-requirements/
- `nco` http://nco.sourceforge.net/



### Software dependency

*Script to interpolate ocean model SSH output onto satellite track*:
- `interp_to_ground_track.x` of [SOSIE](https://github.com/brodeau/sosie) (`make i2gt`)

  





## Results

![plot](https://github.com/ocean-next/eNATL60/blob/master/04_assessment/barotropic-tide/plots/maps_amp_phi_M2N2S2K1O1_eNATL60-FES2014_noblack0.png)


## External libraries needed

  - the `TIDAL_TOOLS` :  https://github.com/molines/TIDAL_TOOLS
  - [python libraries](environment.yaml)

## License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
