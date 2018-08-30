from mpl_toolkits.basemap import Basemap, cm, shiftgrid,interp,maskoceans
from netCDF4 import Dataset as NetCDFFile
import numpy as N
import matplotlib.pyplot as plt
import numpy.ma as ma
from statsmodels.stats.weightstats import DescrStatsW
import matplotlib.colors as colors
region=NetCDFFile('/global/project/projectdirs/m1602/datasets4.full/arbit_init_state_05x05.nc','r')
ind = region.variables['REGION_MASK'][:,:]
lonisam1=region.variables['lon'][:]
ind,lona11=shiftgrid(180.5,ind,lonisam1,start=False)

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



#region=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/mai_irr_fert/output/mai_irr_fert.nc','r')
region=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/maiequilibrium/output/maiequilibrium.nc','r')

ma1 = region.variables['totalyield'][95:105,:,:]#1996-2005
#ma1 = region.variables['yield'][99,:,:]

#region1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/soy_irr_fert/output/soy_irr_fert.nc','r')
region1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/soyequilibrium/output/soyequilibrium.nc','r')

ma2 = region1.variables['totalyield'][95:105,:,:]
#ma2 = region1.variables['yield'][99,:,:]

isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/luh2area_850_2015_corrcrop.nc','r')
meareaisam = isam1.variables['fmai_tt'][1146:1156,:,:]#1980-2009
meareaisam= ma.masked_where(meareaisam<=0.0,meareaisam)
#ma1=ma1*meareaisam

isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/luh2area_850_2015_corrcrop.nc','r')
meareaisam1 = isam1.variables['fsoy_tt'][1146:1156,:,:]#1980-2009
meareaisam1= ma.masked_where(meareaisam1<=0.0,meareaisam1)
#ma2=ma2*meareaisam1


ma1=N.average(ma1,axis=0)
ma2=N.average(ma2,axis=0)

isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/m3_mai.nc','r')
m31 = isam1.variables['m3area'][:,:]
isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/m3_soy.nc','r')
m32 = isam1.variables['m3area'][:,:]


ma1,lona11=shiftgrid(180.5,ma1,lonisam1,start=False)
ma2,lona11=shiftgrid(180.5,ma2,lonisam1,start=False)

ma1= ma.masked_where(m31<=0.0,ma1)
ma2= ma.masked_where(m32<=0.0,ma2)

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



lon,lat = N.meshgrid(lonmask,latmask)
lon1,lat1 = N.meshgrid(lonm3,latm3_new)




#ma1= ma.masked_where(ind!=8.0,ma1)
#ma2= ma.masked_where(ind!=8.0,ma2)

cmap = plt.cm.terrain_r
#bounds=[-0.1,0.0,0.01,0.05,0.1,0.5,1,2,3,4,5,6]
bounds=[-0.1,0.0,1,2,4,6,8,10,12,14,16]

norm = colors.BoundaryNorm(bounds, cmap.N)

fig = plt.figure(figsize=(20,10))

ax1 = fig.add_subplot(222)
#ax1.set_title("Maize ISAM (t grains / ha cropland)",fontsize=20)
map = Basemap(projection ='cyl', llcrnrlat=-62, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')
#map = Basemap(projection ='cyl', llcrnrlat=-15, urcrnrlat=40,llcrnrlon=55, urcrnrlon=145, resolution='c')
x,y = map(lona11,lat)

ma1= ma.masked_where(ma1<=0.0,ma1)

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary()
#ncvar_y=maskoceans(x1,y1,ncvar_y)
gk=(1/meareaisam*gridarea/10000)
a1=ma1/gridarea*10000
cs1 = map.pcolormesh(x,y,ma1,cmap=cmap,norm=norm)
#cs1 = map.pcolormesh(x,y,ma1,cmap=plt.cm.gist_earth,vmin=0,vmax=10)

plt.axis('off')
cbar = map.colorbar(cs1,location='bottom',size="5%",pad="2%",ticks=bounds,extend='max')
cbar.ax.tick_params(labelsize=16)
#cbar.ax.set_xticklabels(['0', '0.01', '0.05','0.1','0.5','1','2','3','4','5','6'])  # horizontal colorbar

#bounds=[-0.1,0.0,0.03,0.06,0.09,0.12,0.15,0.2,0.3,0.4,0.5,0.6,0.7]
bounds=[-0.1,0.0,0.1,0.5,1,1.5,2,2.5,3,3.5,4,4.5]

norm = colors.BoundaryNorm(bounds, cmap.N)

#bounds=[0,0.01,0.05,0.1,0.5,1,1.5,2]
norm = colors.BoundaryNorm(bounds, cmap.N)


ax1 = fig.add_subplot(224)
#ax1.set_title("Soybean ISAM (t grains / ha cropland)",fontsize=20)
map = Basemap(projection ='cyl', llcrnrlat=-62, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')
#map = Basemap(projection ='cyl', llcrnrlat=-15, urcrnrlat=40,llcrnrlon=55, urcrnrlon=145, resolution='c')

ma2= ma.masked_where(ma2[:,:]<=0.0,ma2)

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary()
#ncvar_y=maskoceans(x1,y1,ncvar_y)
gg=(1/meareaisam1*gridarea/10000)
a2=ma2/gridarea*10000*gg
cs1 = map.pcolormesh(x,y,ma2,cmap=cmap,norm=norm)
#cs1 = map.pcolormesh(x,y,ma2,cmap=plt.cm.gist_earth,vmin=0,vmax=5)
plt.axis('off')
cbar = map.colorbar(cs1,location='bottom',size="5%",pad="2%",ticks=bounds,extend='max')
cbar.ax.tick_params(labelsize=16)

plt.savefig('isam_m3_maisoybaseyieldequ.jpg',bbox_inches='tight')

plt.show()


