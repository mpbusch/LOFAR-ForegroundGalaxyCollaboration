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
__email__ = "mpbusch@jhu.edu"
__status__ = "Production"

from astropy.io import fits
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


#### Global Constants ### 
# Please change as needed.
infile = 'M63_spix_rmscut.fits'
outfile = 'M63_magneticfield.fits'

def plot_data(data):
  ''' Plots Fits Data for simple inspection '''
  plt.imshow(data)
  plt.title('Image Data')
  plt.colorbar()
  plt.show()
  
def print_info(infile):
  hdu_list = fits.open(infile)
  hdu_list.info()
  return print(hdu_list.info())

if __name__ == "__main__":
  image_data = hdu_list[0].data[:,:,0,0] # Check axis from hdu_list.info()
  print(type(image_data))
  print(image_data.shape()) # Check to make sure this makes sense. Can use np.swapaxes(array, indx, indx) if needed.
  
  
  



