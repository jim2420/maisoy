from mpl_toolkits.basemap import Basemap, cm, shiftgrid,interp
from netCDF4 import Dataset as NetCDFFile
import numpy as N
import matplotlib.pyplot as plt
import glob
import numpy.ma as ma
from scipy.interpolate import griddata
import matplotlib.colors as colors
from statsmodels.stats.weightstats import DescrStatsW
from scipy.stats import ttest_ind
from matplotlib.markers import TICKDOWN
import matplotlib.patches as mpatches

area=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/gridareahalf_isam.nc','r')
gridarea = area.variables['cell_area'][:,:]
gridlon = area.variables['lon'][:]
gridlat=area.variables['lat'][:]
gridarea,gridlon1 = shiftgrid(180.5,gridarea,gridlon,start=False)
#print gridlon
nclu=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/m3yield_isam.nc','r')
ncvar_maize = nclu.variables['maize_total'][0,:,:]
ncvar_soy = nclu.variables['soy_total'][0,:,:]
areamaize = nclu.variables['maize_area'][0,:,:]
areasoy = nclu.variables['soy_area'][0,:,:]


latnc = nclu.variables['lat'][:]
lonnc = nclu.variables['lon'][:]
ncvar_maize,gridlon1 = shiftgrid(180.5,ncvar_maize,gridlon,start=False)
ncvar_soy,gridlon1 = shiftgrid(180.5,ncvar_soy,gridlon,start=False)

areamaize,gridlon1 = shiftgrid(180.5,areamaize,gridlon,start=False)
areasoy,gridlon1 = shiftgrid(180.5,areasoy,gridlon,start=False)



region1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_mai_luh2.nc','r')
##ha
maitrop = N.average(region1.variables['area'][95:105,:,:],axis=0)

maitrop=ma.masked_where(maitrop<=0,maitrop)
maitrop=ma.filled(maitrop, fill_value=0.)

maizeto = maitrop

region1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_soy_luh2.nc','r')
##ha
 
soytrop = N.average(region1.variables['area'][95:105,:,:],axis=0)

soytrop=ma.masked_where(soytrop<=0,soytrop)
soytrop=ma.filled(soytrop, fill_value=0.)

soyto = soytrop



dat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/soy_irr_fert/output/soy_irr_fert.nc','r')
iyield1ys = N.average(dat.variables['totalyield'][95:105,:,:],axis=0)
iyield1yns = dat.variables['totalyield'][95:105,:,:]

latisam=dat.variables['lat'][:]
lonisam=dat.variables['lon'][:]
iyield1ys,gridlon1 = shiftgrid(180.5,iyield1ys,gridlon,start=False)

iyield1ys= ma.masked_where(iyield1ys<=0.,iyield1ys)
ncvar_soy= ma.masked_where(ncvar_soy<=0.,ncvar_soy)
areasoy= ma.masked_where(areasoy<=0.,areasoy)

iyield1ys= ma.masked_where(ncvar_soy<=0.,iyield1ys)
ncvar_soy= ma.masked_where(iyield1ys<=0.,ncvar_soy)
iyield1ys= ma.masked_where(ncvar_soy<=0.,iyield1ys)
ncvar_soy= ma.masked_where(iyield1ys<=0.,ncvar_soy)

areasoy= ma.masked_where(iyield1ys<=0.,areasoy)

iyield1yns= ma.masked_where(iyield1yns<=0.,iyield1yns)
iyield1ys= ma.masked_where(soyto<=0.,iyield1ys)
ncvar_soy= ma.masked_where(soyto<=0.,ncvar_soy)
areasoy= ma.masked_where(soyto<=0.,areasoy)




dat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/mai_irr_fert/output/mai_irr_fert.nc','r')
iyield1y = N.average(dat.variables['totalyield'][95:105,:,:],axis=0)
iyield1yn = dat.variables['totalyield'][95:105,:,:]

iyield1y,gridlon1 = shiftgrid(180.5,iyield1y,gridlon,start=False)

iyield1y= ma.masked_where(iyield1y<=0.,iyield1y)
ncvar_maize= ma.masked_where(ncvar_maize<=0.,ncvar_maize)
areamaize= ma.masked_where(areamaize<=0.,areamaize)

iyield1y= ma.masked_where(ncvar_maize<=0.,iyield1y)
ncvar_maize= ma.masked_where(iyield1y<=0.,ncvar_maize)
iyield1y= ma.masked_where(ncvar_maize<=0.,iyield1y)
ncvar_maize= ma.masked_where(iyield1y<=0.,ncvar_maize)

areamaize= ma.masked_where(iyield1y<=0.,areamaize)

iyield1yn= ma.masked_where(iyield1yn<=0.,iyield1yn)
iyield1y= ma.masked_where(maizeto<=0.,iyield1y)
ncvar_maize= ma.masked_where(maizeto<=0.,ncvar_maize)
areamaize= ma.masked_where(maizeto<=0.,areamaize)






lon2,lat2 = N.meshgrid(gridlon1,latisam)
cmap = plt.cm.terrain_r
bounds=[-0.1,0.0,0.01,0.05,0.1,0.5,1,2,3,4,5,6]
norm = colors.BoundaryNorm(bounds, cmap.N)



fig = plt.figure(figsize=(10,10))

ax2 = fig.add_subplot(211)

map = Basemap(projection ='cyl', llcrnrlat=-65, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')

x,y = map(lon2,lat2)


map.drawcoastlines(color='gray')
#map.drawcountries()
#map.drawmapboundary()

cs1 = map.pcolormesh(x,y,iyield1y*areamaize*10000/gridarea,cmap=cmap,norm=norm)
plt.axis('off')
plt.title('Maize (t grains / grid cell ha)',fontsize=16)
cbar = map.colorbar(cs1,location='bottom',size="5%",pad="2%",ticks=bounds,extend='max')
cbar.ax.tick_params(labelsize=16)


bounds=[-0.1,0.0,0.03,0.06,0.09,0.12,0.15,0.2,0.3,0.4,0.5,0.6,0.7]
norm = colors.BoundaryNorm(bounds, cmap.N)


ax2 = fig.add_subplot(212)
map = Basemap(projection ='cyl', llcrnrlat=-65, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')

map.drawcoastlines(color='grey')
map.drawmapboundary()
cs1 = map.pcolormesh(x,y,iyield1ys*areasoy*10000/gridarea,cmap=cmap,norm=norm)
plt.title('Soybean (t grains / grid cell ha)',fontsize=16)

cbar = map.colorbar(cs1,location='bottom',size="5%",pad="2%",ticks=bounds,extend='max')
cbar.ax.tick_params(labelsize=16)



plt.axis('off')

plt.savefig('maisoybase_1996_2005.jpg',dpi=600,bbox_inches='tight')
plt.show()

