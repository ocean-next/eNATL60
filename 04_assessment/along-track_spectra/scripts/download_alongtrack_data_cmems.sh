#!/bin/bash

## DEPENDENCIES: python 2.7, motuclient (python), and NCO to be installed !

# Your CMEMS credentials
# => "https://resources.marine.copernicus.eu/?option=com_csw&task=results?option=com_csw&view=account"
USER_CMEMS='xxxxxxx'
PASS_CMEMS='xxxxxxx'

# Where to save on your computer (absolute path please!):
#DIR_SAVE="/data2/climate/SATELLITE"
DIR_SAVE="`pwd`"

############################ end of "safe" user configuration ###############################


if [ "${4}" = "" ]; then
    echo
    echo "USAGE: `basename ${0}` <satellite_name> <YEAR> <MMDD1> <MMDD2>"
    echo
    echo "     * currently supported satellites => 'saral' (SARAL-AltiKa) or 'sentinel' (Sentinel 3A)"
    echo
    exit
fi

sat="${1}"
YEAR="${2}"
DT1="${3}"
DT2="${4}"

cm1=`echo ${DT1} | cut -c1-2`
cm2=`echo ${DT2} | cut -c1-2`
cd1=`echo ${DT1} | cut -c3-4`
cd2=`echo ${DT2} | cut -c3-4`

ch1="00:00:00" ; ch2="23:59:59" ; # Begining and end of a day...


case ${sat} in
    "saral")    NAME="SARAL"
                SID="SEALEVEL_GLO_PHY_L3_REP_OBSERVATIONS_008_062-DGF"
                PID="dataset-duacs-rep-global-alg-phy-l3"
                ;;
    "sentinel") NAME="SENTINEL3A"
                SID="SEALEVEL_GLO_PHY_L3_REP_OBSERVATIONS_008_062-DGF"
                PID="dataset-duacs-rep-global-s3a-phy-l3"
                ;;
    *) echo
       echo " PROBLEM: Satellite ${sat} is unknown!"
       echo; exit
       ;;
esac


VAR2KEEP="time,latitude,longitude,cycle,track,sla_unfiltered" ; # variables to keep from original downloaded files...

f2d="${NAME}_${YEAR}${cm1}${cd1}-${YEAR}${cm2}${cd2}.zip"

dsave="${DIR_SAVE}/${NAME}" ; mkdir -p ${dsave}

# Final file to create:
FILE_SAT="${dsave}/${NAME}_${YEAR}${cm1}${cd1}-${YEAR}${cm2}${cd2}.nc"


############################################
# Download and generate the satellite data #
###########################################

if [ ! -f ${FILE_SAT} ]; then

    dir_tmp=${dsave}/tmp
    mkdir -p ${dir_tmp}
    cd ${dir_tmp}/

    if [ ! -f ./${f2d} ]; then

        # Need to download and unzip the archive

        echo
        echo "Launching download for ${YEAR}-${cm1}-${cd1} ${ch1} -- ${YEAR}-${cm2}-${cd2} ${ch2}"
        echo
        
        python -m motuclient --motu http://my.cmems-du.eu/motu-web/Motu \
               --service-id ${SID} \
               --product-id ${PID} \
               --date-min "${YEAR}-${cm1}-${cd1} ${ch1}" --date-max "${YEAR}-${cm2}-${cd2} ${ch2}" \
               --out-dir ${dir_tmp} --out-name ${f2d} \
               --user ${USER_CMEMS} --pwd ${PASS_CMEMS}
        echo
        
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

    cd ${dsave}/

    rm -rf ./tmp/*.nc ./tmp/*.tmp

else
    echo
    echo " File ${FILE_SAT} is already here! (`pwd`)"
    echo
fi
