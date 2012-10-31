# ===========================================================================
# This module contains code meant to do shear calculations for the DarkWorlds
#  Kaggle competition.
#
#
# ===========================================================================
import numpy as np

def dark_matter_finder_sm( x_galaxy, y_galaxy, e1, e2, x_halo, y_halo):
    """
    Signal Map
    
    Function to calculate the Dark Matter signal around a proposed position
    Arguments :
    x_galaxy, y_galaxy: Vectors containing the x and y coordinate of each galaxy in the sky
    e1, e2: The 2 components of ellipticity for each galaxy in the sky
    x_halo, y_halo: The estimated coordinates of the halo
    Returns :
    signal : Scalar value of the total signal given the proposed halo
    """ 
        
        # Find out the angle each galaxy is at with respects to my guessed position of the halo
    angle_wrt_halo = np.arctan((y_galaxy-y_halo)/(x_galaxy-x_halo))
        
        # Calculate the total signal for a halo at my guessed position
    signal = sum( -(e1*np.cos(2.0*angle_wrt_halo) + \
                    e2*np.sin(2.0*angle_wrt_halo)) )
        
    return signal

def dark_matter_finder_ml( x_galaxy, y_galaxy, e1, e2, x_halo, y_halo) :
  """Function to calculate the likelihood of a dark matter halo given a proposed position
  Arguments:
    x_galaxy, y_galaxy: Vectors containing the x and y coordinate of each galaxy in the sky
    e1, e2: The 2 components of ellipticity for each galaxy in the sky
    x_halo, y_halo: The estimated coordinates of the halo
  Returns :
    likelihood : Scalar value of the likelihood given the proposed halo
   """
 
  # Find out the radial distance and angle each galaxy is at with respects to my guessed position of the halo
  radial_distance_galaxy_from_halo = np.sqrt( (x_galaxy-x_halo)**2 + (y_galaxy-y_halo)**2 )
  angle_wrt_halo = np.arctan((y_galaxy-y_halo)/(x_galaxy-x_halo))
 
  #We assume that the ellipticity caused by this is 1/r
  total_ellipticity = 1.0/radial_distance_galaxy_from_halo
 
  #Then convert this into the two components of ellipticity, e1 and e2
  e1_model = total_ellipticity*np.cos(2.0*angle_wrt_halo)
  e2_model = total_ellipticity*np.sin(2.0*angle_wrt_halo)
 
  #Now work out the chi-square fit of the model with compared to the data
  chi_square_fit = sum( (e1_model - e1)**2 + (e2_model - e2)**2 )
 
  #Convert to likelihood
  likelihood = np.exp((-chi_square_fit/2.0))
 
  return likelihood    



def func3(x,y):
    return (1- x/2 + x**5 + y**3)*np.exp(-x**2-y**2)



def dark_matter_finder_matched( x_galaxy, y_galaxy, e1, e2, x_halo, y_halo) :
  """Function to calculate the likelihood of a dark matter halo given a proposed position
  Arguments:
    x_galaxy, y_galaxy: Vectors containing the x and y coordinate of each galaxy in the sky
    e1, e2: The 2 components of ellipticity for each galaxy in the sky
    x_halo, y_halo: The estimated coordinates of the halo
  Returns :
    likelihood : Scalar value of the likelihood given the proposed halo
   """
 
  # Find out the radial distance and angle each galaxy is at with respects to my guessed position of the halo
  radial_distance_galaxy_from_halo = np.sqrt( (x_galaxy-x_halo)**2 + (y_galaxy-y_halo)**2 )
  angle_wrt_halo = np.arctan((y_galaxy-y_halo)/(x_galaxy-x_halo))
 
  #We assume that the ellipticity caused by this is 1/r
  total_ellipticity = 1.0/radial_distance_galaxy_from_halo
 
  #Then convert this into the two components of ellipticity, e1 and e2

  filter = 1./(1. + radial_distance_galaxy_from_halo / 235.16283004 )
  e1_filter=-1.*filter*np.cos(2.*angle_wrt_halo)
  e2_filter=-1.*filter*np.sin(2.*angle_wrt_halo)

  mass = sum(e1_filter*e1 + e2_filter*e2)
 
  #Now work out the chi-square fit of the model with compared to the data
 
  #Convert to likelihood
  
 
  return mass
