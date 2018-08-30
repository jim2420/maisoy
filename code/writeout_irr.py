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
dat5=NetCDFFile('mai1901_2015region_irr.nc','r')
nf = dat5.variables['i1y'][0,:]
dat1=NetCDFFile('mai1901_2015region.nc','r')
base = dat1.variables['i1y'][0,:]
basenf = dat1.variables['i2y'][0,:]

ee = dat1.variables['e1y'][0,:]
eenf = dat1.variables['e2y'][0,:]


N.savetxt('maiirr.csv',(nf,base,basenf,ee,eenf), delimiter=',')

