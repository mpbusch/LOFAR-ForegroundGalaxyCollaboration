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
infile = 'M63_spix_rmscut.fits'
outfile = 'M63_magneticfield.fits' 
  rows,columns=infile.shape
  Bv=np.zeros_like(infile)
  K0=100 
  Ep=938.28                 #Mev or 1.5033*10**-3 erg 
  inclination=              #user input
  length=                   #user input? has to be assumed 
  frequency=                #user input
  #alpha defined in loop 
  #gamma defined in loop
  c1=6.26428e18             #erg**-2 s**-1 G**-1 
  #c2 defined in loop (we can make a function of this if wanted instead)
  c3=1.86558e(-23)          #erg G**-1 sterad**-1
  c4=(np.cos(inclination))**((gamma+1)/2)
  

def B_calc(infile): 
  for i in range(0,rows): 
    for j in range(0,columns):
      gamma= #UPDATE
      alpha= (gamma-1)/2    #this may be a special case only, synchrotron spectral index
      c2= .25*c3*(gamma+(7/3))/(gamma+1)*scipy.gamma((3*gamma-1)/12)*scipy.gamma((3*gamma+7)/12)
      Iv=infile[i,j] 
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
  image_data = hdu_list[0].data[:,:,0,0] # Check axis from hdu_list.info()
  print(type(image_data))
  print(image_data.shape()) # Check to make sure this makes sense. Can use np.swapaxes(array, indx, indx) if needed.
  
  
  



