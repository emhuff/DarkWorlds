import sys
import os
import math
import numpy

def dark_matter_finder( x_galaxy, y_galaxy, e1, e2, x_halo, y_halo):
    """
    Function to calculate the Dark Matter signal around a proposed position
    Arguments :
    x_galaxy, y_galaxy: Vectors containing the x and y coordinate of each galaxy in the sky
    e1, e2: The 2 components of ellipticity for each galaxy in the sky
    x_halo, y_halo: The estimated coordinates of the halo
    Returns :
    signal : Scalar value of the total signal given the proposed halo
    """ 
        
        # Find out the angle each galaxy is at with respects to my guessed position of the halo
    angle_wrt_halo = arctan((y_galaxy-y_halo)/(x_galaxy-x_halo))
        
        # Calculate the total signal for a halo at my guessed position
    signal = sum( -(e1*np.cos(2.0*angle_wrt_halo) + \
                    e2*np.sin(2.0*angle_wrt_halo)) )
        
    return signal
    
#def main(argv):
if __name__ == "__main__":   
  """
  Main program to determine the position of a halo
  """
  # Read in the data from the Sky test file
  x_galaxy, y_galaxy, e1, e2 = loadtxt('../Data/Test_Sky1.csv', usecols=(1, 2, 3, 4),\
                                       skiprows=1, unpack=True)
 
  #I want to search the sky in a grid like fashion, so I want to split
  # the sky up and find the signal at each point in the grid
  Number_of_bins = 10
  Sky_size = 4200.0

  #It is square in all cases
  Binwidth = Sky_size/float(Number_of_bins)
  gridded_map= zeros([Number_of_bins, Number_of_bins], float)
  for i in xrange(Number_of_bins):
    for j in xrange(Number_of_bins):
      x_halo = i*binwidth # Proposed x position of the halo
      y_halo = j*binwidth # Proposed y position of the halo
 
      gridded_map[i,j] = dark_matter_finder(x_galaxy, y_galaxy, e1, e2,\
                                            x_halo, y_halo)
  estimated_x_position_halo=where(signal == max(gridded_map))[0][0]*binwidth
  estimated_y_position_halo=where(signal == max(gridded_map))[1][0]*binwidth
  
