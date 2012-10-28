
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
import pylab as pl
import numpy as np


def plotstars(x,y,e0_bef,e1_bef):
  scalefac=3000.0
  emag=np.sqrt(e0_bef**2+e1_bef**2)
  alpha=np.arctan2(e1_bef,e0_bef)/2.0
  delta_x=np.cos(alpha)*emag*scalefac
  delta_y=np.sin(alpha)*emag*scalefac
  for i in range(len(x)):
    pl.plot([x[i]-delta_x[i]/2,x[i]+delta_x[i]/2],[y[i]-delta_y[i]/2, y[i]+delta_y[i]/2], 'k')

def plotstars_s(x,y,e0_bef,e1_bef, scalefac):
  emag=np.sqrt(e0_bef**2+e1_bef**2)
  alpha=np.arctan2(e1_bef,e0_bef)/2.0
  delta_x=np.cos(alpha)*emag*scalefac
  delta_y=np.sin(alpha)*emag*scalefac
  for i in range(len(x)):
    pl.plot([x[i]-delta_x[i]/2,x[i]+delta_x[i]/2],[y[i]-delta_y[i]/2, y[i]+delta_y[i]/2], 'k')

def plotstars_color(x,y,e0_bef,e1_bef,color):
  scalefac=5000.0
  emag=np.sqrt(e0_bef**2+e1_bef**2)
  alpha=np.arctan2(e1_bef,e0_bef)/2.0
  delta_x=np.cos(alpha)*emag*scalefac
  delta_y=np.sin(alpha)*emag*scalefac
  for i in range(len(x)):
    pl.plot([x[i]-delta_x[i]/2,x[i]+delta_x[i]/2],[y[i]-delta_y[i]/2, y[i]+delta_y[i]/2], color)

