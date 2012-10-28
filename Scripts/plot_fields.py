#!/usr/bin/env python
# ====================================================================
# Authors:
# JCY
# Current Oct 28, 2012
# 
# ====================================================================


""" This code is designed to plot the fields given in the Dark Worlds
Kaggle competition"""

import sys
import os
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import jcy_simplestarplot as jcy
import csv
from matplotlib.font_manager import FontProperties
from shearcalc import dark_matter_finder

####### Read in data files
path = '/n/des/julia/DarkWorlds/'


start_sky = 101
end_sky = 121

for i in range(start_sky, end_sky):

    sky_num = i
    sky_p = sky_num - 1
    
    str_sky = str(sky_num)
    
    file_halo = '../Data/Training_halos.csv'
    nh, xr, yr, h1x, h1y, h2x, h2y, h3x, h3y = np.loadtxt(file_halo,delimiter=',',unpack=True,usecols=(1,2,3,4,5,6,7,8,9),skiprows=1)
    
    
    
    file = '../Data/Train_Skies/Training_Sky'+str_sky+'.csv'
    x,y,e1,e2=np.loadtxt(file,delimiter=',',unpack=True,usecols=(1,2,3,4),skiprows=1)


    ################ PLOT SKY
    fig1 = plt.figure(1)       
    ax = fig1.add_subplot(111)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Sky '+str_sky)
    if h1x[sky_p] > 0: 
        ax.plot(h1x[sky_p],h1y[sky_p],'r+', label = 'Halo One')
    if h2x[sky_p] > 0: 
        ax.plot(h2x[sky_p],h2y[sky_p],'rx', label = 'Halo Two')
    if h3x[sky_p] > 0: 
        ax.plot(h3x[sky_p],h3y[sky_p],'r*', label = 'Halo Three')
     
    scale = 500
    jcy.plotstars_s(x,y,e1,e2, scale)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width*0.8, box.height])
    leg = ax.legend( loc='center left', bbox_to_anchor= (1,0.5), prop={'size':10})
    #print x
  
    ############ ADD COLOR MAP
    Number_of_bins = 50
    Sky_size = 4200.0

  #It is square in all cases
    binwidth = Sky_size/float(Number_of_bins)
    gridded_map= np.zeros([Number_of_bins, Number_of_bins], float)
    for i in xrange(Number_of_bins):
        for j in xrange(Number_of_bins):
            x_halo = i*binwidth # Proposed x position of the halo
            y_halo = j*binwidth # Proposed y position of the halo
 
            gridded_map[i,j] = dark_matter_finder(x, y, e1, e2, x_halo, y_halo)

    fig2 = plt.figure(2)       

    plt.imshow(gridded_map.T,origin='lower')
    plt.colorbar()
    plt.show()

    print raw_input("hold")
