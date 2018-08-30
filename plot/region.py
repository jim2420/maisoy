from mpl_toolkits.basemap import Basemap, cm, shiftgrid,interp
from netCDF4 import Dataset as NetCDFFile
import numpy as N
import matplotlib.pyplot as plt
import glob
import numpy.ma as ma
from scipy.interpolate import griddata
import matplotlib.colors as colors
area1=NetCDFFile('/global/project/projectdirs/m1602/datasets4.full/arbit_init_state_05x05.nc','r')
mask = area1.variables['REGION_MASK'][:,:]
lon = area1.variables['lon'][:]
lat = area1.variables['lat'][:]
mask,lon = shiftgrid(180.5,mask,lon,start=False)

fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(1, 1, 1)

map = Basemap(projection ='cyl', llcrnrlat=-62, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')
lon1,lat1 = N.meshgrid(lon,lat)
mask1=N.zeros((360,720))
x,y = map(lon1,lat1)
map.drawcoastlines()
map.drawcountries()
map.drawmapboundary()
for i in range(0,360):
	for j in range(0,720):
		if mask[i,j]==5.0:
			mask1[i,j]=4.0
		else:
                        mask1[i,j]=mask[i,j]

mask1= ma.masked_where(mask1<=0.0,mask1)
mask1= ma.masked_where(mask1>=10.0,mask1)
mask1= ma.masked_where(mask1==9.0,mask1)
mask1= ma.masked_where(mask1==6.0,mask1)
levels = [0, 1, 2, 3, 4, 5,6,7,8]
cmap2=colors.ListedColormap(['#7A944D', '#F7CD2B','gray', '#E45E39','#E33125','#DE3636','#702D70','#232963'])

cmap2.set_over('gray')
cmap2.set_under('green')
norm2 = colors.BoundaryNorm(levels, cmap2.N)

cs=plt.contourf(x, y, mask1,levels,cmap=cmap2,norm=norm2);
plt.axis('off')
#cbar = map.colorbar(cs,location='bottom',size="5%",pad="2%")
name=["North America","South America","European Union","Africa","China","South and Southeast Asia"]
name1=["(NA)","(SA)","(EU)","(AF)","(CHN)","(SSEA)"]

#ax.text(.0.8,.65,'{0}'.format(name[0]),fontsize=14,horizontalalignment='center',transform=ax.transAxes)
#ax.text(.12,.6,'{0}'.format(name1[0]),fontsize=14,horizontalalignment='center',transform=ax.transAxes)
plt.tight_layout()

plt.savefig('region.png')
plt.show()
