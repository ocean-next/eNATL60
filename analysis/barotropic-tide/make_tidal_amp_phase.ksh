#!/bin/ksh
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --constraint=VISU
#SBATCH -J make_tide
#SBATCH -e make_tide.e%j
#SBATCH -o make_tide.o%j
#SBATCH --time=5:59:00
#SBATCH --exclusive

CONFIG=eNATL60
CASE=BLBT02

mkdir -p /scratch/cnt0024/hmg2840/albert7a/eNATL60/eNATL60-BLBT02-S/1h/tide
cd /scratch/cnt0024/hmg2840/albert7a/eNATL60/eNATL60-BLBT02-S/1h/tide

ln -sf /store/CT1/hmg2840/lbrodeau/eNATL60/eNATL60-BLBT02*-S/*/eNATL60-BLBT02*_1h_*_gridT-2D_*.nc .

ln -sf /scratch/cnt0024/hmg2840/albert7a/DEV/git/eNATL60-plots-paper/amp-phase-tides-FES/namelist_tideharm namelist

/scratch/cnt0024/hmg2840/albert7a/DEV/git/TIDAL_TOOLS/bin/tid_harm_ana -l *gridT-2D*nc
