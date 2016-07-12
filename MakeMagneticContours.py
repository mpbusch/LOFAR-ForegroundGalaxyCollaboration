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

__author__ = "Michael Busch and Trevor Van Engelhoven"
__license__ = "MIT License"
__version__ = "1.0.0"
__maintainer__ = "Michael Busch"
__email__ = "mpbusch@jhu.edu"
__status__ = "Production"

from astropy.io import fits
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy 


#### Global Constants ### 
# Please change as needed.
spix_infile = 'M63_spix_rmscut.fits'    # Change to spectral index map of your galaxy.
intensity_infile = 'M63_LOFAR_convolve2_cut_reorder_regrid.fits'  # Change to intensity map for your galaxy.
outfile = 'M63_magneticfield.fits' 
get_shape = fits.open(spix_infile)      # These commands are needed to correctly extract data from a .fits file
file_shape = get_shape[0].data[0,0,:,:] # Unpacking data from .fits file to determine shape.
rows,columns= file_shape.shape          # Determining number of columns and rows.
Bv=np.zeros_like(file_shape)            # Array of shape with same dimensions as data.
K0=100                                  # Proton-electron number density ration, 100 assumed for star forming regions.
Ep=938.28                               # Mev or 1.5033*10**-3 erg 
inclination=55                          # user input, change for each galaxy
l=                                      # l, user input? has to be assumed, 'pathlength'
v=131                                   # v, frequency in MHz, user input
#alpha defined in loop 
#gamma defined in loop
c1=6.26428e18                           #erg**-2 s**-1 G**-1 
#c2 defined in loop (we can make a function of this if wanted instead)
c3=1.86558e(-23)                        #erg G**-1 sterad**-1
c4=(np.cos(inclination))**((gamma+1)/2)
  

def B_calc(spix_infile, intensity_infile): 
  alpha_list = fits.open(spix_infile)
  intensity_list = fits.open(intensity_infile)
  for i in range(0,rows): 
    for j in range(0,columns):
      alpha=alpha_list[0].data[0,0,i,j]   #Spectral Index per pixel from Spectral Index Map
      gamma= 2*alpha + 1                  #I guess? Please check this.
      #alpha= (gamma-1)/2                 #This may be a special case only, synchrotron spectral index
      c2= .25*c3*(gamma+(7/3))/(gamma+1)*scipy.gamma((3*gamma-1)/12)*scipy.gamma((3*gamma+7)/12)
      Iv=intensity_list[0].data[0,0,i,j] #Intensity per pixel from Intensity Map
      Bv[i,j]=(4*np.pi*(2*alpha+1)*(K0+1)*Iv*Ep**(1-2*alpha)*(v/(2*c1))**alpha/((2*alpha-1)*c2*l*c4))**(1/(alpha+3))
  return Bv
      

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
  image_data = hdu_list[0].data[0,0,:,:] # Check axis from print_info()
  print(type(image_data))
  print(image_data.shape()) # Check to make sure this makes sense. Can use np.swapaxes(array, indx, indx) if needed
  
