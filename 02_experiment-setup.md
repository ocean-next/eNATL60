# Description of NEMO-eNATL60  experiment set-up 

We here provide a brief description of NEMO-eNATL60 model configuration and experiment. The code used for producing eNATL60 simulations is available on a separate GitHub repository.

eNATL60 is a basin-scale configuration of the NEMO (Nucleus for European Modeling of the Ocean) at ultrahigh horizontal and vertical resolution. eNATL60 is the successor and horizontally extended version of NATL60. eNATL60 spans the North Atlantic from about 6°N up to the polar circle and fully includes the Gulf of Mexico, the Med Sea, and the Black Sea.

### In short

- Numerical code: NEMO 3.6 + xios-2.0 (https://www.nemo-ocean.eu/)
- Horizontal grid: 1/60°, 8354×4729 points
- 0.8 km < Δx < 1.6 km
- Vertical grid: 300 levels
- LBCs U,V, T, S & sea-ice: daily, GLORYS12 v1 (1/12°, Mercator Ocean)
- LBCs tide (SSH, u, v) : FES2014 (F. Lyard)
- LBCs coast: No slip!
- Atmospheric forcing: 3-hourly, ERA-interim (ECMWF)
- \# processors in parallel required: >= 18000
- Model time step: 40s
- Model integration speed: 45 minutes for 1 model day

![plot](https://github.com/ocean-next/eNATL60/blob/master/figs/eNATL60_domain.png)
*Figure 1: horizontal extent of the eNATL60 domain illustrated by a snapshot of surface current speed.*


## NEMO-eNATL60 model configuration 
 - domain : 
 - grid : 
 - bathymetry : 
 - surface forcing : 
 - boundary conditions : 

### Configuration files
For the two experiments NEMO ocean and sea-ice namelists, as well as XIOS xml files can be found on the [`meom-configurations` GitHub page](https://github.com/meom-configurations).

 - [eNATL60-BLB002 (experimemt without explicit tidal motion)](https://github.com/meom-configurations/eNATL60-BLB002/tree/master/namelists_xml)
 - [eNATL60-BLBT02 (experimemt WITH explicit tidal motion)](https://github.com/meom-configurations/eNATL60-BLBT02/tree/master/namelists_xml)


## NEMO-eNATL60 model experiments

- eNATL60-BLB002: experiment without explicit tidal motion
- eNATL60-BLBT02: experiment WITH explicit tidal motion

![plot](https://github.com/ocean-next/eNATL60/blob/master/figs/eNATL60_twin_exp.svg)
*Figure 2: Twin experiment design.*




## NEMO-eNATL60 source code

The source code for the two experiments is hosted on the [`meom-configurations` GitHub page](https://github.com/meom-configurations).

 - [eNATL60-BLB002 (experimemt without explicit tidal motion)](https://github.com/meom-configurations/eNATL60-BLB002)
 - [eNATL60-BLBT02 (experimemt WITH explicit tidal motion)](https://github.com/meom-configurations/eNATL60-BLBT02)



