from mpl_toolkits.basemap import Basemap, cm, shiftgrid,interp
from netCDF4 import Dataset as NetCDFFile
import numpy as N
import matplotlib.pyplot as plt
import glob
import numpy.ma as ma
from scipy.interpolate import griddata
import matplotlib.colors as colors
from matplotlib.dates import DateFormatter
import datetime




dat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/soy1901_2015regionNF.nc','r')


for i in range(1,2):

        locals()['i{0}p'.format(i)] = dat.variables['i{0}p'.format(i)][:,:]
        locals()['i{0}y'.format(i)] = dat.variables['i{0}y'.format(i)][:,:]
        locals()['i{0}g'.format(i)] = dat.variables['i{0}g'.format(i)][:,:]

#N.savetxt('soynfh45.csv', (i1p[0,85],i1p[1,85],i1p[2,85],i1p[3,85],i1p[4,85],i1p[7,85],i1p[8,85]), delimiter=',')
#N.savetxt('soynfharea45.csv', (i1g[0,85],i1g[1,85],i1g[2,85],i1g[3,85],i1g[4,85],i1g[7,85],i1g[8,85]), delimiter=',')
N.savetxt('soynfhg.csv', (i1p[0,:]), delimiter=',')
N.savetxt('soynfhareag.csv', (i1g[0,:]), delimiter=',')


