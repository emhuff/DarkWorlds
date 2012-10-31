
# ====================================================================
# Authors:
# Maria Elidaiana - mariaeli@cbpf.br
# Mandeep S. Gill - 
# Current July 7, 2011
# modified by JCY
# ====================================================================

"""Code for plotting ellipticity, shear maps, and other WL-related visualization"""
# Usage example : python simplestarplot.py "a611.starsOnStars.test.lhsChip.cat"
import sys
import pylab as plt
import numpy as np


def plotstars(x,y,e0_bef,e1_bef):
  scalefac=3000.0
  emag=np.sqrt(e0_bef**2+e1_bef**2)
  alpha=np.arctan2(e1_bef,e0_bef)/2.0
  delta_x=np.cos(alpha)*emag*scalefac
  delta_y=np.sin(alpha)*emag*scalefac
  for i in range(len(x)):
    plt.plot([x[i]-delta_x[i]/2,x[i]+delta_x[i]/2],[y[i]-delta_y[i]/2, y[i]+delta_y[i]/2], 'k')

def plotstars_s(x,y,e0_bef,e1_bef, scalefac):
  emag=np.sqrt(e0_bef**2+e1_bef**2)
  alpha=np.arctan2(e1_bef,e0_bef)/2.0
  delta_x=np.cos(alpha)*emag*scalefac
  delta_y=np.sin(alpha)*emag*scalefac
  for i in range(len(x)):
    plt.plot([x[i]-delta_x[i]/2,x[i]+delta_x[i]/2],[y[i]-delta_y[i]/2, y[i]+delta_y[i]/2], 'k')

def plotstars_color(x,y,e0_bef,e1_bef,color):
  scalefac=5000.0
  emag=np.sqrt(e0_bef**2+e1_bef**2)
  alpha=np.arctan2(e1_bef,e0_bef)/2.0
  delta_x=np.cos(alpha)*emag*scalefac
  delta_y=np.sin(alpha)*emag*scalefac
  for i in range(len(x)):
    plt.plot([x[i]-delta_x[i]/2,x[i]+delta_x[i]/2],[y[i]-delta_y[i]/2, y[i]+delta_y[i]/2], color)


def plot_field_galaxies(h1x,h1y,h2x,h2y,h3x,h3y, gx, gy, e1, e2, save, sky_num, name, ax):
  str_sky = str(sky_num)
  sky_p = sky_p = sky_num - 1
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_title('Sky '+ str_sky)
  if h1x[sky_p] > 0: 
    #    ax.plot(h1x[sky_p],h1y[sky_p],'r+', label = 'Halo One', markersize=10., markeredgewidth=5.)
    ax.plot(h1x[sky_p],h1y[sky_p],'r+', label = 'Halo One')
  if h2x[sky_p] > 0: 
    #    ax.plot(h2x[sky_p],h2y[sky_p],'rx', label = 'Halo Two', markersize=10., markeredgewidth=5.)
    ax.plot(h2x[sky_p],h2y[sky_p],'rx', label = 'Halo Two')
  if h3x[sky_p] > 0: 
    #    ax.plot(h3x[sky_p],h3y[sky_p],'r*', label = 'Halo Three', markersize = 10., markeredgewidth=5.)
    ax.plot(h3x[sky_p],h3y[sky_p],'r*', label = 'Halo Three')

  scale = 500
  plotstars_s(gx,gy,e1,e2, scale)
  box = ax.get_position()
  ax.set_position([box.x0, box.y0, box.width*0.8, box.height])
  leg = ax.legend( loc='center left', bbox_to_anchor= (1,0.5), prop={'size':10})
