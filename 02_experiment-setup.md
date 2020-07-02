# Description of NEMO-eNATL60  experiment set-up 

We here provide a brief description of NEMO-eNATL60 model configuration and experiment. The code used for producing eNATL60 simulations is available on a separate GitHub repository.

eNATL60 is a basin-scale configuration of the NEMO (Nucleus for European Modeling of the Ocean) at ultrahigh horizontal and vertical resolution. eNATL60 is the successor and horizontally extended version of NATL60. eNATL60 spans the North Atlantic from about 6°N up to the polar circle and fully includes the Gulf of Mexico, the Med Sea, and the Black Sea.

## NEMO-eNATL60 model configuration 

- Numerical code: NEMO 3.6 + xios-2.0 (https://www.nemo-ocean.eu/)
- Horizontal grid: 1/60°, 8354×4729 points
- 0.8 km < Δx < 1.6 km
- Vertical grid: 300 levels
- Lateral Boundary Conditions for U,V, T, S & sea-ice: daily, GLORYS12 v1 (1/12°, Mercator Ocean)
- Lateral Boundary Conditions for tides (SSH, u, v) : FES2014 (F. Lyard)
- Lateral Boundary Conditions at the coast: No slip.
- Atmospheric forcing: 3-hourly, ERA-interim (ECMWF)
- \# processors in parallel required: >= 18000
- Model time step: 40s
- Model integration speed: 45 minutes for 1 model day


![plot](https://github.com/ocean-next/eNATL60/blob/master/figs/deptht.svg)
*Figure 1: Characteristics of the 300-level vertical `z-coordinate` grid of eNATL60. Depth and thickness of levels.*


NEMO ocean and sea-ice namelists, as well as XIOS xml files can be found on the [`meom-configurations` GitHub page](https://github.com/meom-configurations). See the links below. 


## NEMO-eNATL60 twin model experiments
The model configuration has been implemented and run in two different simulations. The reference experiment eNATL60-BLB002 has been run WITHOUT explicit tidal forcing; the sensitivity experiment eNATL60-BLBT02 was run WITH explicit tidal forcing. The overall experiment strategy (simulated period, model spin-up and output strategy) is summarized below. 

![plot](https://github.com/ocean-next/eNATL60/blob/master/figs/eNATL60_twin_exp.svg)
*Figure 2: eNATL60 twin experiment strategy.*


## Sources codes : 

The source code for the two experiments is documented on [`meom-configurations` GitHub repos](https://github.com/meom-configurations).

 - [eNATL60-BLB002 experiment (WITHOUT explicit tidal motion)](https://github.com/meom-configurations/eNATL60-BLB002)
 - [eNATL60-BLBT02 experiment (WITH explicit tidal motion)](https://github.com/meom-configurations/eNATL60-BLBT02)


For the two experiments NEMO ocean and sea-ice namelists, as well as XIOS xml files can be found at : 

 - [namelist eNATL60-BLB002 (WITHOUT explicit tidal motion)](https://github.com/meom-configurations/eNATL60-BLB002/tree/master/namelists_xml)
 - [namelist eNATL60-BLBT02 (WITH explicit tidal motion)](https://github.com/meom-configurations/eNATL60-BLBT02/tree/master/namelists_xml)



## License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

