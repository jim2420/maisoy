from mpl_toolkits.basemap import Basemap, cm, shiftgrid,interp,maskoceans
from netCDF4 import Dataset as NetCDFFile
import numpy as N
import matplotlib.pyplot as plt
import numpy.ma as ma
xx=1110
isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/luh2area_850_2015_corrcrop.nc','r')
meareaisam1 = isam1.variables['fsoy_tt'][1151,:,:]#2000
meareaisam1= ma.masked_where(meareaisam1<=0.0,meareaisam1)
print meareaisam1.shape
fmearea = isam1.variables['fsoy_tt'][1051,:,:]#1901

fmearea= ma.masked_where(fmearea<=0.0,fmearea)

mask=NetCDFFile('/global/project/projectdirs/m1602/datasets4.full/arbit_init_state_05x05.nc','r')
ind = mask.variables['REGION_MASK'][:,:]
ind= ma.masked_where(ind<=0.0,ind)

ind1=N.zeros((50,360,720))
farea=N.zeros((50,360,720))
meareaisam=N.zeros((50,360,720))

for i in range(0,50):
	ind1[i,:,:]=ind[:,:]
	farea[i,:,:]=fmearea[:,:]
	meareaisam[i,:,:]=meareaisam1
meareaisam= ma.masked_where(ind1!=8,meareaisam)
farea= ma.masked_where(ind1!=8,farea)

area=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/gridareahalf_isam.nc','r')
gridarea = area.variables['cell_area']

isam=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/soy_irr_fert/output/soy_irr_fert.nc','r')
lonisam1=isam.variables['lon'][:]
x1=59#1960
tric_i_f=isam.variables['totalyield'][x1:109,:,:]
tric_i_f=ma.masked_where(tric_i_f<=0.0,tric_i_f)
tric_i_f=ma.filled(tric_i_f, fill_value=0.)
tric_i_f= ma.masked_where(ind1!=8,tric_i_f)

isam=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/soy_fert/output/soy_fert.nc','r')
tric_f=isam.variables['totalyield'][x1:109,:,:]
tric_f=ma.masked_where(tric_f<=0.0,tric_f)
tric_f=ma.filled(tric_f, fill_value=0.)
tric_f= ma.masked_where(ind1!=8,tric_f)

isam=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/fixedirr/soy_cli/output/soy_cli.nc','r')
tric_fc=isam.variables['totalyield'][x1:109,:,:]
tric_fc=ma.masked_where(tric_fc<=0.0,tric_fc)
tric_fc=ma.filled(tric_fc, fill_value=0.)
tric_fc= ma.masked_where(ind1!=8,tric_fc)

isam=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/fixedirr/soy_irr/output/soy_irr.nc','r')
tric_i=isam.variables['totalyield'][x1:109,:,:]
tric_i=ma.masked_where(tric_i<=0.0,tric_i)
tric_i=ma.filled(tric_i, fill_value=0.)
tric_i= ma.masked_where(ind1!=8,tric_i)

isam=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/fixedirr/soy_co2/output/soy_co2.nc','r')
tric_c=isam.variables['totalyield'][x1:109,:,:]
tric_c=ma.masked_where(tric_c<=0.0,tric_c)
tric_c=ma.filled(tric_c, fill_value=0.)
tric_c= ma.masked_where(ind1!=8,tric_c)
isam=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/soyequilibrium/output/soyequilibrium.nc','r')
ric_i_f=isam.variables['totalyield'][x1:109,:,:]
ric_i_f=ma.masked_where(ric_i_f<=0.0,ric_i_f)
ric_i_f=ma.filled(ric_i_f, fill_value=0.)
ric_i_f= ma.masked_where(ind1!=8,ric_i_f)

isam=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/soyequilibrium_fert/output/soyequilibrium_fert.nc','r')
ric_f=isam.variables['totalyield'][x1:109,:,:]
ric_f=ma.masked_where(ric_f<=0.0,ric_f)
ric_f=ma.filled(ric_f, fill_value=0.)
ric_f= ma.masked_where(ind1!=8,ric_f)

isam=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/fixedirr/equili/soyequilibrium_irr/output/soyequilibrium_irr.nc','r')
ric_i=isam.variables['totalyield'][x1:109,:,:]
ric_i=ma.masked_where(ric_i<=0.0,ric_i)
ric_i=ma.filled(ric_i, fill_value=0.)
ric_i= ma.masked_where(ind1!=8,ric_i)
isam=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/soyequilibrium_co2/output/soyequilibrium_co2.nc','r')
ric_c=isam.variables['totalyield'][x1:109,:,:]
ric_c=ma.masked_where(ric_c<=0.0,ric_c)
ric_c=ma.filled(ric_c, fill_value=0.)
ric_c= ma.masked_where(ind1!=8,ric_c)

isam=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/soyequilibrium_cli/output/soyequilibrium_cli.nc','r')
ric_cli=isam.variables['totalyield'][x1:109,:,:]
ric_cli=ma.masked_where(ric_cli<=0.0,ric_cli)
ric_cli=ma.filled(ric_cli, fill_value=0.)
ric_cli= ma.masked_where(ind1!=8,ric_cli)



c=50
base=N.zeros(c)
base_i=N.zeros(c)#no irrigation

base_c=N.zeros(c)#fixed co2
base_cli=N.zeros(c)#irrigation and fixed climate
base_f=N.zeros(c) #no fertilizer
base_n=N.zeros(c)
tbase=N.zeros(c)
tbase_i=N.zeros(c)#no irrigation
tbase_n=N.zeros(c)
tbase_c=N.zeros(c)#fixed co2
tbase_cli=N.zeros(c)#irrigation and fixed climate
tbase_f=N.zeros(c) #no fertilizer
tbase_lu=N.zeros(c)
base_lu=N.zeros(c)


tbase_lu=N.sum(tric_i_f*farea,axis=(1,2))
tbase=N.sum(tric_i_f*meareaisam,axis=(1,2))
tbase_i=N.sum(tric_f*meareaisam,axis=(1,2))
tbase_f=N.sum(tric_i*meareaisam,axis=(1,2))
tbase_cli=N.sum(tric_fc*meareaisam,axis=(1,2))
tbase_c=N.sum(tric_c*meareaisam,axis=(1,2))

base_lu=N.sum(ric_i_f*farea,axis=(1,2))
base=N.sum(ric_i_f*meareaisam,axis=(1,2))
base_i=N.sum(ric_i*meareaisam,axis=(1,2))
base_f=N.sum(ric_f*meareaisam,axis=(1,2))
base_cli=N.sum(ric_cli*meareaisam,axis=(1,2))
base_c=N.sum(ric_c*meareaisam,axis=(1,2))

yirr=(tbase-tbase_i)
yf=(tbase-tbase_f)
ycli=(tbase-tbase_cli)
yc=(tbase-tbase_c)
ylu=tbase-tbase_lu

tyirr=(base_i-base)
tyf=(base_f-base)
tycli=(base_cli-base)
tyc=(base_c-base)
tylu=base-base_lu

ayirr=(N.average(yirr[0:10]),N.average(yirr[10:20]),N.average(yirr[20:30]),N.average(yirr[30:40]),N.average(yirr[40:50]))
aycli=(N.average(ycli[0:10]),N.average(ycli[10:20]),N.average(ycli[20:30]),N.average(ycli[30:40]),N.average(ycli[40:50]))
ayc=(N.average(yc[0:10]),N.average(yc[10:20]),N.average(yc[20:30]),N.average(yc[30:40]),N.average(yc[40:50]))
ayf=(N.average(yf[0:10]),N.average(yf[10:20]),N.average(yf[20:30]),N.average(yf[30:40]),N.average(yf[40:50]))
aylu=(N.average(ylu[0:10]),N.average(ylu[10:20]),N.average(ylu[20:30]),N.average(ylu[30:40]),N.average(ylu[40:50]))

sayirr=(N.std(yirr[0:10]),N.std(yirr[10:20]),N.std(yirr[20:30]),N.std(yirr[30:40]),N.std(yirr[40:50]))
saycli=(N.std(ycli[0:10]),N.std(ycli[10:20]),N.std(ycli[20:30]),N.std(ycli[30:40]),N.std(ycli[40:50]))
sayf=(N.std(yf[0:10]),N.std(yf[10:20]),N.std(yf[20:30]),N.std(yf[30:40]),N.std(yf[40:50]))
sayc=(N.std(yc[0:10]),N.std(yc[10:20]),N.std(yc[20:30]),N.std(yc[30:40]),N.std(yc[40:50]))
saylu=(N.std(ylu[0:10]),N.std(ylu[10:20]),N.std(ylu[20:30]),N.std(ylu[30:40]),N.std(ylu[40:50]))



tayirr=(N.average(tyirr[0:10]),N.average(tyirr[10:20]),N.average(tyirr[20:30]),N.average(tyirr[30:40]),N.average(tyirr[40:50]))
taycli=(N.average(tycli[0:10]),N.average(tycli[10:20]),N.average(tycli[20:30]),N.average(tycli[30:40]),N.average(tycli[40:50]))
tayc=(N.average(tyc[0:10]),N.average(tyc[10:20]),N.average(tyc[20:30]),N.average(tyc[30:40]),N.average(tyc[40:50]))
tayf=(N.average(tyf[0:10]),N.average(tyf[10:20]),N.average(tyf[20:30]),N.average(tyf[30:40]),N.average(tyf[40:50]))
taylu=(N.average(tylu[0:10]),N.average(tylu[10:20]),N.average(tylu[20:30]),N.average(tylu[30:40]),N.average(tylu[40:50]))


tsayirr=(N.std(tyirr[0:10]),N.std(tyirr[10:20]),N.std(tyirr[20:30]),N.std(tyirr[30:40]),N.std(tyirr[40:50]))
tsaycli=(N.std(tycli[0:10]),N.std(tycli[10:20]),N.std(tycli[20:30]),N.std(tycli[30:40]),N.std(tycli[40:50]))
tsayf=(N.std(tyf[0:10]),N.std(tyf[10:20]),N.std(tyf[20:30]),N.std(tyf[30:40]),N.std(tyf[40:50]))
tsayc=(N.std(tyc[0:10]),N.std(tyc[10:20]),N.std(tyc[20:30]),N.std(tyc[30:40]),N.std(tyc[40:50]))
tsaylu=(N.std(tylu[0:10]),N.std(tylu[10:20]),N.std(tylu[20:30]),N.std(tylu[30:40]),N.std(tylu[40:50]))


tsbase=(N.average(tbase[0:10]),N.average(tbase[10:20]),N.average(tbase[20:30]),N.average(tbase[30:40]),N.average(tbase[40:50]))
sbase=(N.std(tbase[0:10]),N.std(tbase[10:20]),N.std(tbase[20:30]),N.std(tbase[30:40]),N.std(tbase[40:50]))



fig = plt.figure(figsize=(8,4))
n_groups = 5
ax = fig.add_subplot(111)
#plt.ylim(-10,60)
index = N.arange(n_groups)
bar_width = 0.11
opacity = 0.6
#arects21 = plt.bar(0.05+index, tayc, bar_width, yerr=tsayc,hatch='..',
#                     alpha=opacity,color='black',label='CO$_{2}$')
rects3 = plt.bar(0.05+index+bar_width*1, ayc, bar_width, yerr=sayc,
         alpha=opacity,color='black',label='CO$_{2}$')
#rects2 = plt.bar(0.05+index+bar_width*2, taycli, bar_width, yerr=tsaycli,hatch='..',
#         alpha=opacity,color='blue',
#         label='Climate')
rects22 = plt.bar(0.05+index+bar_width*2, aycli, bar_width, yerr=saycli,
         alpha=opacity,color='blue',
         label='Climate')

#rects02 = plt.bar(0.05+index+bar_width*4, tayirr, bar_width, yerr=tsayirr,hatch='..',
#         alpha=opacity,color='red',
#         label='Irrigation')
rects0 = plt.bar(0.05+index+bar_width*3, ayirr, bar_width, yerr=sayirr,
         alpha=opacity,color='red',
         label='Irrigation')

#rects41 = plt.bar(0.05+index+bar_width*6, tayf, bar_width, yerr=tsayf,hatch='..',
#         alpha=opacity,color='green',
#         label='Nitrogen fertilizer')

rects4 = plt.bar(0.05+index+bar_width*4, ayf, bar_width, yerr=sayf,
         alpha=opacity,color='green',
         label='Nitrogen fertilizer')

#rects412 = plt.bar(0.05+index+bar_width*8, taylu, bar_width, yerr=tsaylu,hatch='..',
#         alpha=opacity,color='m',
#         label='Land conversion')

rects42 = plt.bar(0.05+index+bar_width*5, aylu, bar_width, yerr=saylu,
         alpha=opacity,color='m',
         label='Land conversion')

rects = plt.bar(0.05+index+bar_width*6, tsbase, bar_width, yerr=sbase,
         alpha=opacity,color='gray',
         label='Base')


plt.ylabel('Effect on prodiction (tonnes/yr)',fontsize=18)
plt.tick_params(axis='both',labelsize=18)
plt.xticks(index + bar_width+0.37, ('1960s','1970s','1980s','1990s','2000s'))
#leg=plt.legend(loc=2)
#leg.get_frame().set_alpha(0.5)

plt.tight_layout()

plt.savefig('soyp_effect_aogsluii1960fixedlu.png')
plt.show()

