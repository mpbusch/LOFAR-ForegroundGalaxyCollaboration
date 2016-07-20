 
 
 def Flux(infile,degrees,bin_size): 
  deg= degrees    #User input: degrees to rotate image so that the galaxy is horizontal 
  bin= bin_size   #User input: the rows divided by bin equals the bin size
  infile=infile.rotate(deg) 
  out=np.zeros(int(rows/bin))
  rows,columns=infile.shape 
  for k in range(len(int(rows/bin)))        #iterating over each bin 
    for i in range(len(int(rows/bin))):     #iterating over rows in the bin 
      for j in range(len(columns)):         #iterating over columns
        out[k]=out[k]+infile[i+(k*int(rows/bin)),j] 
        
  return out
      
      
      
  
