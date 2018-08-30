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

isam=NetCDFFile('../code/m3_soy.nc','r')
lonisam = isam.variables['lon'][:]
latisam = isam.variables['lat'][:]
ryield1 = isam.variables['yieldm3'][:,:]
mearea=isam.variables['m3area'][:,:]
gridarea1=isam.variables['gridarea'][:,:]
m3psoy=gridarea1*ryield1/10000
m3ysoy=m3psoy/mearea
m3psoy= ma.masked_where(m3psoy<=0.0,m3psoy)
m3ysoy= ma.masked_where(m3ysoy<=0.0,m3ysoy)



isam=NetCDFFile('../code/m3_mai.nc','r')
ryield2 = isam.variables['yieldm3'][:,:]
mearea2=isam.variables['m3area'][:,:]
m3pmai=gridarea1*ryield2/10000
m3ymai=m3pmai/mearea2
m3pmai= ma.masked_where(m3pmai<=0.0,m3pmai)
m3ymai= ma.masked_where(m3ymai<=0.0,m3ymai)


spam=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/spamsoy_isam.nc','r')
spamys=spam.variables['soyy_total'][:,:]
spampros=spam.variables['soyp_total'][:,:]
spamareas=spam.variables['soya_total'][:,:]
spamys= ma.masked_where(spamys<=0.0,spamys)
spampros= ma.masked_where(spampros<=0.0,spampros)


spam=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/spammaize_isam.nc','r')
spamym=spam.variables['maiy_total'][:,:]
spamprom=spam.variables['maip_total'][:,:]
spamaream=spam.variables['maia_total'][:,:]

spamym= ma.masked_where(spamym<=0.0,spamym)
spamprom= ma.masked_where(spamprom<=0.0,spamprom)


aa1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/iizumi/iizumi.2013JAN29.soybean.1982-2006.30min.nc4','r')
iizumiy=N.zeros((9,360,720))
iizumia=N.zeros((9,360,720))
for i in range(1997,2006):
        xx=i-1982
        j=i-1997
        ya = N.flipud(aa1.variables['yield50'][xx,:,:])#t/ha
        yaa = N.flipud(aa1.variables['area'][xx,:,:])##%
        iizumiy[j,:,:]=ya
        iizumia[j,:,:]=yaa
iizumiy= ma.masked_where(iizumiy<=0.0,iizumiy)
iizumia= ma.masked_where(iizumia<=0.0,iizumia)
iizumiy= ma.masked_where(iizumiy>=(10**18),iizumiy)
iizumia= ma.masked_where(iizumia>=(10**18),iizumia)
iizua=iizumia/100*gridarea1/10000
iizup=iizua*iizumiy
iizups=N.ma.average(iizup,axis=0)
iizuys=N.ma.average(iizumiy,axis=0)


aa1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/iizumi/iizumi.2013JAN29.maize.1982-2006.30min.nc4','r')
for i in range(1997,2006):
        xx=i-1982
        j=i-1997
        ya = N.flipud(aa1.variables['yield50'][xx,:,:])#t/ha
        yaa = N.flipud(aa1.variables['area'][xx,:,:])##%
        iizumiy[j,:,:]=ya
        iizumia[j,:,:]=yaa
iizumiy= ma.masked_where(iizumiy<=0.0,iizumiy)
iizumia= ma.masked_where(iizumia<=0.0,iizumia)
iizumiy= ma.masked_where(iizumiy>=(10**18),iizumiy)
iizumia= ma.masked_where(iizumia>=(10**18),iizumia)
iizua=iizumia/100*gridarea1/10000
iizup=iizua*iizumiy

iizupm=N.ma.average(iizup,axis=0)
iizuym=N.ma.average(iizumiy,axis=0)



region=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_mai_luh2.nc','r')
ma1 = region.variables['yield'][96:105,:,:]
ma1p = region.variables['production'][96:105,:,:]
ma1= ma.masked_where(ma1<=0,ma1)
ma1p= ma.masked_where(ma1p<=0,ma1p)


region1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_soy_luh2vmax1.nc','r')
ma2 = region1.variables['yield'][96:105,:,:]
ma2p = region1.variables['production'][96:105,:,:]
ma2= ma.masked_where(ma2<=0,ma2)
ma2p= ma.masked_where(ma2p<=0,ma2p)

ma1=N.ma.average(ma1,axis=0)
ma2=N.ma.average(ma2,axis=0)

ma1p=N.ma.average(ma1p,axis=0)
ma2p=N.ma.average(ma2p,axis=0)


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


lon,lat = N.meshgrid(lonmask,latmask)
lon1,lat1 = N.meshgrid(lonm3,latm3_new)
m3new1p=N.zeros((3,360,720))
m3new2p=N.zeros((3,360,720))
m3new1y=N.zeros((3,360,720))
m3new2y=N.zeros((3,360,720))

for i in range(0,3):
	if i==0:
		m3new1p[i,:,:]=iizupm[:,:]
                m3new1y[i,:,:]=iizuym[:,:]
                m3new2p[i,:,:]=iizups[:,:]
                m3new2y[i,:,:]=iizuys[:,:]

	elif i==1:
		m3new1p[i,:,:]=spamprom[:,:]
                m3new1y[i,:,:]=spamym[:,:]
                m3new2p[i,:,:]=spampros[:,:]
                m3new2y[i,:,:]=spamys[:,:]

	elif i==2:
		m3new1p[i,:,:]=m3pmai[:,:]
                m3new1y[i,:,:]=m3ymai[:,:]
                m3new2p[i,:,:]=m3psoy[:,:]
                m3new2y[i,:,:]=m3ysoy[:,:]

am3new1p=N.ma.average(m3new1p,axis=0)
am3new1y=N.ma.average(m3new1y,axis=0)
am3new2p=N.ma.average(m3new2p,axis=0)
am3new2y=N.ma.average(m3new2y,axis=0)

am3new1p= ma.masked_where(ma1p<=0,am3new1p)
am3new2p= ma.masked_where(ma2p<=0,am3new2p)
ma1p= ma.masked_where(am3new1p<=0,ma1p)
ma2p= ma.masked_where(am3new2p<=0,ma2p)


cmap = plt.cm.terrain_r
bounds=[-0.1,0.0,0.01,0.05,0.1,0.5,1,2,3,4,5,6]

norm = colors.BoundaryNorm(bounds, cmap.N)

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(221)
ax1.set_title("Maize OBS (t grains / ha gridarea)",fontsize=20)
map = Basemap(projection ='cyl', llcrnrlat=-62, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')
map.drawcoastlines()
map.drawcountries()
map.drawmapboundary()
x,y = map(lon,lat)
cs1 = map.pcolormesh(x,y,am3new1p*10000/gridarea,cmap=cmap,norm=norm)
#cs1 = map.pcolormesh(x,y,m3newp*10000/gridarea,cmap=plt.cm.Greens,norm=colors.PowerNorm(gamma=1./2.),vmin=0,vmax=9)
#cs1 = map.pcolormesh(x,y,m3newp/m3newa,cmap=plt.cm.gist_earth,vmin=0,vmax=10)
plt.axis('off')

cbar = map.colorbar(cs1,location='bottom',size="5%",pad="2%",ticks=bounds,extend='max')
#cbar.ax.set_xticklabels(['0', '0.01', '0.05','0.1','0.5','1','2','3','4','5','6'])  # horizontal colorbar

cbar.ax.tick_params(labelsize=16)

ax1 = fig.add_subplot(222)
ax1.set_title("Maize ISAM (t grains / ha gridarea)",fontsize=20)
map = Basemap(projection ='cyl', llcrnrlat=-62, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')


map.drawcoastlines()
map.drawcountries()
map.drawmapboundary()
#ncvar_y=maskoceans(x1,y1,ncvar_y)
cs1 = map.pcolormesh(x,y,ma1p*10000/gridarea,cmap=cmap,norm=norm)
#cs1 = map.pcolormesh(x,y,ma1,cmap=plt.cm.gist_earth,vmin=0,vmax=10)

plt.axis('off')
cbar = map.colorbar(cs1,location='bottom',size="5%",pad="2%",ticks=bounds,extend='max')
cbar.ax.tick_params(labelsize=16)
#cbar.ax.set_xticklabels(['0', '0.01', '0.05','0.1','0.5','1','2','3','4','5','6'])  # horizontal colorbar

bounds=[-0.1,0.0,0.03,0.06,0.09,0.12,0.15,0.2,0.3,0.4,0.5,0.6,0.7]
norm = colors.BoundaryNorm(bounds, cmap.N)

#bounds=[0,0.01,0.05,0.1,0.5,1,1.5,2]
norm = colors.BoundaryNorm(bounds, cmap.N)

ax1 = fig.add_subplot(223)
ax1.set_title("Soybean OBS (t grains / ha gridarea)",fontsize=20)
map = Basemap(projection ='cyl', llcrnrlat=-62, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')
map.drawcoastlines()
map.drawcountries()
map.drawmapboundary()

cs1 = map.pcolormesh(x,y,am3new2p*10000/gridarea,cmap=cmap,norm=norm)
#cs1 = map.pcolormesh(x,y,m3newps/m3newas,cmap=plt.cm.gist_earth,vmin=0,vmax=5)
plt.axis('off')
cbar = map.colorbar(cs1,location='bottom',size="5%",pad="2%",ticks=bounds,extend='max')
cbar.ax.tick_params(labelsize=16)

ax1 = fig.add_subplot(224)
ax1.set_title("Soybean ISAM (t grains / ha gridarea)",fontsize=20)
map = Basemap(projection ='cyl', llcrnrlat=-62, urcrnrlat=90,llcrnrlon=-180, urcrnrlon=180, resolution='c')


map.drawcoastlines()
map.drawcountries()
map.drawmapboundary()
#ncvar_y=maskoceans(x1,y1,ncvar_y)
cs1 = map.pcolormesh(x,y,ma2p*10000/gridarea,cmap=cmap,norm=norm)
#cs1 = map.pcolormesh(x,y,ma2,cmap=plt.cm.gist_earth,vmin=0,vmax=5)
plt.axis('off')
cbar = map.colorbar(cs1,location='bottom',size="5%",pad="2%",ticks=bounds,extend='max')
cbar.ax.tick_params(labelsize=16)

plt.savefig('isam_maisoycombine.jpg',bbox_inches='tight')

plt.show()


