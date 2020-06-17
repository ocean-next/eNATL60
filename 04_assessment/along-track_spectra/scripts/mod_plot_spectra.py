#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-

#    L. Brodeau, 2018

import sys
import numpy as nmp
#
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

#reload(sys)
#sys.setdefaultencoding('utf8')

clr_red = '#AD0000'

# Color OceanNext style:
clr_sat = '#ffed00'
clr_mod = '#008ab8'

rDPI=100. ; # dots per inch for image to create...


def plot_pow_spectrum_ssh( vk1, vps1, clab1=None, clr1=clr_mod, lw1=6, \
                           cfig_name='fig_spectrum_SSH.png', cinfo='', \
                           L_min=7., L_max=5000., P_min_y=-6, P_max_y=6,    \
                           l_show_k11o3=False, l_show_k5=False, l_show_k4=False, l_show_k2=False, \
                           vk2=[], vps2=[], clab2=None, clr2=clr_sat, lw2=3, \
                           vk3=[], vps3=[], clab3=None, clr3='b',   lw3=4, \
                           vk4=[], vps4=[], clab4=None, clr4='0.5', lw4=3, \
                           vk5=[], vps5=[], clab5=None, clr5='g',   lw5=1, \
                           vk6=[], vps6=[], clab6=None, clr6='0.2', lw6=1.5 ):
    '''
    #------------------------------------------------------------------
    # Function that generates the comparison figure
    #
    # L_min, L_max : min and max wave-length for x-axis (km)
    #------------------------------------------------------------------
    '''
    #
    # r2Pi = 2.*nmp.pi # k is in rad/[space unit]
    r2Pi = 1. # k is in cycle/[space unit]

    # Font-related stuff...
    rat = 100./float(rDPI)
    params = { 'font.family':'Open Sans',
               'font.size':       int(14.*rat),
               'legend.fontsize': int(14.*rat),
               'xtick.labelsize': int(14.*rat),
               'ytick.labelsize': int(14.*rat),
               'axes.labelsize':  int(14.*rat),
               'legend.facecolor': 'white',
               'figure.facecolor': 'white' }
    mpl.rcParams.update(params)    
    font_inf  = { 'fontname':'Consolas', 'fontweight':'normal', 'fontsize':int(14.*rat) }
    
    # x-axis (lambda):
    k_min = r2Pi/L_max ; k_max = r2Pi/L_min
    xdef_l = nmp.asarray([ 4000., 2500., 1500., 1000., 700., 500., 300., 200., 150., 100., 70., 50., 40., 25., 15., 10., 7., 5., 4., 3., 2. ])
    (idx1,) = nmp.where(xdef_l>L_max) ; (idx2,) = nmp.where(xdef_l<L_min)
    xtcks_l = nmp.delete(xdef_l,nmp.concatenate((idx1,idx2)))
    cxtcks_l = []
    for rr in xtcks_l: cxtcks_l.append(str(int(rr)))
    xtcks_k  = r2Pi/xtcks_l

    fig = plt.figure(num = 1, figsize=(9.,9.), facecolor='w', edgecolor='k')
    ax  = plt.axes([0.1, 0.07, 0.875, 0.86])

    if len(vk3) > 1 and len(vps3) > 1:
        plt.plot(nmp.log10(vk3), nmp.log10(vps3), '-', color=clr3, linewidth=lw3, label=clab3, zorder=10)
    if len(vk2) > 1 and len(vps2) > 1:
        plt.plot(nmp.log10(vk2), nmp.log10(vps2), '-', color=clr2, linewidth=lw2, label=clab2, zorder=15)
    if len(vk4) > 1 and len(vps4) > 1:
        plt.plot(nmp.log10(vk4), nmp.log10(vps4), '-', color=clr4, linewidth=lw4, label=clab4, zorder=4)
    if len(vk5) > 1 and len(vps5) > 1:
        plt.plot(nmp.log10(vk5), nmp.log10(vps5), '-', color=clr5, linewidth=lw5, label=clab5, zorder=5)
    if len(vk6) > 1 and len(vps6) > 1:
        plt.plot(nmp.log10(vk6), nmp.log10(vps6), '-', color=clr6, linewidth=lw6, label=clab6, zorder=5)

    plt.plot(    nmp.log10(vk1), nmp.log10(vps1), '-', color=clr1, linewidth=lw1, label=clab1, zorder=5)

    nl = len(vk1)
    i1=int(0.53*float(nl)) ; i2=nl ; rfct = 3.
    if l_show_k2:
        plt.plot(nmp.log10(vk1[i1:i2]), nmp.log10((vk1[i1:i2]**-2.)/(rfct*1.E7)), '--', color='k', linewidth=2, label=r'k$^\mathregular{-2}$', zorder=2)
    if l_show_k4:
        plt.plot(nmp.log10(vk1[i1:i2]), nmp.log10((vk1[i1:i2]**-4.)/(rfct*3.E8)), '-', color='0.6', linewidth=2, label=r'k$^\mathregular{-4}$', zorder=1)
    if l_show_k5:
        plt.plot(nmp.log10(vk1[i1:i2]), nmp.log10((vk1[i1:i2]**-5.)/(rfct*2.E10)), '--', color='0.6', linewidth=2, label=r'k$^\mathregular{-5}$', zorder=2)
    if l_show_k11o3:
        plt.plot(nmp.log10(vk1[i1:i2]), nmp.log10((vk1[i1:i2]**(-11./3.))/(rfct*1.E9)), '-.', color='0.6', linewidth=2, label=r'k$^\mathregular{-11/3}$', zorder=2)
    #
    # Bottom X-axis:
    plt.xticks( nmp.log10(xtcks_k), cxtcks_l)
    ax.set_xlim(nmp.log10(k_min), nmp.log10(k_max))
    ax.grid(color='k', linestyle='-', linewidth=0.2)
    plt.xlabel('Wave-length [km]')
    #
    # Y-axis:
    ax.set_ylim(P_min_y,P_max_y)
    cytcks = []
    for ii in range(P_min_y,P_max_y+1): cytcks.append(r'$\mathregular{10^{'+str(ii)+'}}$')
    plt.yticks( nmp.arange(P_min_y,P_max_y+1,1) , nmp.asarray(cytcks))
    plt.ylabel(r'SSH PSD [$\mathregular{m^2}$/(cy/km)]', color='k')
    #
    if clab1 != None: plt.legend(loc='best', shadow=True, fancybox=True) ; #lulu
    #
    # Top X-axis:
    ax2 = ax.twiny()
    P_max_x = 1 ; P_min_x = -4
    cxtcks_k = []
    for ii in range(P_min_x,P_max_x+1): cxtcks_k.append(r'$\mathregular{10^{'+str(ii)+'}}$')
    plt.xticks( nmp.arange(P_min_x,P_max_x+1,1) , nmp.asarray(cxtcks_k))
    ax2.set_xlim(nmp.log10(k_min), nmp.log10(k_max))
    [t.set_color('0.3') for t in ax2.xaxis.get_ticklabels()]
    plt.xlabel('Wave-number [cy/km]', color='0.3')
    #
    if cinfo != '':
        ax2.annotate(cinfo, xy=(0.08, 0.13), xycoords='axes fraction',  \
                     bbox={'facecolor':'0.9', 'alpha':1., 'pad':10}, zorder=100, **font_inf)
    #
    plt.savefig(cfig_name, dpi=rDPI, facecolor='w', edgecolor='w', orientation='portrait', transparent=True)
    plt.close(1)
    return 0
