# NEMO-eNATL60 description and assessment repository

This repository describes the twin model simulations performed in 2019 with [NEMO](https://www.nemo-ocean.eu) ocean model over the North Atlantic at 1/60° grid resolution by [Ocean-Next](https://www.ocean-next.fr/) and the [MEOM group](http://meom-group.github.io) at [IGE](http://www.ige-grenoble.fr) on MareNostrum supercomputer at [BSC](https://www.bsc.es) within a [PRACE](http://prace-ri.eu/) project.

To get an idea of what eNATL60 model data look like, you may have a look a the series of video animations  available on [Ocean-Next vimeo channel](https://vimeo.com/oceannext).

![plot](https://github.com/ocean-next/eNATL60/blob/master/figs/eNATL60_domain.png)<br>
*Figure 1: horizontal extent of the eNATL60 domain illustrated by a snapshot of surface current speed.*



## Why this repository ? 

Geoscientific numerical simulations like eNATL60 require substancial computing ressources and have a large carbon footprint. This is why we believe that they should be designed and analysed collaboratively so that they could serve many different scientific applications.

The volume of data generated by such computation is also so large that the scientific assessment of the model solution is by itself a substancial undertaking. We believe that this effort should be a community effort with input from the users of the simulation data.

We have therefore decided to gather in a GitHub repository all the relevant information related to the model set-up, experiment and production, and to propose a workflow for sharing the protocols and the results of comparison of the model solutions with observations. 

We have adopted this approach rather than a more conventional scientific article or report because we hope that an open and collaborative workflow will more effectively allow to build a shared understanding of the strengths and weaknesses of our simulations. 

More generally, we hope that this effort will help foster more collaborative and reproducible workflows in geoscientific modelling. 

Should you have any comment on the structure or on the content of this repository, do not hesitate to open a GitHub [issue](https://github.com/ocean-next/eNATL60/issues) and share your thoughts. 

## Content of the repository 

  - A list of [contributors](./00_contributors.md) involved at various stages of the project development;
  - A statement of our [motivations](./01_motivation.md) for running these numerical experiments; 
  - A description of the model configuration, [set-up and experiments](./02_experiment-setup.md);
  - Some more details on the [production](./03_production.md) of the simulations; 
  - Practical information on how to access the model [data](./05_data.md);
  - Results on the [assessment](./04_assessment/README.md) of the model with respect to observationnal datasets;
  - A list of on-going [studies and groups](./06_dissemination.md) using eNATL60 model data. 


## Contributing to this repository 

As described above, you may open [issues](https://github.com/ocean-next/eNATL60/issues) for asking questions, for sharing your thoughts or for proposing improvements to this repository.

As a user of eNATL60 model data, you may also contribute to the assessement of the simulation by fluxing back the results and the code of your comparisons of eNATL60 model data with observations. 

In practice, please follow the template of one of the available [assessments](./04_assessment/) and formulate a pull request to this repository. We will try to respond shortly.

## Citing this repository

As it grows over time, this GitHub repository will regularly be archived on [Zenodo](https://zenodo.org) and tagged with a digital object identifier (doi). Should you need to cite NEMO-eNATL60 simulations, please refer to the latest Zenodo doi.

## License
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
