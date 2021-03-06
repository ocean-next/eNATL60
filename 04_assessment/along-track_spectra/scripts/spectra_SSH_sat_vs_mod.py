#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

#    L. Brodeau, 2018

import sys
from os import path, getcwd, mkdir
import argparse as ap
import numpy as nmp
#
import scipy.signal as signal
from netCDF4 import Dataset
#
from string import find
import warnings
warnings.filterwarnings("ignore")
import time
#
import mod_plot_spectra as mps


reload(sys)
sys.setdefaultencoding('utf8')


# User-configurable part:

l_tapper      = True ; # apply tappering !
l_detrend_lin = True ; # apply a linear detrending on data segment before computing spectrum...
l_rm_i_noise  = False

dir_figs='./figs'
fig_ext='svg' ; # image type to be generated

rcut_by_time = 1.2 # specify in seconds the time gap between two obs to detect and discontinuity and therefore
#                  # should be considered as a cut!

rcut_by_dist = 7.8 # same as rcut_by_time, but in terms of distance (in km) between two consecutive points!
#                  # time criterion "rcut_by_time" would have been sufficient if SARAL data was not bugged!!!
#                  # => in SARAL data, spotted two consecutive points with the usual dt and a huge dL !!!
#                  #   => like if the satellite undergone an extremely short huge acceleration !!!
#                  #   => ex: 3rd of August 2016 around 07:53:43 !!!

nvalid_seg = 120  # specify the minimum number of values a segment should contain to be considered and used!

r_max_amp_ssh = 1.5 # in meters

# Look and feel for the plot:

clr_red = '#AD0000'

# Color OceanNext style:
clr_sat = '#ffed00'
clr_mod = '#008ab8'

rDPI=100. ; # dots per inch for image to create...

#=============== en of configurable part ================================



if not path.exists(dir_figs): mkdir(dir_figs)



################## ARGUMENT PARSING / USAGE #########################################################################################

# Defaults before reading command-line arguments:
cn_mod = "NEMO"
cn_sat = "Altimetry"
cn_box = "Unknown box"
pow10_min_y = -8
pow10_max_y =  2

parser = ap.ArgumentParser(description='Generate along-track spectral comparison of SSH, model versus satellite')
#
requiredNamed = parser.add_argument_group('required arguments')
requiredNamed.add_argument('-i', '--fin' , required=True, help='specify output "result" file from interp_to_ground_track.x@SOSIE')
requiredNamed.add_argument('-m', '--vmod', required=True, help='specify the name of the model variable for SSH' )
requiredNamed.add_argument('-s', '--vsat', required=True, help='specify the name of the satellite variable for SSH')
#
parser.add_argument('-B', '--name_box', default=cn_box,   help='name of the rectangular region (box) considered')
parser.add_argument('-M', '--name_mod', default=cn_mod,   help='name of the model (ex: NEMO-eNATL60)')
parser.add_argument('-S', '--name_sat', default=cn_sat,   help='name of the satellite (ex: SARAL-Altika)')
#parser.add_argument('-z', '--zld' ,                           help='specify the topography netCDF file to use (field="z")')
parser.add_argument('-a', '--pmin_y', type=int, default=pow10_min_y, help='minimum y-axis value to display in terms of 10^pmin_y')
parser.add_argument('-b', '--pmax_y', type=int, default=pow10_max_y, help='maximum y-axis value to display in terms of 10^pmax_y')
#
args = parser.parse_args()

cf_in  = args.fin
cv_mod = args.vmod
cv_sat = args.vsat
cn_box = args.name_box
cn_mod = args.name_mod
cn_sat = args.name_sat
pow10_min_y = args.pmin_y
pow10_max_y = args.pmax_y

#####################################################################################################################################


cfs  = path.basename(cf_in)
cseas = ''
if ('JFM' in cfs) and not('JAS' in cfs) : cseas = 'JFM'; vseas = ['01','02','03']
if ('JAS' in cfs) and not('JFM' in cfs) : cseas = 'JAS'; vseas = ['07','08','09']
print '\n *** Season: '+cseas+'\n'

print ' *** Opening file '+cf_in+'!'
id_in    = Dataset(cf_in)
vt_epoch = id_in.variables['time'][:]
vmodel   = id_in.variables[cv_mod][:]
vsatel   = id_in.variables[cv_sat][:]
vlon     = id_in.variables['longitude'][:]
vlat     = id_in.variables['latitude'][:]
vdist    = id_in.variables['distance'][:]
id_in.close()
print "  => Everything read!\n"

nbr = len(vt_epoch)
cyear = time.strftime("%Y", time.localtime(vt_epoch[2]))




ii=nbr/300
ib=max(ii-ii%10,1)
xticks_d=30.*ib


vmask = vmodel.mask

(idx_ok,) = nmp.where(vmask==False) ; # indices with valid values!
nbr_v = len(idx_ok)

print ' *** '+str(nbr_v)+' valid points out of '+str(nbr)+' !\n'

# Will extract the N valid data segments:
nb_seg=0
idx_seg_start = [] ; # index of first valid point of the segment
idx_seg_stop  = [] ; # index of last  valid point of the segment

jr=0
while jr < nbr:
    # Ignoring masked values and zeros...
    if (not vmask[jr]) and (vmodel[jr]!=0.0) and (vmodel[jr]<100.):
        nb_seg = nb_seg + 1
        print '\n --- found seg #'+str(nb_seg)+' !'
        idx_seg_start.append(jr)
        print ' => starting at jt='+str(jr)
        while (not vmask[jr+1]) and (vmodel[jr+1]!=0.0) and (vt_epoch[jr+1]-vt_epoch[jr] < rcut_by_time) and (vdist[jr+1]-vdist[jr] < rcut_by_dist) and (vmodel[jr]<100.) :
            jr = jr+1
            if jr==nbr-1: break
        idx_seg_stop.append(jr)
        print ' => and stoping at jt='+str(jr)
    jr = jr+1

if len(idx_seg_start) != nb_seg: print ' ERROR #1!'; sys.exit(1)



# Maximum number of poins in the segments:

isd = nmp.asarray(idx_seg_stop[:]) - nmp.asarray(idx_seg_start[:]) + 1
print '\n lengths =>', isd[:]
nbp_max = max(isd)
print '\n *** Longest segments has nbp_max='+str(nbp_max)+' points!\n'

# Treat only segments with at least nvalid_seg points:
(vtreat,) = nmp.where(isd >= nvalid_seg)
nb_v_seg = len(vtreat)
rN = nmp.mean(isd[vtreat])
print '\nMean segment-length for the '+str(nb_v_seg)+' segments with at least '+str(nvalid_seg)+' points:', round(rN,1)

Nsp = int(rN/10.)*10
print '  ==> Nsp = '+str(Nsp)
(vtreat,) = nmp.where(isd >= Nsp)
nb_v_seg = len(vtreat)
print ' ==> will use '+str(nb_v_seg)+' segments with a fixed length of '+str(Nsp)+' point!\n'

x_all_spectra_s = nmp.zeros((nb_v_seg,Nsp)) # array to store all spectra in...
x_all_spectra_m = nmp.zeros((nb_v_seg,Nsp)) # array to store all spectra in...

clabel_mod=cn_mod+' ("'+cv_mod+'")'
clabel_sat=cn_sat+' ("'+cv_sat+'")'

jcpt = -1
for js in vtreat:
    
    jcpt= jcpt+1
    it1 = idx_seg_start[js]
    it2 = idx_seg_stop[js]
    nbp = it2-it1+1    
    cseg = '%2.2i'%(js+1)

    print '\n\n ###################################'
    print '  *** Seg #'+cseg+' of '+cn_box+':'
    print '  ***   => originally '+str(nbp)+' points in this segment (from '+str(it1)+' to '+str(it2)+')'

    # nb of points in excess / Nsp:
    nxcs = nbp - Nsp
    jmp_strt = nxcs/2
    jmp_stop = nxcs/2 + nxcs%2
    it1 = it1+jmp_strt
    it2 = it2-jmp_stop
    print '  ***   => we only retain '+str(it2-it1+1)+' points from '+str(it1)+' to '+str(it2)+'!'
    
    # Checking the typical distance (in km) between two measures:
    dmean = nmp.mean(vdist[it1+1:it2+1]-vdist[it1:it2])
    print '\n Mean distance between two consecutive points is '+str(dmean)+' km\n'
    # Sample spacing in [km] (inverse of the sampling rate):
    rdist_sample = round(dmean,3)
    print ' => will use a spatial sample spacing of '+str(rdist_sample)+' km\n'

    # First centering the two time-series about 0, and tappering at extremities (filling with zeros)
    vs_s = nmp.zeros(Nsp) ; vs_m = nmp.zeros(Nsp)
    print '             (length = '+str(len(vsatel[it1:it2+1]))+' / '+str(Nsp)+')'
    
    vs_s[:] = vsatel[it1:it2+1]
    vs_m[:] = vmodel[it1:it2+1]

    # Linear detrending
    if l_detrend_lin:
        vs_s[:] = signal.detrend(vs_s[:],type='linear')
        vs_m[:] = signal.detrend(vs_m[:],type='linear')

    # Centering about 0:
    vs_s = vs_s - nmp.mean(vs_s)
    vs_m = vs_m - nmp.mean(vs_m)

    # Tappering:
    if l_tapper:        
        wdw =  signal.tukey(Nsp,0.5)
        vs_s = vs_s*wdw
        vs_m = vs_m*wdw
        
    # Power Spectrum:
    vYf_s = 2.*(rdist_sample/float(Nsp)) * nmp.abs(nmp.fft.fft(vs_s))**2
    vYf_m = 2.*(rdist_sample/float(Nsp)) * nmp.abs(nmp.fft.fft(vs_m))**2

    # Wave numbers:
    if jcpt==0:
        vk  = nmp.fft.fftfreq(Nsp, rdist_sample)
        idx = nmp.argsort(vk)

    # Saving for current segment:
    x_all_spectra_s[jcpt,:] = vYf_s[idx]
    x_all_spectra_m[jcpt,:] = vYf_m[idx]

        

# Plotting mean spectrum:
vps_mod = nmp.mean(x_all_spectra_m[:,:],axis=0)
vps_sat = nmp.mean(x_all_spectra_s[:,:],axis=0) 
cinfrm =  'Box: '+cn_box+'\n' \
         +'Period: '+cseas+' '+cyear+'\n' \
         +'Segments: '+str(Nsp)+' p\n' \
         +'Segm. used: '+str(nb_v_seg)+'\n' \
         +r'$\Delta$L: '+str(round(rdist_sample,1))+' km'


# remove white noise at fine scale for satellite (instrument) [advice from Clement Ubelmann]
cxtr_noise=''
if l_rm_i_noise:    
    rwn = nmp.mean(vps_sat[Nsp-15:Nsp])
    vps_sat = vps_sat - rwn
    cxtr_noise='_denoised'

# Sample spacing rdist_sample
cpout   = dir_figs+'/SSH_pow-spectrum_'+cn_box+'__'+cn_mod+'--'+cn_sat+'__'+cseas+cxtr_noise
cfigure = cpout+'.'+fig_ext

print ' *** cn_sat =', cn_sat    

ii = mps.plot_pow_spectrum_ssh( vk[idx], vps_mod, clab1=clabel_mod, clr1=clr_mod, lw1=5, \
                                cfig_name=cfigure, cinfo=cinfrm, \
                                L_min=10., L_max=1200., P_min_y=pow10_min_y, P_max_y=pow10_max_y, \
                                l_show_k4=False, l_show_k5=True, l_show_k11o3=False, l_show_k2=True, \
                                vk2=vk[idx], vps2=vps_sat, clab2=clabel_sat, clr2=clr_sat, lw2=4 )

nmp.savez( cpout+'_mod.npz',               vk=vk[idx], vps=vps_mod )
nmp.savez( cpout+'_sat'+cxtr_noise+'.npz', vk=vk[idx], vps=vps_sat )
