#  Production of NEMO-eNATL60 simulations

We provide here some information on how NEMO-eNATL60 twin experiments have been run. 

## Computing resources 

The computing resources for running NEMO-eNATL60 twin experiments have been granted through (PRACE)[https://prace-ri.eu] 16th call, under a projet named ReSuMPTiOn (Revealing SubMesoscale Processes and Turbulence in the Ocean, PI. L. Brodeau). Access has been granted to MareNostrum 4 supercomputer at Barcelona Supercomputing Center ((BSC)[https://www.bsc.es/]). MareNostrum 4 is a supercomputer with a peak performance of 11.15 Petaflops. It has been deployed at BSC in 2017. It is based on Intel Xeon Platinum processors, Lenovo SD530 Compute Racks, a Linux Operating System and an Intel Omni-Path interconnection. Besides the PRACE project, a partnership has been set-up with (CINES)[https://www.cines.fr/] supercomputing center (Montpellier, France) for hosting and analysing the model data.  

## Preprocessing

NEMO-eNATL60 model grid combines 6.3 billion compute points (8354 x 4727 points for the horizontal grid and 300 vertical levels). The preprocessing of input data (bathymetry, coastline, atmospheric forcing, initial conditions) therefore requires substancial computing resources too. Atmospheric forcing data have been interpolated at the run-time from their native grid. Bathymetry, coastline and initial states have been prepared at CINES and BSC before the computing campaign. 

## Actual run production 

The minimum HPC requirement for NEMO-eNATL60 (6.3 billion compute points) is about 35 TB of memory and 15000 cores in parallel. Scallability tests have been performed on several PRACE supercomputers during a preparatory access grant in order to identify the most appropriate machine in Europe for running eNATL60 experiments. The best performances and time-to-solution was obtained on Marenostrum 4 at BSC. The converged production set-up uses 18000 cores and a 40s timestep, so that integrating a model-day requires approximately 50min elaspe time. The simulations have been produced between Oct. 2018 and May 2019 and used about 40 millions CPU hours. The production was split into 5 model-day segments with restarts files ~1.2Tb. In total, the model has been integrated for 53 model-months of simulation, featuring a 19 model-month overlap between the two experiments. The production has been severely delayed during phases of peak load on Marenostrum 4, due to repeated model crashes related to the NEMO IO server memory requirements. In consequence, a substancial fraction of the 5d production segments had to be run several times. The support team at BSC has been very helpful and supportive during the whole production cycle.   

## IO and storage strategy 

A major challenge of NEMO-eNATL60 experiments is related to the size of the output data. Indeed, we have decided to store a full 3D archive of model data at hourly frequency, hourly temporal resolution being essential for analysing the role of internal tides and internal waves on energy exchanges in the open ocean. Each 5d-segment therefore produces about 7.8Tb of model data. In total, the 53 model-months of simulation have generated about 1.5Pb of model data. CINES has offered to host this whole dataset for several years as a benchmarck for the use and deployment of interactive data analysis workflows based on (Pangeo)[https://pangeo.io] on their supercomputers (Occigen). During the run productions, the whole model data archive has been transferred via the network from BSC to CINES where it is now available openly to the commmunity. Surface field have also been duplicated on Pangeo cloud.   
