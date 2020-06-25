## eNATL60 and AVISO mean and standart deviation of sea surface height

### Motivation

A classical comparison of ssh with AVISO data

### Authors

Aurélie Albert ([Ocean Next](https://ocean-next.fr)), Julien LeSommer ([MEOM-IGE](https://github.com/meom-group.io))

### Date

25/11/2019

### Practical Steps

  - Hourly eNATL60 SSH is averaged at daily frequency to match AVISO resolution, see block 6 of the [notebook](https://github.com/ocean-next/eNATL60/blob/master/04_assessment/mesoscale-variability/notebooks/2019-11-25-AA-std-mean-ssh-eNATL60-1h-to-1d.ipynb)
  - Temporal mean and standart deviation are computed for both datasets ([eNATL60](https://github.com/ocean-next/eNATL60/blob/master/04_assessment/mesoscale-variability/notebooks/2019-11-25-AA-std-mean-ssh-eNATL60-1h-to-1d.ipynb) and [AVISO](https://github.com/ocean-next/eNATL60/blob/master/04_assessment/mesoscale-variability/notebooks/2019-11-25-AA-std-mean-ssh-AVISO.ipynb))
  - Results are stored in netcdf files for future reuse
  - Maps of standart deviation superimposed with mean as contours are produced [here](https://github.com/ocean-next/eNATL60/blob/master/04_assessment/mesoscale-variability/notebooks/2019-11-25-AA-plots-std-mean-ssh-AVISO-eNATL60-mac.ipynb) 
  
### Results

![plot](https://github.com/ocean-next/eNATL60/blob/master/04_assessment/mesoscale-variability/plots/std-mean-SSH-AVISO-eNATL60-BLBT02.png)<br>
*Figure 1: Standard deviation of SSH over the 30/06/2009 - 30/10/2010 period, contours = mean SSH.*



The computation of temporal mean and standart deviation of eNATL60 hourly ssh converted to daily frequency for the whole domain requires 30 minutes of nearly 200 high-memory cores on the CINES OCCIGEN machine.

Click on [![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/ocean-next/demo-compare-ssh-eNATL60-AVISO/master) for an interactive demonstration of the computation on the Gulf Stream area.
  

### External librairies needed
  
  - [python librairies](environment.yaml)

### License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
