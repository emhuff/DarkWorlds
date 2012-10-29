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
import shearplots as splot

####### Read in data files

start_sky = 201
end_sky = 221

for i in range(start_sky, end_sky):

    sky_num = i
    sky_p = sky_num - 1
    
    str_sky = str(sky_num)
    
    file_halo = '../Data/Training_halos.csv'
    nh, xr, yr, h1x, h1y, h2x, h2y, h3x, h3y = np.loadtxt(file_halo,delimiter=',',unpack=True,usecols=(1,2,3,4,5,6,7,8,9),skiprows=1)
    
    
    
    file = '../Data/Train_Skies/Training_Sky'+str_sky+'.csv'
    x,y,e1,e2=np.loadtxt(file,delimiter=',',unpack=True,usecols=(1,2,3,4),skiprows=1)



    name = '../Plots'
    save = 1
    
    ################ PLOT SKY
    splot.plot_field_galaxies(h1x,h1y,h2x,h2y,h3x,h3y, x, y, e1, e2, save, sky_num, name)
    
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

    plt.imshow(gridded_map.T,origin='lower', cmap='BuPu')
    plt.colorbar()
    plt.show()

    print raw_input("hold")
