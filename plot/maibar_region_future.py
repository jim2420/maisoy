from mpl_toolkits.basemap import Basemap, cm, shiftgrid,interp
from netCDF4 import Dataset as NetCDFFile
import numpy as N
import matplotlib.pyplot as plt
import glob
import numpy.ma as ma
from scipy.interpolate import griddata
import matplotlib.colors as colors
area1=NetCDFFile('/project/projectdirs/m1602/datasets4.full/surfdata_05x05.nc','r')
mask = area1.variables['REGION_MASK_CRU_NCEP'][:,:]

area=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/gridareahalf_isam.nc','r')
gridarea1= area.variables['cell_area'][:,:]
gridlon = area.variables['lon'][:]
gridlat=area.variables['lat'][:]

region1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_mai_luh2rcp45.nc','r')
maitrop = region1.variables['area'][75:85,:,:]#2090-2099
lonisam1=region1.variables['lon'][:]
maitrop=ma.masked_where(maitrop<=0,maitrop)
maitrop=ma.filled(maitrop, fill_value=0.)
maizeto = maitrop

region2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_mai_luh2rcp85.nc','r')
maitrop85 = region2.variables['area'][75:85,:,:]#2090-2099
maitrop85=ma.masked_where(maitrop85<=0,maitrop85)
maitrop85=ma.filled(maitrop85, fill_value=0.)
maizeto85 = maitrop85


edat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/equili/maiequilibrium/output/maiequilibrium.nc','r')
eiyield1ynew = edat.variables['totalyield'][75:85,:,:]

edat2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/equili/maiequilibrium_irr/output/maiequilibrium_irr.nc','r')
eiyield2ynew = edat2.variables['totalyield'][75:85,:,:]

edat3=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/equili/maiequilibrium_fert/output/maiequilibrium_fert.nc','r')
eiyield3ynew = edat3.variables['totalyield'][75:85,:,:]

edat4=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/equili/maiequilibrium_co2/output/maiequilibrium_co2.nc','r')
eiyield4ynew = edat4.variables['totalyield'][75:85,:,:]

edat5=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/equili/maiequilibrium_cli/output/maiequilibrium_cli.nc','r')
eiyield5ynew = edat5.variables['totalyield'][75:85,:,:]
 
edat85=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/equili/maiequilibrium/output/maiequilibrium.nc','r')
eiyield1ynew85 = edat85.variables['totalyield'][75:85,:,:]

edat285=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/equili/maiequilibrium_irr/output/maiequilibrium_irr.nc','r')
eiyield2ynew85 = edat285.variables['totalyield'][75:85,:,:]

edat385=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/equili/maiequilibrium_fert/output/maiequilibrium_fert.nc','r')
eiyield3ynew85 = edat385.variables['totalyield'][75:85,:,:]

edat485=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/equili/maiequilibrium_co2/output/maiequilibrium_co2.nc','r')
eiyield4ynew85 = edat485.variables['totalyield'][75:85,:,:]

edat585=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/equili/maiequilibrium_cli/output/maiequilibrium_cli.nc','r')
eiyield5ynew85 = edat585.variables['totalyield'][75:85,:,:]

dat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/mai_irr_fert/output/mai_irr_fert.nc','r')
iyield1ynew = dat.variables['totalyield'][75:85,:,:]
latisam=dat.variables['lat'][:]
lonisam=dat.variables['lon'][:]
dat2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/mai_fert/output/mai_fert.nc','r')
iyield2ynew = dat2.variables['totalyield'][75:85,:,:]

dat3=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/mai_irr/output/mai_irr.nc','r')
iyield3ynew = dat3.variables['totalyield'][75:85,:,:]

dat4=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/mai_co2/output/mai_co2.nc','r')
iyield4ynew = dat4.variables['totalyield'][75:85,:,:]

dat5=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/mai_cli/output/mai_cli.nc','r')
iyield5ynew = dat5.variables['totalyield'][75:85,:,:]


dat85=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/mai_irr_fert/output/mai_irr_fert.nc','r')
iyield1ynew85 = dat85.variables['totalyield'][75:85,:,:]

dat285=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/mai_fert/output/mai_fert.nc','r')
iyield2ynew85 = dat285.variables['totalyield'][75:85,:,:]

dat385=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/mai_irr/output/mai_irr.nc','r')
iyield3ynew85 = dat385.variables['totalyield'][75:85,:,:]

dat485=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/mai_co2/output/mai_co2.nc','r')
iyield4ynew85 = dat485.variables['totalyield'][75:85,:,:]

dat585=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/mai_cli/output/mai_cli.nc','r')
iyield5ynew85 = dat585.variables['totalyield'][75:85,:,:]



iyield1ynew= ma.masked_where(iyield1ynew<=0.,iyield1ynew)
iyield2ynew= ma.masked_where(iyield2ynew<=0.,iyield2ynew)
iyield3ynew= ma.masked_where(iyield3ynew<=0.,iyield3ynew)
iyield4ynew= ma.masked_where(iyield4ynew<=0.,iyield4ynew)
iyield5ynew= ma.masked_where(iyield5ynew<=0.,iyield5ynew)

eiyield1ynew= ma.masked_where(eiyield1ynew<=0.,eiyield1ynew)
eiyield2ynew= ma.masked_where(eiyield2ynew<=0.,eiyield2ynew)
eiyield3ynew= ma.masked_where(eiyield3ynew<=0.,eiyield3ynew)
eiyield4ynew= ma.masked_where(eiyield4ynew<=0.,eiyield4ynew)
eiyield5ynew= ma.masked_where(eiyield5ynew<=0.,eiyield5ynew)

iyield1ynew85= ma.masked_where(iyield1ynew85<=0.,iyield1ynew85)
iyield2ynew85= ma.masked_where(iyield2ynew85<=0.,iyield2ynew85)
iyield3ynew85= ma.masked_where(iyield3ynew85<=0.,iyield3ynew85)
iyield4ynew85= ma.masked_where(iyield4ynew85<=0.,iyield4ynew85)
iyield5ynew85= ma.masked_where(iyield5ynew85<=0.,iyield5ynew85)

eiyield1ynew85= ma.masked_where(eiyield1ynew85<=0.,eiyield1ynew85)
eiyield2ynew85= ma.masked_where(eiyield2ynew85<=0.,eiyield2ynew85)
eiyield3ynew85= ma.masked_where(eiyield3ynew85<=0.,eiyield3ynew85)
eiyield4ynew85= ma.masked_where(eiyield4ynew85<=0.,eiyield4ynew85)
eiyield5ynew85= ma.masked_where(eiyield5ynew85<=0.,eiyield5ynew85)

maizeto1,lonisam2=shiftgrid(0.5,maizeto,lonisam1,start=True)
maizeto1r,lonisam2=shiftgrid(0.5,maitrop,lonisam1,start=True)
maizeto185,lonisam2=shiftgrid(0.5,maizeto85,lonisam1,start=True)
maizeto1r85,lonisam2=shiftgrid(0.5,maitrop85,lonisam1,start=True)

iyield1ynew=ma.filled(iyield1ynew, fill_value=0.)
iyield2ynew=ma.filled(iyield2ynew, fill_value=0.)
iyield3ynew=ma.filled(iyield3ynew, fill_value=0.)
iyield4ynew=ma.filled(iyield4ynew, fill_value=0.)
iyield5ynew=ma.filled(iyield5ynew, fill_value=0.)

iyield1ynew= ma.masked_where(iyield1ynew<=0.,iyield1ynew)
iyield2ynew= ma.masked_where(iyield2ynew<=0.,iyield2ynew)
iyield3ynew= ma.masked_where(iyield3ynew<=0.,iyield3ynew)
iyield4ynew= ma.masked_where(iyield4ynew<=0.,iyield4ynew)
iyield5ynew= ma.masked_where(iyield5ynew<=0.,iyield5ynew)

iyield1ynew85=ma.filled(iyield1ynew85, fill_value=0.)
iyield2ynew85=ma.filled(iyield2ynew85, fill_value=0.)
iyield3ynew85=ma.filled(iyield3ynew85, fill_value=0.)
iyield4ynew85=ma.filled(iyield4ynew85, fill_value=0.)
iyield5ynew85=ma.filled(iyield5ynew85, fill_value=0.)

iyield1ynew85= ma.masked_where(iyield1ynew85<=0.,iyield1ynew85)
iyield2ynew85= ma.masked_where(iyield2ynew85<=0.,iyield2ynew85)
iyield3ynew85= ma.masked_where(iyield3ynew85<=0.,iyield3ynew85)
iyield4ynew85= ma.masked_where(iyield4ynew85<=0.,iyield4ynew85)
iyield5ynew85= ma.masked_where(iyield5ynew85<=0.,iyield5ynew85)

eiyield1ynew=ma.filled(eiyield1ynew, fill_value=0.)
eiyield2ynew=ma.filled(eiyield2ynew, fill_value=0.)
eiyield3ynew=ma.filled(eiyield3ynew, fill_value=0.)
eiyield4ynew=ma.filled(eiyield4ynew, fill_value=0.)
eiyield5ynew=ma.filled(eiyield5ynew, fill_value=0.)

eiyield1ynew= ma.masked_where(eiyield1ynew<=0.,eiyield1ynew)
eiyield2ynew= ma.masked_where(eiyield2ynew<=0.,eiyield2ynew)
eiyield3ynew= ma.masked_where(eiyield3ynew<=0.,eiyield3ynew)
eiyield4ynew= ma.masked_where(eiyield4ynew<=0.,eiyield4ynew)
eiyield5ynew= ma.masked_where(eiyield5ynew<=0.,eiyield5ynew)


eiyield1ynew85=ma.filled(eiyield1ynew85, fill_value=0.)
eiyield2ynew85=ma.filled(eiyield2ynew85, fill_value=0.)
eiyield3ynew85=ma.filled(eiyield3ynew85, fill_value=0.)
eiyield4ynew85=ma.filled(eiyield4ynew85, fill_value=0.)
eiyield5ynew85=ma.filled(eiyield5ynew85, fill_value=0.)

eiyield1ynew85= ma.masked_where(eiyield1ynew85<=0.,eiyield1ynew85)
eiyield2ynew85= ma.masked_where(eiyield2ynew85<=0.,eiyield2ynew85)
eiyield3ynew85= ma.masked_where(eiyield3ynew85<=0.,eiyield3ynew85)
eiyield4ynew85= ma.masked_where(eiyield4ynew85<=0.,eiyield4ynew85)
eiyield5ynew85= ma.masked_where(eiyield5ynew85<=0.,eiyield5ynew85)


#print iyield1ynew.shape
rmask=N.zeros((10,360,720))
m3maize=N.zeros((10,360,720))
maizeto2=N.zeros((10,360,720))
maizeto285=N.zeros((10,360,720))
maizeto2i=N.zeros((10,360,720))
maizete2r=N.zeros((10,360,720))
maizete2i=N.zeros((10,360,720))
landfrac2=N.zeros((10,360,720))
gridarea2=N.zeros((10,360,720))

for i in range(0,10):
	for x in range(0,360):
		for y in range(0,720):
                        rmask[i,x,y]=mask[x,y]
			maizeto2[i,x,y]=maizeto1[i,x,y]
                        maizeto285[i,x,y]=maizeto185[i,x,y]
                        gridarea2[i,x,y]=gridarea1[x,y]




ii=N.zeros((9,2))
nn=N.zeros((9,2))
co=N.zeros((9,2))
cli=N.zeros((9,2))
sii=N.zeros((9,2))
snn=N.zeros((9,2))
sco=N.zeros((9,2))
scli=N.zeros((9,2))

eii=N.zeros((9,2))
enn=N.zeros((9,2))
eco=N.zeros((9,2))
ecli=N.zeros((9,2))
esii=N.zeros((9,2))
esnn=N.zeros((9,2))
esco=N.zeros((9,2))
escli=N.zeros((9,2))


for i in range (1,9):
	maizeto3=maizeto2
        maizeto385=maizeto285
	if i==5:
		i=9
	if i==4 :
	        maizeto3=ma.masked_where(rmask>5.0,maizeto3)
                maizeto3=ma.masked_where(rmask<4.0,maizeto3)
                maizeto385=ma.masked_where(rmask>5.0,maizeto385)
                maizeto385=ma.masked_where(rmask<4.0,maizeto385)

	else:
		print i
		maizeto3=ma.masked_where(rmask!=i,maizeto3)
                maizeto385=ma.masked_where(rmask!=i,maizeto385)

	if i==9:
		i=5

	maizeto3=ma.filled(maizeto3, fill_value=0.)
        maizeto385=ma.filled(maizeto385, fill_value=0.)

        allynew=N.sum(iyield1ynew*maizeto3,axis=(1,2))
        allyinew=N.sum(iyield2ynew*maizeto3,axis=(1,2))
        allynnew=N.sum(iyield3ynew*maizeto3,axis=(1,2))
        allycnew=N.sum(iyield4ynew*maizeto3,axis=(1,2))
        allyclinew=N.sum(iyield5ynew*maizeto3,axis=(1,2))

        allynew85=N.sum(iyield1ynew85*maizeto385,axis=(1,2))
        allyinew85=N.sum(iyield2ynew85*maizeto385,axis=(1,2))
        allynnew85=N.sum(iyield3ynew85*maizeto385,axis=(1,2))
        allycnew85=N.sum(iyield4ynew85*maizeto385,axis=(1,2))
        allyclinew85=N.sum(iyield5ynew85*maizeto385,axis=(1,2))


	bb=(allynew-allyinew)/allynew*100
	cc=(allynew-allynnew)/allynew*100
	dd=(allynew-allycnew)/allynew*100
	ee=(allynew-allyclinew)/allynew*100

        bb85=(allynew85-allyinew85)/allynew85*100
        cc85=(allynew85-allynnew85)/allynew85*100
        dd85=(allynew85-allycnew85)/allynew85*100
        ee85=(allynew85-allyclinew85)/allynew85*100

	ii[i,0]=N.average(bb)
	nn[i,0]=N.average(cc)
	co[i,0]=N.average(dd)
	cli[i,0]=N.average(ee)

	sii[i,0]=N.std(bb)
	snn[i,0]=N.std(cc)
	sco[i,0]=N.std(dd)
	scli[i,0]=N.std(ee)

        ii[i,1]=N.average(bb85)
        nn[i,1]=N.average(cc85)
        co[i,1]=N.average(dd85)
        cli[i,1]=N.average(ee85)

        sii[i,1]=N.std(bb85)
        snn[i,1]=N.std(cc85)
        sco[i,1]=N.std(dd85)
        scli[i,1]=N.std(ee85)

        eallynew=N.sum(eiyield1ynew*maizeto3,axis=(1,2))
        eallyinew=N.sum(eiyield2ynew*maizeto3,axis=(1,2))
        eallynnew=N.sum(eiyield3ynew*maizeto3,axis=(1,2))
        eallycnew=N.sum(eiyield4ynew*maizeto3,axis=(1,2))
        eallyclinew=N.sum(eiyield5ynew*maizeto3,axis=(1,2))

        eallynew85=N.sum(eiyield1ynew85*maizeto385,axis=(1,2))
        eallyinew85=N.sum(eiyield2ynew85*maizeto385,axis=(1,2))
        eallynnew85=N.sum(eiyield3ynew85*maizeto385,axis=(1,2))
        eallycnew85=N.sum(eiyield4ynew85*maizeto385,axis=(1,2))
        eallyclinew85=N.sum(eiyield5ynew85*maizeto385,axis=(1,2))

        ebb=(eallyinew-eallynew)/allynew*100
        ecc=(eallynnew-eallynew)/allynew*100
        edd=(eallycnew-eallynew)/allynew*100
        eee=(eallyclinew-eallynew)/allynew*100

        ebb85=(eallyinew85-eallynew85)/allynew85*100
        ecc85=(eallynnew85-eallynew85)/allynew85*100
        edd85=(eallycnew85-eallynew85)/allynew85*100
        eee85=(eallyclinew85-eallynew85)/allynew85*100

        eii[i,0]=N.average(ebb)
        enn[i,0]=N.average(ecc)
        eco[i,0]=N.average(edd)
        ecli[i,0]=N.average(eee)

        esii[i,0]=N.std(ebb)
        esnn[i,0]=N.std(ecc)
        esco[i,0]=N.std(edd)
        escli[i,0]=N.std(eee)

        eii[i,1]=N.average(ebb85)
        enn[i,1]=N.average(ecc85)
        eco[i,1]=N.average(edd85)
        ecli[i,1]=N.average(eee85)

        esii[i,1]=N.std(ebb85)
        esnn[i,1]=N.std(ecc85)
        esco[i,1]=N.std(edd85)
        escli[i,1]=N.std(eee85)



allynew=N.sum(iyield1ynew*maizeto2,axis=(1,2))
allyinew=N.sum(iyield2ynew*maizeto2,axis=(1,2))
allynnew=N.sum(iyield3ynew*maizeto2,axis=(1,2))
allycnew=N.sum(iyield4ynew*maizeto2,axis=(1,2))
allyclinew=N.sum(iyield5ynew*maizeto2,axis=(1,2))

allynew85=N.sum(iyield1ynew85*maizeto285,axis=(1,2))
allyinew85=N.sum(iyield2ynew85*maizeto285,axis=(1,2))
allynnew85=N.sum(iyield3ynew85*maizeto285,axis=(1,2))
allycnew85=N.sum(iyield4ynew85*maizeto285,axis=(1,2))
allyclinew85=N.sum(iyield5ynew85*maizeto285,axis=(1,2))

bb=(allynew-allyinew)/allynew*100
cc=(allynew-allynnew)/allynew*100
dd=(allynew-allycnew)/allynew*100
ee=(allynew-allyclinew)/allynew*100

bb85=(allynew85-allyinew85)/allynew85*100
cc85=(allynew85-allynnew85)/allynew85*100
dd85=(allynew85-allycnew85)/allynew85*100
ee85=(allynew85-allyclinew85)/allynew85*100


ii[0,0]=N.average(bb)
nn[0,0]=N.average(cc)
co[0,0]=N.average(dd)
cli[0,0]=N.average(ee)

sii[0,0]=N.std(bb)
snn[0,0]=N.std(cc)
sco[0,0]=N.std(dd)
scli[0,0]=N.std(ee)

ii[0,1]=N.average(bb85)
nn[0,1]=N.average(cc85)
co[0,1]=N.average(dd85)
cli[0,1]=N.average(ee85)

sii[0,1]=N.std(bb85)
snn[0,1]=N.std(cc85)
sco[0,1]=N.std(dd85)
scli[0,1]=N.std(ee85)

eallynew=N.sum(eiyield1ynew*maizeto2,axis=(1,2))
eallyinew=N.sum(eiyield2ynew*maizeto2,axis=(1,2))
eallynnew=N.sum(eiyield3ynew*maizeto2,axis=(1,2))
eallycnew=N.sum(eiyield4ynew*maizeto2,axis=(1,2))
eallyclinew=N.sum(eiyield5ynew*maizeto2,axis=(1,2))

eallynew85=N.sum(eiyield1ynew85*maizeto285,axis=(1,2))
eallyinew85=N.sum(eiyield2ynew85*maizeto285,axis=(1,2))
eallynnew85=N.sum(eiyield3ynew85*maizeto285,axis=(1,2))
eallycnew85=N.sum(eiyield4ynew85*maizeto285,axis=(1,2))
eallyclinew85=N.sum(eiyield5ynew85*maizeto285,axis=(1,2))


ebb=(eallyinew-eallynew)/allynew*100
ecc=(eallynnew-eallynew)/allynew*100
edd=(eallycnew-eallynew)/allynew*100
eee=(eallyclinew-eallynew)/allynew*100

ebb85=(eallyinew85-eallynew85)/allynew85*100
ecc85=(eallynnew85-eallynew85)/allynew85*100
edd85=(eallycnew85-eallynew85)/allynew85*100
eee85=(eallyclinew85-eallynew85)/allynew85*100

eii[0,0]=N.average(ebb)
enn[0,0]=N.average(ecc)
eco[0,0]=N.average(edd)
ecli[0,0]=N.average(eee)

esii[0,0]=N.std(ebb)
esnn[0,0]=N.std(ecc)
esco[0,0]=N.std(edd)
escli[0,0]=N.std(eee)

eii[0,1]=N.average(ebb85)
enn[0,1]=N.average(ecc85)
eco[0,1]=N.average(edd85)
ecli[0,1]=N.average(eee85)

esii[0,1]=N.std(ebb85)
esnn[0,1]=N.std(ecc85)
esco[0,1]=N.std(edd85)
escli[0,1]=N.std(eee85)


name=["Global","NA","SA","EU","Africa","PD","USSR","China","SSEA"]

fig = plt.figure(figsize=(6.3,5.5))
#plt.rc('font', weight='bold')
plt.subplots_adjust(hspace=1)

for idx in xrange(9):
	ax = fig.add_subplot(3, 3, idx+1)
        ax.spines['bottom'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.yaxis.set_ticks_position('left')

	n_groups = 1
	plt.ylim(-35, 80)
	ax.set_yticks([-20,0,20,40,60,80 ])
        if idx==0 or idx==3 or idx==6:
		ax.set_yticklabels([-20,0,20,40,60,80])
        else:
		ax.set_yticklabels([])

	index = N.arange(n_groups)
	bar_width = 0.01
	opacity = 0.5
        plt.axhline(y=0.0, color='gray', linestyle=':')
        for x in range(0,2):
             if x==0:
                rects0 = plt.scatter(1, eco[idx,x],s=80,
                        color='k',alpha=opacity,
                        label='CO$_{2}$')
                rects4 = plt.scatter(2, ecli[idx,x],
                                        color='b',alpha=opacity,s=80,
                                        label='CLIMATE')
                rects1 = plt.scatter(3, eii[idx,x],
                                color='r',alpha=opacity,s=80,
                                label='Irrigation')
                rects2 = plt.scatter(4 , enn[idx,x],
                                color='g',alpha=opacity,s=80,
                                label='NF')
             else:
                rects10 = plt.scatter(1, eco[idx,x],
                        color='k',facecolors='none',alpha=1,s=80,
                        label='CO$_{2}$')
                rects14 = plt.scatter(2, ecli[idx,x],
                                        color='b',facecolors='none',alpha=1,s=80,
                                        label='CLIMATE')
                rects11 = plt.scatter(3, eii[idx,x],
                                color='r',facecolors='none',alpha=1,s=80,
                                label='Irrigation')
                rects12 = plt.scatter(4 , enn[idx,x],s=80,
                                color='g',facecolors='none',alpha=1,
                                label='NF')
        for x in range(0,2):
             if x==0:
                rects08 = plt.scatter(1.5, co[idx,x],s=80,
                        color='k',alpha=0.5,marker='*',
                        label='CO$_{2}$')
                rects48 = plt.scatter(2.5, cli[idx,x],
                                        color='b',alpha=0.5,s=80,marker='*',
                                        label='CLIMATE')
                rects18 = plt.scatter(3.5, ii[idx,x],marker='*',
                                color='r',alpha=0.5,s=80,
                                label='Irrigation')
                rects28 = plt.scatter(4.5 , nn[idx,x],marker='*',
                                color='g',alpha=0.5,s=80,
                                label='NF')
             else:
                rects108 = plt.scatter(1.5, co[idx,x],facecolors='none',
                        color='k',marker='*',alpha=1,s=80,
                        label='CO$_{2}$')
                rects148 = plt.scatter(2.5, cli[idx,x],facecolors='none',
                                        color='b',marker='*',alpha=1,s=80,
                                        label='CLIMATE')
                rects118 = plt.scatter(3.5, ii[idx,x],facecolors='none',
                                color='r',marker='*',alpha=1,s=80,
                                label='Irrigation')
                rects128 = plt.scatter(4.5 , nn[idx,x],s=80,facecolors='none',
                                color='g',marker='*',alpha=1,
                                label='NF')
	plt.tight_layout()

	#plt.subplots_adjust(hspace=0.5)
	plt.tick_params(
	    axis='x',          # changes apply to the x-axis
	    which='both',      # both major and minor ticks are affected
	    bottom='off',      # ticks along the bottom edge are off
	    top='off',         # ticks along the top edge are off
	    labelbottom='off') # labels along the bottom edge are off
#	plt.axis('off')

	ax.text(.25,.85,'{0}'.format(name[idx]),fontsize=12,
        	horizontalalignment='center',
        	transform=ax.transAxes)
#	plt.title('{0}'.format(name[idx]))
#plt.tight_layout()
	ax.tick_params(labelsize=12)

plt.savefig('mai_region_idfuture.png')
plt.show()
