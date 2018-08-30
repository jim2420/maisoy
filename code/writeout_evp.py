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
dat5=NetCDFFile('soy1901_2015region_evp.nc','r')
for i in range(1,6):
        locals()['i{0}y1'.format(i)]=N.zeros((115))
        locals()['i{0}y1'.format(i)]=dat5.variables['i{0}y'.format(i)][0,:]

        locals()['ei{0}y1'.format(i)]=N.zeros((115))
        locals()['ei{0}y1'.format(i)]=dat5.variables['e{0}y'.format(i)][0,:]

dat1=NetCDFFile('soy1901_2015region.nc','r')

for i in range(1,6):
        locals()['ai{0}y1'.format(i)]=N.zeros((115))
        locals()['ai{0}y1'.format(i)]=dat1.variables['i{0}y'.format(i)][0,:]

        locals()['aei{0}y1'.format(i)]=N.zeros((115))
        locals()['aei{0}y1'.format(i)]=dat1.variables['e{0}y'.format(i)][0,:]


for i in range(1,6):
        locals()['a{0}'.format(i)]=N.zeros((115))
        locals()['a{0}'.format(i)]=(locals()['ai{0}y1'.format(i)])/(locals()['i{0}y1'.format(i)])
        locals()['ea{0}'.format(i)]=N.zeros((115))
        locals()['ea{0}'.format(i)]=(locals()['aei{0}y1'.format(i)])/(locals()['ei{0}y1'.format(i)])


N.savetxt('soyevp.csv',(a1,a4,a5,a2,a3,ea1,ea4,ea5,ea2,ea3), delimiter=',')

