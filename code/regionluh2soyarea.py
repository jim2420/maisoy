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
	meareaisam = isam1.variables['fsoy_tt'][1051:1166,:,:]#1901-2015
	meareaisam= ma.masked_where(meareaisam<=0.0,meareaisam)

        isam1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/luh2area_850_2015_corrcrop.nc','r')
        meareaisam1 = isam1.variables['fsoy_tt'][1051,:,:]#1901
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
	        isampmask=isamp
	        isamarea=meareaisam

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
	return allproisam,allyisam,luharea

nn=9
year=115


dat=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/luh2NFrate_850_2015_cropfinal.nc','r')
iyield1ynew = dat.variables['soynf'][1051:1166,:,:]
latisam=dat.variables['lat'][:]
lonisam=dat.variables['lon'][:]



iyield1ynew= ma.masked_where(iyield1ynew<=0.,iyield1ynew)



for i in range(1,2):
        locals()['i{0}p'.format(i)]=N.zeros((nn,year))
        locals()['i{0}y'.format(i)]=N.zeros((nn,year))
        locals()['i{0}g'.format(i)]=N.zeros((nn,year))


        locals()['i{0}'.format(i)]=region(year,locals()['iyield{0}ynew'.format(i)])
        locals()['i{0}p'.format(i)]=locals()['i{0}'.format(i)][0]
        locals()['i{0}y'.format(i)]=locals()['i{0}'.format(i)][1]
        locals()['i{0}g'.format(i)]=locals()['i{0}'.format(i)][2]

ncfile=NetCDFFile('soy1901_2015regionNF.nc','w',format='NETCDF3_64BIT_OFFSET')
ncfile.createDimension('region', 9)
ncfile.createDimension('time', 115)

times = ncfile.createVariable('time', 'f8', ('time',))
region1 = ncfile.createVariable('region', 'f8', ('region',))
for i in range(1,2):
	locals()['i{0}p1'.format(i)]= ncfile.createVariable('i{0}p'.format(i), 'f8', ('region','time'),fill_value=-9999.)
	locals()['i{0}y1'.format(i)]= ncfile.createVariable('i{0}y'.format(i), 'f8', ('region','time'),fill_value=-9999.)
	locals()['i{0}g1'.format(i)]= ncfile.createVariable('i{0}g'.format(i), 'f8', ('region','time'),fill_value=-9999.)
	locals()['i{0}p1'.format(i)][:]=locals()['i{0}p'.format(i)]
	locals()['i{0}y1'.format(i)][:]=locals()['i{0}y'.format(i)]
	locals()['i{0}g1'.format(i)][:]=locals()['i{0}g'.format(i)]




ttt= N.arange(1901,2016,1)
times[:]=ttt
region1[:] = N.arange(0,9,1)
times.long_name = '1901-2015'
i1g1.long_name = 'ha'
i1p1.long_name = 'kgN'
i1y1.long_name ='kgN/ha'

ncfile.close()



