#!/usr/bin/env python

'''
MakeMagneticContours.py: 
  This script will create a magnetic field map using 
  equipartition estimates from a spectral index fits 
  file. Please edit the global constants as needed.
  
  For more information about the magnetic field
  equipartition estimates, please consult the standard
  literature on the revised classical formula from:
  Beck and Krause 2005.
'''

__author__ = "Michael Busch"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Michael Busch"
__email__ = "mpbusch@asu.edu"
__status__ = "Production"

from astropy.io import fits
import numpy as np


#### Global Constants ### 
# Please change as needed.
infile = 'M63_spix_rmscut.fits'
outfile = 'M63_magneticfield.fits'



if __name__ == "__main__":
  data, header = fits.getdata(infile, header=True)
  



