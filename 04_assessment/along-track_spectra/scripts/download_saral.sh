#!/bin/bash

## DEPENDENCIES: python 2.7, motuclient (python), and NCO to be installed !

# Your CMEMS credentials
# => "https://resources.marine.copernicus.eu/?option=com_csw&task=results?option=com_csw&view=account"
USER_CMEMS='xxxxxxx'
PASS_CMEMS='xxxxxxx'

# Where to save on your computer:
DIR_SAVE="/data2/climate/SATELLITE/SARAL"
#DIR_SAVE="/MEDIA/data/SATELLITE/SARAL"
#DIR_SAVE="/mnt/meom/workdir/brodeau/SATELLITE/NEW/SARAL"

# Period of interest
YEAR="2017"
cm1="01" ; d1="01" ; h1="00:00:00" ; # day # 1 
cm2="03" ; d2="31" ; h2="23:59:59" ; # last day...



### end of safe user configuration ###############################

VAR2KEEP="time,latitude,longitude,cycle,track,sla_unfiltered"

f2d="SARAL_${YEAR}${cm1}${d1}-${YEAR}${cm2}${d2}.zip"

# Final file to create:
FILE_SAT="${DIR_SAVE}/SARAL_${YEAR}${cm1}${d1}-${YEAR}${cm2}${d2}.nc"


########################################
# Download and generate the SARAL data #
########################################

if [ ! -f ${FILE_SAT} ]; then

    dir_tmp=${DIR_SAVE}/tmp
    mkdir -p ${dir_tmp}
    cd ${dir_tmp}/
    
    if [ ! -f ./${f2d} ]; then

        # Need to download and unzip the archive

        # AL:
        #python -m motuclient --motu http://nrt.cmems-du.eu/motu-web/Motu \
        #       --service-id SEALEVEL_GLO_PHY_L3_NRT_OBSERVATIONS_008_044-DGF \
        #       --product-id dataset-duacs-nrt-global-al-phy-l3 \
        #       --date-min "${YEAR}-${cm1}-${d1} ${h1}" --date-max "${YEAR}-${cm2}-${d2} ${h2}" \
        #       --out-dir ${DIR_SAVE} --out-name ${f2d} \
        #       --user ${USER_CMEMS} --pwd ${PASS_CMEMS}


        # ALG:
        python -m motuclient --motu http://my.cmems-du.eu/motu-web/Motu \
               --service-id SEALEVEL_GLO_PHY_L3_REP_OBSERVATIONS_008_062-DGF \
               --product-id dataset-duacs-rep-global-alg-phy-l3 \
               --date-min "${YEAR}-${cm1}-${d1} ${h1}" --date-max "${YEAR}-${cm2}-${d2} ${h2}" \
               --out-dir ${dir_tmp} --out-name ${f2d} \
               --user ${USER_CMEMS} --pwd ${PASS_CMEMS}

        unzip -o ${f2d}
        
    fi
    
    # Need treatment:
    list=`\ls *.nc`

    for ff in ${list}; do

        echo

        fu=`echo ${ff} | sed -e s/'.nc'/'_unpacked.tmp'/g` ; # Name of unpacked file!
        fn=`echo ${ff} | sed -e s/'.nc'/'_tr.tmp'/g`       ; # Name of file with an UNLIMITED time record

        echo "${ff} -> ${fu} -> ${fn}"; echo

        # Unpacking first for safety! => otherwize lon and lat are screwed up!
        if [ ! -f ${fu} ]; then
            ncrename -v longitude,vxx -v latitude,vyy ${ff}            
            ncpdq -U ${ff} -o ${fu}
            echo ; echo " *** Unpacked ${ff} into ${fu} !!!"; echo
            ncrename -v vxx,longitude -v vyy,latitude ${fu}            
            rm -f ${fn}
        fi

        if [ ! -f ${fn} ]; then
            ncecat -O ${fu} ${fn}     # Add degenerate record dimension named "record"
            echo ; echo
            ncpdq -O -a time,record ${fn} ${fn} # Switch "record" and "time"
            echo ; echo
            ncwa -O -a record ${fn} ${fn}       # Remove (degenerate) "record"
            echo ; echo
        fi

        #if [ ! -f ${fn}4 ]; then
        #    ncks -4 -L 5 --cnk_dmn time_counter,2000 ${fn} -o ${fn}4
        #fi

    done
    

    CMD="ncrcat -O -h -v ${VAR2KEEP} *_tr.tmp -o ${FILE_SAT}"
    echo; echo " *** ${CMD}"; ${CMD};
    
    cd ${DIR_SAVE}/
    
    rm -rf ./tmp/*.nc ./tmp/*.tmp
    
else
    echo
    echo " File ${FILE_SAT} is already here! (`pwd`)"
    echo
fi

