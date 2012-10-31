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

import shearplots as splot
import shearcalc as scalc

####### Read in data files

start_sky = 1
end_sky = 20

for i in range(start_sky, end_sky):

    sky_num = i
    sky_p = sky_num - 1
    
    str_sky = str(sky_num)
    
    file_halo = '../Data/Training_halos.csv'
    nh, xr, yr, h1x, h1y, h2x, h2y, h3x, h3y = np.loadtxt(file_halo,delimiter=',',unpack=True,usecols=(1,2,3,4,5,6,7,8,9),skiprows=1)    
    
    file = '../Data/Train_Skies/Training_Sky'+str_sky+'.csv'
    x,y,e1,e2=np.loadtxt(file,delimiter=',',unpack=True,usecols=(1,2,3,4),skiprows=1)

    ############ ADD COLOR MAP
    Number_of_bins = 50
    Sky_size = 4200.0

    #It is square in all cases
    binwidth = Sky_size/float(Number_of_bins)
    gridded_map= np.zeros([Number_of_bins, Number_of_bins], float)

    dx = binwidth 
    xs = np.arange(0, Sky_size, dx)
    ys = np.arange(0, Sky_size, dx)
    X_h,Y_h = np.meshgrid(xs, ys)
    Z_ml = scalc.func3(X_h, Y_h)
    Z_sm = scalc.func3(X_h, Y_h)
    
    for i in xrange(Number_of_bins):
        for j in xrange(Number_of_bins):
            x_halo = i*binwidth # Proposed x position of the halo
            y_halo = j*binwidth # Proposed y position of the halo
            gridded_map[i,j] = scalc.dark_matter_finder_ml(x, y, e1, e2, x_halo, y_halo)
            Z_ml[i,j] = scalc.dark_matter_finder_ml(x, y, e1, e2, x_halo, y_halo)
            Z_sm[i,j] = scalc.dark_matter_finder_sm(x, y, e1, e2, x_halo, y_halo)
            
    name = '../Plots'
    save = 1
  
    ################ PLOT SKY FOR MAXIMUM LIKELIHOOD
    fig1 = plt.figure(1)       
    ax = fig1.add_subplot(111)
    splot.plot_field_galaxies(h1x,h1y,h2x,h2y,h3x,h3y, x, y, e1, e2, save, sky_num, name, ax)
    plt.pcolormesh(X_h, Y_h, Z_ml.T , cmap='BuPu')

    ################ PLOT SKY FOR SIGNAL MAP
    fig2 = plt.figure(2)       
    ax2 = fig2.add_subplot(111)
    splot.plot_field_galaxies(h1x,h1y,h2x,h2y,h3x,h3y, x, y, e1, e2, save, sky_num, name, ax2)
    plt.pcolormesh(X_h, Y_h, Z_sm.T , cmap='BuPu')

    plt.show()
    
    print raw_input("hold")
