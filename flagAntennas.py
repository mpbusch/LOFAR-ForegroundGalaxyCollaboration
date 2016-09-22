# This short program should be run in CASA, in the directory filled with .ms files you wish to flag.
# Feel free to change the 'antenna' parameter in flagdata to flag whichever antennas are giving you trouble.
# Author: Michael Busch

from glob import glob

vislist = glob.glob("*.ms")

for visibility in vislist:
	flagdata(vis=visibility, antenna=[ [RS508HBA, RS509HBA], [RS208HBA, RS509HBA], [CS302HBA0], [RS205HBA] ], mode='manual')

print "Finished flagging measurement sets. Enjoy!"
