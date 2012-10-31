#!/usr/bin/env python
# ====================================================================

"""
 This code will calculate the average tangential shear profile for
 a range of DarkWorlds test fields.

 It now also fits a shear profile of the form A/(1+r/r0) to the average
 tangential shear profile.
"""

# ====================================================================




import sys
import os
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv
from matplotlib.font_manager import FontProperties
from scipy.optimize import minimize

import shearplots as splot
import shearcalc as scalc

######## This is the range of example skies that we will use.
start_sky = 1
end_sky = 100


######## These are the arrays which will hold the tangential shear statistics
nbins = 25
Sky_size = 4200.0
bin_width = Sky_size/nbins
bin_edges = np.arange(nbins+1)*bin_width
bin_centers = np.arange(nbins)*bin_width + bin_width/2.
shear_array = np.zeros(nbins)
count_array = np.zeros(nbins)
single_shear_array = np.zeros(nbins)
single_count_array = np.zeros(nbins)

fig1 = plt.figure(1)
ax = fig1.add_subplot(111)
ax.set_yscale('log')
ax.set_xscale('log')


for i in range(start_sky, end_sky):
    str_sky = str(i+1)
    file_halo = '../Data/Training_halos.csv'
    nh, xr, yr, h1x, h1y, h2x, h2y, h3x, h3y = np.loadtxt(file_halo,delimiter=',',unpack=True,usecols=(1,2,3,4,5,6,7,8,9),skiprows=1)    
    
    file = '../Data/Train_Skies/Training_Sky'+str_sky+'.csv'
    x,y,e1,e2=np.loadtxt(file,delimiter=',',unpack=True,usecols=(1,2,3,4),skiprows=1)
    
    radial_distance_galaxy_from_halo = np.sqrt( (x-h1x[i])**2 + (y-h1y[i])**2 )

    for bin_index in range(0,nbins):
        b1 = (radial_distance_galaxy_from_halo >= bin_edges[bin_index])
        b2 = (radial_distance_galaxy_from_halo < bin_edges[bin_index+1])
        these = b1*b2
        #        print np.average(x[these]), np.min(x[these]), np.max(x[these]), bin_edges[bin_index], bin_edges[bin_index+1]
        shear_array[bin_index] += scalc.dark_matter_finder_sm(x[these],y[these],e1[these],e2[these],h1x[i],h1y[i])
        count_array[bin_index] += len(x[these])
        #        single_shear_array[bin_index]  = scalc.dark_matter_finder_sm(x[these],y[these],e1[these],e2[these],h1x[i],h1y[i])
        #        single_count_array[bin_index] = len(x[these])
        #        single_shear_profile = single_shear_array/(single_count_array+0.0001)
        #        plt.plot(bin_centers,single_shear_profile,".")

        
shear_profile = shear_array/(count_array+0.0001)
err = 0.3/np.sqrt(count_array+.0001)

def stacked_log_likelihood(pars):
    A = pars[0]
    r0 = pars[1]
    profile = A/(1+bin_centers/r0)
    log_likelihood = sum((shear_profile-profile)**2/err**2)/2.

    return(log_likelihood)



initial_guess= np.array([0.3,300])
outpars = minimize(stacked_log_likelihood,initial_guess,method="nelder-mead", options = {'xtol':1e-6, 'disp':True})

print "Final parameters are: "+str(outpars.x)
#plt.plot(bin_centers,shear_profile,"r")
plt.errorbar(bin_centers,shear_profile,yerr=err,fmt="r.")
plt.plot(bin_centers,outpars.x[0]/(1+bin_centers/outpars.x[1]),"b")
ax.set_ylim(-0.1,0.6)
plt.savefig("../Plots/fit_to_avg_shear_profile."+str(start_sky)+"."+str(end_sky)+".pdf")
