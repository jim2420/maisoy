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
dat5=NetCDFFile('soy1901_2015regionNF.nc','r')
nf = dat5.variables['i1y'][0,:]
dat1=NetCDFFile('soy1901_2015region.nc','r')
base = dat1.variables['i1y'][0,:]
basenf = dat1.variables['i3y'][0,:]

ee = dat1.variables['e1y'][0,:]
eenf = dat1.variables['e3y'][0,:]


N.savetxt('soyfert.csv',(nf,base,basenf,ee,eenf), delimiter=',')

