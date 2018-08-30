from mpl_toolkits.basemap import Basemap, cm, shiftgrid,interp,maskoceans
from netCDF4 import Dataset as NetCDFFile
import numpy as N
import matplotlib.pyplot as plt
import numpy.ma as ma
import matplotlib.colors as colors
def region(x,ryield):
	region=NetCDFFile('/global/project/projectdirs/m1602/datasets4.full/arbit_init_state_05x05.nc','r')
	ind = region.variables['REGION_MASK'][:,:]

	area=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/gridareahalf_isam.nc','r')
	gridarea1 = area.variables['cell_area']

	isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/luh2area_850_2015_corrcrop.nc','r')
	meareaisam = isam1.variables['fmai_tt'][1051:1166,:,:]#1901-2015
	meareaisam= ma.masked_where(meareaisam<=0.0,meareaisam)

        isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/mirca_isam.nc','r')
        meareaisam1 = isam1.variables['amai_tt'][:,:]#mirca2000
        meareaisam1= ma.masked_where(meareaisam1<=0.0,meareaisam1)

        areaa1=N.zeros((x,360,720))
	ind1=N.zeros((x,360,720))
	gridarea=N.zeros((x,360,720))
	for i in range(0,x):
        	ind1[i,:,:]=ind[:,:]
	        gridarea[i,:,:]=gridarea1[:,:]
		areaa1[i,:,:]=meareaisam1[:,:]


	ryield= ma.masked_where(ind1==0.0,ryield)
	gridarea= ma.masked_where(ind1==0.0,gridarea)
	meareaisam= ma.masked_where(ind1==0.0,meareaisam)
        areaa1= ma.masked_where(ind1==0.0,areaa1)

	isamp=ryield*meareaisam
	isamp1=ryield*areaa1
	name=["Global","NA","SA","EU","Africa","PD","USSR","China","SSEA"]

	num=9

	allarea1=N.zeros((num))
	allproisam=N.zeros((num,x))
	allyisam=N.zeros((num,x))
	allgrid=N.zeros((num))
	isamgrid=N.zeros((num,x))

	luharea=N.zeros((num,x))
	for idx in range(0,num):
	        isampmask=N.zeros((115,360,720))
	        isamarea=N.zeros((115,360,720))
	        areak=N.zeros((115,360,720))
	        areak=gridarea
	        isampmask=isamp1
	        isamarea=areaa1

	        if idx==5:
	                idx=9
	        if idx==4 :
	                isampmask=ma.masked_where(ind1>5.0,isampmask)
	                isamarea=ma.masked_where(ind1>5.0,isamarea)
	                areak=ma.masked_where(ind1>5.0,areak)

	                areak=ma.masked_where(ind1<4.0,areak)
	                isampmask=ma.masked_where(ind1<4.0,isampmask)
	                isamarea=ma.masked_where(ind1<4.0,isamarea)

	        elif idx==0:
	   	        isampmask=ma.masked_where(ind1==idx,isampmask)
	                isamarea=ma.masked_where(ind1==idx,isamarea)
	                areak=ma.masked_where(ind1==idx,areak)

		else:
	                isampmask=ma.masked_where(ind1!=idx,isampmask)
	                isamarea=ma.masked_where(ind1!=idx,isamarea)
	                areak=ma.masked_where(ind1!=idx,areak)
	        if idx==9:
	                idx=5

		luharea[idx,:]=N.sum(isamarea,axis=(1,2))

	        allproisam[idx,:]=(N.sum(isampmask,axis=(1,2)))
	        allyisam[idx,:]=N.sum(isampmask,axis=(1,2))/(N.sum(isamarea,axis=(1,2)))
	        isamgrid[idx,:]=(N.sum(isampmask,axis=(1,2))/(N.sum(areak,axis=(1,2)))*10000)
	return allproisam,allyisam,isamgrid

nn=9
year=115

edat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/maiequilibrium/output/maiequilibrium.nc','r')
eiyield1ynew = edat.variables['g_ET'][0:115,0,:,:]

edat2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/fixedirr/equili/maiequilibrium_irr/output/maiequilibrium_irr.nc','r')
eiyield2ynew = edat2.variables['g_ET'][0:115,0,:,:]

edat3=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/maiequilibrium_fert/output/maiequilibrium_fert.nc','r')
eiyield3ynew = edat3.variables['g_ET'][0:115,0,:,:]
edat4=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/maiequilibrium_co2/output/maiequilibrium_co2.nc','r')
eiyield4ynew = edat4.variables['g_ET'][0:115,0,:,:]

edat5=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/maiequilibrium_cli/output/maiequilibrium_cli.nc','r')
eiyield5ynew = edat5.variables['g_ET'][0:115,0,:,:]

dat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/mai_irr_fert/output/mai_irr_fert.nc','r')
iyield1ynew = dat.variables['g_ET'][0:115,0,:,:]
latisam=dat.variables['lat'][:]
lonisam=dat.variables['lon'][:]

dat2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/mai_fert/output/mai_fert.nc','r')
iyield2ynew = dat2.variables['g_ET'][0:115,0,:,:]

dat3=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/fixedirr/mai_irr/output/mai_irr.nc','r')
iyield3ynew = dat3.variables['g_ET'][0:115,0,:,:]

dat4=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/fixedirr/mai_co2/output/mai_co2.nc','r')
iyield4ynew = dat4.variables['g_ET'][0:115,0,:,:]

dat5=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/fixedirr/mai_cli/output/mai_cli.nc','r')
iyield5ynew = dat5.variables['g_ET'][0:115,0,:,:]

iyield6ynew=N.zeros((115,360,720))
dat6=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_mai_mirca_evp.nc','r')
lonisam1=dat6.variables['lon'][:]
for z in range(0,115):
         aa= dat6.variables['yield'][z,:,:]
         maizeto1r,lonisam2=shiftgrid(0.5,aa,lonisam1,start=True)
         iyield6ynew[z,:,:] = maizeto1r


iyield1ynew= ma.masked_where(iyield1ynew<=0.,iyield1ynew)
iyield2ynew= ma.masked_where(iyield2ynew<=0.,iyield2ynew)
iyield3ynew= ma.masked_where(iyield3ynew<=0.,iyield3ynew)
iyield4ynew= ma.masked_where(iyield4ynew<=0.,iyield4ynew)
iyield5ynew= ma.masked_where(iyield5ynew<=0.,iyield5ynew)
iyield6ynew= ma.masked_where(iyield6ynew<=0.,iyield6ynew)

eiyield1ynew= ma.masked_where(eiyield1ynew<=0.,eiyield1ynew)
eiyield2ynew= ma.masked_where(eiyield2ynew<=0.,eiyield2ynew)
eiyield3ynew= ma.masked_where(eiyield3ynew<=0.,eiyield3ynew)
eiyield4ynew= ma.masked_where(eiyield4ynew<=0.,eiyield4ynew)
eiyield5ynew= ma.masked_where(eiyield5ynew<=0.,eiyield5ynew)


for i in range(1,6):
        locals()['e{0}p'.format(i)]=N.zeros((nn,year))
        locals()['e{0}y'.format(i)]=N.zeros((nn,year))
        locals()['e{0}g'.format(i)]=N.zeros((nn,year))


        locals()['e{0}'.format(i)]=region(year,locals()['eiyield{0}ynew'.format(i)])
        locals()['e{0}p'.format(i)]=locals()['e{0}'.format(i)][0]
        locals()['e{0}y'.format(i)]=locals()['e{0}'.format(i)][1]
        locals()['e{0}g'.format(i)]=locals()['e{0}'.format(i)][2]


for i in range(1,7):
        locals()['i{0}p'.format(i)]=N.zeros((nn,year))
        locals()['i{0}y'.format(i)]=N.zeros((nn,year))
        locals()['i{0}g'.format(i)]=N.zeros((nn,year))


        locals()['i{0}'.format(i)]=region(year,locals()['iyield{0}ynew'.format(i)])
        locals()['i{0}p'.format(i)]=locals()['i{0}'.format(i)][0]
        locals()['i{0}y'.format(i)]=locals()['i{0}'.format(i)][1]
        locals()['i{0}g'.format(i)]=locals()['i{0}'.format(i)][2]

ncfile=NetCDFFile('mai1901_2015regionnewmirca_evp.nc','w',format='NETCDF3_64BIT_OFFSET')
ncfile.createDimension('region', 9)
ncfile.createDimension('time', 115)

times = ncfile.createVariable('time', 'f8', ('time',))
region1 = ncfile.createVariable('region', 'f8', ('region',))
for i in range(1,7):
        if i==6:
                iallp= ncfile.createVariable('iallp', 'f8', ('region','time'),fill_value=-9999.)
                ially= ncfile.createVariable('ially', 'f8', ('region','time'),fill_value=-9999.)
                iallg= ncfile.createVariable('iallg', 'f8', ('region','time'),fill_value=-9999.)
                iallp[:]=locals()['i{0}p'.format(i)]
                ially[:]=locals()['i{0}y'.format(i)]
                iallg[:]=locals()['i{0}g'.format(i)]
	else:
		locals()['i{0}p1'.format(i)]= ncfile.createVariable('i{0}p'.format(i), 'f8', ('region','time'),fill_value=-9999.)
		locals()['i{0}y1'.format(i)]= ncfile.createVariable('i{0}y'.format(i), 'f8', ('region','time'),fill_value=-9999.)
		locals()['i{0}g1'.format(i)]= ncfile.createVariable('i{0}g'.format(i), 'f8', ('region','time'),fill_value=-9999.)
		locals()['i{0}p1'.format(i)][:]=locals()['i{0}p'.format(i)]
		locals()['i{0}y1'.format(i)][:]=locals()['i{0}y'.format(i)]
		locals()['i{0}g1'.format(i)][:]=locals()['i{0}g'.format(i)]


	 	locals()['e{0}p1'.format(i)]= ncfile.createVariable('e{0}p'.format(i), 'f8', ('region','time'),fill_value=-9999.)
	        locals()['e{0}y1'.format(i)]= ncfile.createVariable('e{0}y'.format(i), 'f8', ('region','time'),fill_value=-9999.)
	        locals()['e{0}g1'.format(i)]= ncfile.createVariable('e{0}g'.format(i), 'f8', ('region','time'),fill_value=-9999.)
	        locals()['e{0}p1'.format(i)][:]=locals()['e{0}p'.format(i)]
	        locals()['e{0}y1'.format(i)][:]=locals()['e{0}y'.format(i)]
	        locals()['e{0}g1'.format(i)][:]=locals()['e{0}g'.format(i)]



ttt= N.arange(1901,2016,1)
times[:]=ttt
region1[:] = N.arange(0,9,1)
times.long_name = '1901-2015'
ncfile.close()



