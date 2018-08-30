from mpl_toolkits.basemap import Basemap, cm, shiftgrid,interp,maskoceans
from netCDF4 import Dataset as NetCDFFile
import numpy as N
import matplotlib.pyplot as plt
import numpy.ma as ma
from statsmodels.stats.weightstats import DescrStatsW
import matplotlib.colors as colors

area=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/gridareahalf.nc','r')
gridarea = area.variables['cell_area'][:,:]

nclu=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/maize_AreaYieldProduction.nc','r')
ncvar_m = nclu.variables['maizeData'][0,0,:,:]
ncvar_y = nclu.variables['maizeData'][0,1,:,:]
ncvar_a = nclu.variables['maizeData'][0,4,:,:]
ncvar_p = nclu.variables['maizeData'][0,5,:,:]

nclu1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/soybean_AreaYieldProduction.nc','r')
ncvar_ms = nclu1.variables['soybeanData'][0,0,:,:]
ncvar_ys = nclu1.variables['soybeanData'][0,1,:,:]
ncvar_as = nclu1.variables['soybeanData'][0,4,:,:]
ncvar_ps = nclu1.variables['soybeanData'][0,5,:,:]

latm3 = nclu1.variables['latitude'][:]
lonm3 = nclu1.variables['longitude'][:]


region=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_mai_luh2.nc','r')
ma1h = region.variables['yield'][95:105,:,:]
#ma1 = region.variables['yield'][99,:,:]

region1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_soy_luh2.nc','r')
ma2h = region1.variables['yield'][95:105,:,:]


region=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_mai_luh2rcp85.nc','r')
ma1 = region.variables['yield'][75:85,:,:]
#ma1 = region.variables['yield'][99,:,:]

region1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_soy_luh2rcp85.nc','r')
ma2 = region1.variables['yield'][75:85,:,:]
#ma2 = region1.variables['yield'][99,:,:]

ma1=N.average(ma1,axis=0)
ma2=N.average(ma2,axis=0)
ma1h=N.average(ma1h,axis=0)
ma2h=N.average(ma2h,axis=0)

latmask = region.variables['lat'][:]
lonmask = region.variables['lon'][:]

latm3_new=N.flipud(latm3)
ncvar_m=N.flipud(ncvar_m)
ncvar_y=N.flipud(ncvar_y)
ncvar_a=N.flipud(ncvar_a)
ncvar_p=N.flipud(ncvar_p)

ncvar_ms=N.flipud(ncvar_ms)
ncvar_ys=N.flipud(ncvar_ys)
ncvar_as=N.flipud(ncvar_as)
ncvar_ps=N.flipud(ncvar_ps)

ncvar_m[N.isnan(ncvar_m)] = 0
ncvar_y[N.isnan(ncvar_y)] = 0
ncvar_a[N.isnan(ncvar_a)] = 0
ncvar_p[N.isnan(ncvar_p)] = 0

ncvar_ms[N.isnan(ncvar_ms)] = 0
ncvar_ys[N.isnan(ncvar_ys)] = 0
ncvar_as[N.isnan(ncvar_as)] = 0
ncvar_ps[N.isnan(ncvar_ps)] = 0


ncvar_m= ma.masked_where(ncvar_m<=0.0,ncvar_m)
ncvar_y= ma.masked_where(ncvar_y<=0.0,ncvar_y)
ncvar_a= ma.masked_where(ncvar_a<=0.0,ncvar_a)
ncvar_p= ma.masked_where(ncvar_p<=0.0,ncvar_p)

ncvar_m= ma.masked_where(ncvar_m>10**20,ncvar_m)
ncvar_y= ma.masked_where(ncvar_y>10**20,ncvar_y)
ncvar_a= ma.masked_where(ncvar_a>10**20,ncvar_a)
ncvar_p= ma.masked_where(ncvar_p>10**20,ncvar_p)

ncvar_ms= ma.masked_where(ncvar_ms<=0.0,ncvar_ms)
ncvar_ys= ma.masked_where(ncvar_ys<=0.0,ncvar_ys)
ncvar_as= ma.masked_where(ncvar_as<=0.0,ncvar_as)
ncvar_ps= ma.masked_where(ncvar_ps<=0.0,ncvar_ps)

ncvar_ms= ma.masked_where(ncvar_ms>10**20,ncvar_ms)
ncvar_ys= ma.masked_where(ncvar_ys>10**20,ncvar_ys)
ncvar_as= ma.masked_where(ncvar_as>10**20,ncvar_as)
ncvar_ps= ma.masked_where(ncvar_ps>10**20,ncvar_ps)


ncvar_m=ma.filled(ncvar_m, fill_value=0.)
ncvar_y=ma.filled(ncvar_y, fill_value=0.)
ncvar_a=ma.filled(ncvar_a, fill_value=0.)
ncvar_p=ma.filled(ncvar_p, fill_value=0.)

ncvar_ms=ma.filled(ncvar_ms, fill_value=0.)
ncvar_ys=ma.filled(ncvar_ys, fill_value=0.)
ncvar_as=ma.filled(ncvar_as, fill_value=0.)
ncvar_ps=ma.filled(ncvar_ps, fill_value=0.)

ma1h= ma.masked_where(ma1h<=0,ma1h)
ma2h= ma.masked_where(ma2h<=0,ma2h)
ma1h= ma.masked_where(ma1<=0,ma1h)
ma2h= ma.masked_where(ma2<=0,ma2h)
ma1= ma.masked_where(ma1h<=0,ma1)
ma2= ma.masked_where(ma2h<=0,ma2)


lon,lat = N.meshgrid(lonmask,latmask)
lon1,lat1 = N.meshgrid(lonm3,latm3_new)


m3newy=N.zeros((360,720))
m3newp=N.zeros((360,720))
m3newa=N.zeros((360,720))
m3newm=N.zeros((360,720))

m3newys=N.zeros((360,720))
m3newps=N.zeros((360,720))
m3newas=N.zeros((360,720))
m3newms=N.zeros((360,720))

cmap = plt.cm.terrain_r
#bounds=[-0.1,0.0,0.01,0.05,0.1,0.5,1,2,3,4,5,6]
bounds=[-0.1,0.0,1,2,4,6,8,10,12,14,16]

norm = colors.BoundaryNorm(bounds, cmap.N)

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(221)

ax1 = fig.add_subplot(222)
ax1.set_title("Maize ISAM (t grains / ha gridarea)",fontsize=20)
map = Basemap(projection ='cyl', llcrnrlat=-62, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')
x,y = map(lon,lat)

ma1= ma.masked_where(ma1[:,:]<=0.0,ma1)

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary()
#ncvar_y=maskoceans(x1,y1,ncvar_y)
cs1 = map.pcolormesh(x,y,ma1,cmap=cmap,norm=norm)
#cs1 = map.pcolormesh(x,y,ma1,cmap=plt.cm.gist_earth,vmin=0,vmax=10)

plt.axis('off')
cbar = map.colorbar(cs1,location='bottom',size="5%",pad="2%",ticks=bounds,extend='max')
cbar.ax.tick_params(labelsize=16)
#cbar.ax.set_xticklabels(['0', '0.01', '0.05','0.1','0.5','1','2','3','4','5','6'])  # horizontal colorbar

#bounds=[-0.1,0.0,0.03,0.06,0.09,0.12,0.15,0.2,0.3,0.4,0.5,0.6,0.7]

norm = colors.BoundaryNorm(bounds, cmap.N)
bounds=[-0.1,0.0,0.1,0.5,1,1.5,2,2.5,3,3.5,4,4.5]

#bounds=[0,0.01,0.05,0.1,0.5,1,1.5,2]
norm = colors.BoundaryNorm(bounds, cmap.N)

ax1 = fig.add_subplot(224)
ax1.set_title("Soybean ISAM (t grains / ha gridarea)",fontsize=20)
map = Basemap(projection ='cyl', llcrnrlat=-62, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')

ma2= ma.masked_where(ma2[:,:]<=0.0,ma2)

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary()
#ncvar_y=maskoceans(x1,y1,ncvar_y)
cs1 = map.pcolormesh(x,y,ma2,cmap=cmap,norm=norm)
#cs1 = map.pcolormesh(x,y,ma2,cmap=plt.cm.gist_earth,vmin=0,vmax=5)
plt.axis('off')
cbar = map.colorbar(cs1,location='bottom',size="5%",pad="2%",ticks=bounds,extend='max')
cbar.ax.tick_params(labelsize=16)

plt.savefig('isam_maisoy2090srcp85.jpg',bbox_inches='tight')

plt.show()


