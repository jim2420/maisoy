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



region=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/mai_irr_fert/output/mai_irr_fert.nc','r')
ma1 = region.variables['totalyield'][95:105,:,:]#1996-2005

region1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/soy_irr_fert/output/soy_irr_fert.nc','r')
ma2 = region1.variables['totalyield'][95:105,:,:]

region=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/fixedirr/mai_irr_fert/output/mai_irr_fert.nc','r')
ma1i = region.variables['totalyield'][75:85,:,:]#2090-2099

region1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/fixedirr/soy_irr_fert/output/soy_irr_fert.nc','r')
ma2i = region1.variables['totalyield'][75:85,:,:]



isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/luh2area_850_2015_corrcrop.nc','r')
meareaisam = N.average(isam1.variables['fmai_tt'][1146:1156,:,:])#1980-2009
meareaisam= ma.masked_where(meareaisam<=0.0,meareaisam)
meareaisama=N.zeros((10,360,720))
for i in range(0,10):
	meareaisama[i,:,:]=meareaisam
ma1=ma1*meareaisama

isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/luh2area_rcp85_corrcrop.nc','r')
meareaisami = isam1.variables['fmai_tt'][75:85,:,:]#2090-2099
meareaisami= ma.masked_where(meareaisami<=0.0,meareaisami)

ma1i=ma1i*meareaisama

isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/luh2area_850_2015_corrcrop.nc','r')
meareaisam1 = N.average(isam1.variables['fsoy_tt'][1146:1156,:,:])#1980-2009
meareaisam1= ma.masked_where(meareaisam1<=0.0,meareaisam1)
meareaisamb=N.zeros((10,360,720))
for i in range(0,10):
        meareaisamb[i,:,:]=meareaisam1


ma2=ma2*meareaisamb

isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/luh2area_rcp85_corrcrop.nc','r')
meareaisam1i = isam1.variables['fsoy_tt'][75:85,:,:]#2090-2099
meareaisam1i= ma.masked_where(meareaisam1i<=0.0,meareaisam1i)


ma2i=ma2i*meareaisamb



ma1=N.average(ma1,axis=0)
ma2=N.average(ma2,axis=0)
ma1i=N.average(ma1i,axis=0)
ma2i=N.average(ma2i,axis=0)






isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/m3_mai.nc','r')
m31 = isam1.variables['m3area'][:,:]
isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/m3_soy.nc','r')
m32 = isam1.variables['m3area'][:,:]


ma1,lona11=shiftgrid(180.5,ma1,lonisam1,start=False)
ma2,lona11=shiftgrid(180.5,ma2,lonisam1,start=False)
ma1i,lona11=shiftgrid(180.5,ma1i,lonisam1,start=False)
ma2i,lona11=shiftgrid(180.5,ma2i,lonisam1,start=False)


ma1= ma.masked_where(m31<=0.0,ma1)
ma2= ma.masked_where(m32<=0.0,ma2)

ma1i= ma.masked_where(m31<=0.0,ma1i)
ma2i= ma.masked_where(m32<=0.0,ma2i)



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

#ma1i= ma.masked_where(ind!=8.0,ma1i)
#ma2i= ma.masked_where(ind!=8.0,ma2i)






cmap = plt.cm.bwr
bounds=[-120,-100,-80,-60,-40,-20,0,20,40,60,80,100,120]

norm = colors.BoundaryNorm(bounds, cmap.N)

fig = plt.figure(figsize=(20,15))

ax1 = fig.add_subplot(211)
map = Basemap(projection ='cyl', llcrnrlat=-62, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')
#map = Basemap(projection ='cyl', llcrnrlat=-15, urcrnrlat=40,llcrnrlon=55, urcrnrlon=145, resolution='c')
x,y = map(lona11,lat)

aa=((ma1i/gridarea*10000)-(ma1/gridarea*10000))/(ma1/gridarea*10000)*100
aa= ma.masked_where(aa==0.0,aa)

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary()
cs1 = map.pcolormesh(x,y,aa,cmap=cmap,norm=norm)

plt.axis('off')
cbar = map.colorbar(cs1,location='bottom',size="5%",pad="2%",ticks=bounds,extend='both')
cbar.ax.tick_params(labelsize=16)



ax1 = fig.add_subplot(212)
map = Basemap(projection ='cyl', llcrnrlat=-62, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')
#map = Basemap(projection ='cyl', llcrnrlat=-15, urcrnrlat=40,llcrnrlon=55, urcrnrlon=145, resolution='c')
bb=((ma2i/gridarea*10000)-(ma2/gridarea*10000))/(ma2/gridarea*10000)*100
bb= ma.masked_where(bb==0.0,bb)

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary()
cs1 = map.pcolormesh(x,y,bb,cmap=cmap,norm=norm)
#cs1 = map.pcolormesh(x,y,ma2,cmap=plt.cm.gist_earth,vmin=0,vmax=5)
plt.axis('off')
cbar = map.colorbar(cs1,location='bottom',size="5%",pad="2%",ticks=bounds,extend='both')
cbar.ax.tick_params(labelsize=16)


plt.savefig('isamdiffbase_maisoy85_2090fixedlug.jpg',bbox_inches='tight')

plt.show()


