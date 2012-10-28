def dark_matter_finder( x_galaxy, y_galaxy, e1, e2, x_halo, y_halo)
"""Function to calculate the Dark Matter signal around a proposed position
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
        signal = sum( -(e1*np.cos(2.0*angle_wrt_halo) + \ e2*np.sin(2.0*angle_wrt_halo)) )
        
        return signal