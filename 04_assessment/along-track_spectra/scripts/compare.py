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


CSAT = 'SARAL'

# JAS

fs_1 = 'figs/SSH_pow-spectrum_Azores__eNATL60-tide--'+CSAT+'__JAS_sat.npz'     ; clab_s1 = CSAT+' (JAS)'
fs_2 = 'figs/SSH_pow-spectrum_Azores__eNATL60-tide--'+CSAT+'__JFM_sat.npz'     ; clab_s2 = CSAT+' (JFM)'

fm_1 = 'figs/SSH_pow-spectrum_Azores__eNATL60-tide--'+CSAT+'__JAS_mod.npz'    ; clab_m1 = 'eNATL60-tide (JAS)'
fm_2 = 'figs/SSH_pow-spectrum_Azores__eNATL60-tide--'+CSAT+'__JFM_mod.npz'    ; clab_m2 = 'eNATL60-tide (JFM)'
fm_3 = 'figs/SSH_pow-spectrum_Azores__eNATL60-notide--'+CSAT+'__JAS_mod.npz'    ; clab_m3 = 'eNATL60-notide (JAS)'
fm_4 = 'figs/SSH_pow-spectrum_Azores__eNATL60-notide--'+CSAT+'__JFM_mod.npz'    ; clab_m4 = 'eNATL60-notide (JFM)'



data_s_1 = nmp.load(fs_1)
data_s_2 = nmp.load(fs_2)

data_m_1 = nmp.load(fm_1)
data_m_2 = nmp.load(fm_2)
data_m_3 = nmp.load(fm_3)
data_m_4 = nmp.load(fm_4)

#print data_s_1

vk_s_1  = data_s_1['vk'] ; vps_s_1 = data_s_1['vps']
vk_s_2  = data_s_2['vk'] ; vps_s_2 = data_s_2['vps']

vk_m_1  = data_m_1['vk'] ; vps_m_1 = data_m_1['vps']
vk_m_2  = data_m_2['vk'] ; vps_m_2 = data_m_2['vps']
vk_m_3  = data_m_3['vk'] ; vps_m_3 = data_m_3['vps']
vk_m_4  = data_m_4['vk'] ; vps_m_4 = data_m_4['vps']
 


ii = mps.plot_pow_spectrum_ssh( vk_s_1,    vps_s_1, clab1=clab_s1, \
                                L_min=10., L_max=1200., P_min_y=-7, P_max_y=1, \
                                vk2=vk_s_2, vps2=vps_s_2, clab2=clab_s2, \
                                vk3=vk_m_1, vps3=vps_m_1, clab3=clab_m1, \
                                vk4=vk_m_2, vps4=vps_m_2, clab4=clab_m2, \
                                vk5=vk_m_3, vps5=vps_m_3, clab5=clab_m3, \
                                vk6=vk_m_4, vps6=vps_m_4, clab6=clab_m4 )




#ii = mps.plot_pow_spectrum_ssh( vk_s_1,    vps_s_1, \
#                                vk2=vk_m_1, vps2=vps_m_1, \
#                                vk3=vk_s_2, vps3=vps_s_2, \
#                                vk4=vk_m_2, vps4=vps_m_2 )
#, clab1=clab_s, clr1=clr_mod, lw1=5, \
#                                cfig_name=cfigure, cinfo=cinfrm, \
#                                L_min=10., L_max=1200., P_min_y=pow10_min_y, P_max_y=pow10_max_y, \
#                                l_show_k4=False, l_show_k5=True, l_show_k11o3=False, l_show_k2=True, \
#                                vk2=vk[idx], vps2=vps_sat, clab2=clabel_sat, clr2=clr_sat, lw2=4 )





