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





clr_sat_jas = '#FFBE69'  ; #orange
#clr_sat_jas = '#ffed00' ; #jaune ON
#clr_sat_jfm = '#008ab8'  ; #bleu ON
clr_sat_jfm = '#0BD5E3'

clr_mod1_jas = '#AD0000'
clr_mod1_jfm = '#277ABA'

clr_mod2_jas = '#FA5773'
clr_mod2_jfm = '#52FA8A'



for CSAT in [ 'SARAL', 'Sentinel3' ]:

    for CBOX in ['GulfS', 'Azores']:

        pmin=-7 ; pmax=1
        if CBOX == 'GulfS': pmin=-6 ; pmax=2
        
        
        # JAS
    
        fs_1 = 'figs/SSH_pow-spectrum_'+CBOX+'__eNATL60-tide--'+CSAT+'__JAS_sat.npz'     ; clab_s1 = CSAT+' (JAS)'
        fs_2 = 'figs/SSH_pow-spectrum_'+CBOX+'__eNATL60-tide--'+CSAT+'__JFM_sat.npz'     ; clab_s2 = CSAT+' (JFM)'
    
        fm_1 = 'figs/SSH_pow-spectrum_'+CBOX+'__eNATL60-tide--'+CSAT+'__JAS_mod.npz'    ; clab_m1 = 'eNATL60-tide (JAS)'
        fm_2 = 'figs/SSH_pow-spectrum_'+CBOX+'__eNATL60-tide--'+CSAT+'__JFM_mod.npz'    ; clab_m2 = 'eNATL60-tide (JFM)'
        fm_3 = 'figs/SSH_pow-spectrum_'+CBOX+'__eNATL60-notide--'+CSAT+'__JAS_mod.npz'    ; clab_m3 = 'eNATL60-notide (JAS)'
        fm_4 = 'figs/SSH_pow-spectrum_'+CBOX+'__eNATL60-notide--'+CSAT+'__JFM_mod.npz'    ; clab_m4 = 'eNATL60-notide (JFM)'
    
        data_s_1 = nmp.load(fs_1)
        data_s_2 = nmp.load(fs_2)
    
        data_m_1 = nmp.load(fm_1)
        data_m_2 = nmp.load(fm_2)
        data_m_3 = nmp.load(fm_3)
        data_m_4 = nmp.load(fm_4)
    
        vk_s_1  = data_s_1['vk'] ; vps_s_1 = data_s_1['vps']
        vk_s_2  = data_s_2['vk'] ; vps_s_2 = data_s_2['vps']
    
        vk_m_1  = data_m_1['vk'] ; vps_m_1 = data_m_1['vps']
        vk_m_2  = data_m_2['vk'] ; vps_m_2 = data_m_2['vps']
        vk_m_3  = data_m_3['vk'] ; vps_m_3 = data_m_3['vps']
        vk_m_4  = data_m_4['vk'] ; vps_m_4 = data_m_4['vps']
     
    
    
        ii = mps.plot_pow_spectrum_ssh( vk_s_1,    vps_s_1, clab1=clab_s1, clr1=clr_sat_jas, \
                                        cfig_name='eNATL60-twin_vs_'+CSAT+'_'+CBOX+'.svg', cinfo=CSAT+': '+CBOX, \
                                        L_min=10., L_max=1200., P_min_y=pmin, P_max_y=pmax, \
                                        vk2=vk_s_2, vps2=vps_s_2, clab2=clab_s2, clr2=clr_sat_jfm, \
                                        vk3=vk_m_1, vps3=vps_m_1, clab3=clab_m1, clr3=clr_mod1_jas, \
                                        vk4=vk_m_2, vps4=vps_m_2, clab4=clab_m2, clr4=clr_mod1_jfm, \
                                        vk5=vk_m_3, vps5=vps_m_3, clab5=clab_m3, clr5=clr_mod2_jas, \
                                        vk6=vk_m_4, vps6=vps_m_4, clab6=clab_m4, clr6=clr_mod2_jfm )
    
    

