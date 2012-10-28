if __name__ == "__main__":
    from numpy import *
    import numpy.random
    import matplotlib.pyplot as plt
    from shearcalc import dark_matter_finder
    from shearplots import plotstars
    """
    Main program to determine the position of a halo
    """
  # Read in the data from the Sky test file
    x_galaxy, y_galaxy, e1, e2 = loadtxt('../Data/Test_Skies/Test_Sky1.csv', delimiter=",", usecols=(1, 2, 3, 4),skiprows=1, unpack=True)
 
  #I want to search the sky in a grid like fashion, so I want to split
  # the sky up and find the signal at each point in the grid
    Number_of_bins = 50
    Sky_size = 4200.0

  #It is square in all cases
    binwidth = Sky_size/float(Number_of_bins)
    gridded_map= zeros([Number_of_bins, Number_of_bins], float)
    for i in xrange(Number_of_bins):
        for j in xrange(Number_of_bins):
            x_halo = i*binwidth # Proposed x position of the halo
            y_halo = j*binwidth # Proposed y position of the halo
 
            gridded_map[i,j] = dark_matter_finder(x_galaxy, y_galaxy, e1, e2,\
                                            x_halo, y_halo)

    plotstars(x_galaxy,y_galaxy,e1,e2)
    plt.imshow(gridded_map.T,origin='lower')
    plt.colorbar()
    plt.show()
    
