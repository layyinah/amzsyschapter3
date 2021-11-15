import sys
import zipfile

from zipfile import *

def zipp(z1,z2):
    z=zipfile(z1,'w')
    for i in z2:
        z.zipfile(i,'w')
    print(z)
zipp(sys.argv[1,sys.argv[2:]])

