## eNATL60 and AVISO mean and standart deviation of sea surface height

### Motivation

### Authors

Aurélie Albert ([Ocean Next](https://ocean-next.fr)), Julien LeSommer ([MEOM-IGE](https://github.com/meom-group.io))

### Date

25/11/2019

### Detailed description

### Practical Steps

  - Hourly eNATL60 SSH is averaged at daily frequency to match AVISO resolution, see [block 6](https://github.com/ocean-next/eNATL60/blob/master/analysis/mesoscale-variability/notebooks/2019-11-25-AA-std-mean-ssh-eNATL60-1h-to-1d.ipynb)
  - Temporal mean and standart deviation are computed for both datasets ([eNATL60](https://github.com/ocean-next/eNATL60/blob/master/analysis/mesoscale-variability/notebooks/2019-11-25-AA-std-mean-ssh-eNATL60-1h-to-1d.ipynb) and [AVISO](https://github.com/ocean-next/eNATL60/blob/master/analysis/mesoscale-variability/notebooks/2019-11-25-AA-std-mean-ssh-AVISO.ipynb))
  - Results are stored in netcdf files for future reuse
  - Maps of standart deviation superimposed with mean as contours are produced [here](https://github.com/ocean-next/eNATL60/blob/master/analysis/mesoscale-variability/notebooks/2019-11-25-AA-plots-std-mean-ssh-AVISO-eNATL60-mac.ipynb) 
  
### Results

![plot](https://github.com/ocean-next/eNATL60/blob/master/04_assessment/mesoscale-variability/plots/std-mean-SSH-AVISO-eNATL60-BLBT02.png)
  

### External librairies needed
  
  - [python librairies](environment.yaml)

### License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
