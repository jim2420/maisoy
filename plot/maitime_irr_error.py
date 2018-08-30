from mpl_toolkits.basemap import Basemap, cm, shiftgrid,interp
from netCDF4 import Dataset as NetCDFFile
import numpy as N
import matplotlib.pyplot as plt
import glob
import numpy.ma as ma
from scipy.interpolate import griddata
import matplotlib.colors as colors
from matplotlib.dates import DateFormatter
import datetime


area1=NetCDFFile('/project/projectdirs/m1602/datasets4.full/surfdata_05x05.nc','r')
mask = area1.variables['REGION_MASK_CRU_NCEP'][:,:]

area=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/gridareahalf_isam.nc','r')
gridarea1= area.variables['cell_area'][:,:]
gridlon = area.variables['lon'][:]
gridlat=area.variables['lat'][:]
#print gridlon
nclu=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/m3yield_isam.nc','r')
ncvar_maize = nclu.variables['maizey'][0,:,:]
marea = nclu.variables['maize_area'][0,:,:]





region1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_mai_luh2.nc','r')
maitrop = region1.variables['area'][:,:,:]
lonisam1=region1.variables['lon'][:]
maitrop=ma.masked_where(maitrop<=0,maitrop)
maitrop=ma.filled(maitrop, fill_value=0.)

maizeto = maitrop

edat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/maiequilibrium/output/maiequilibrium_irr.nc','r')
eiyield1ynew = edat.variables['irrigation'][0:115,0,:,:]

edat2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/maiequilibrium_irr/output/maiequilibrium_irr_irr.nc','r')
eiyield2ynew = edat2.variables['irrigation'][0:115,0,:,:]

edat3=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/maiequilibrium_fert/output/maiequilibrium_fert_irr.nc','r')
eiyield3ynew = edat3.variables['irrigation'][0:115,0,:,:]

edat4=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/maiequilibrium_co2/output/maiequilibrium_co2_irr.nc','r')
eiyield4ynew = edat4.variables['irrigation'][0:115,0,:,:]

edat5=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/maiequilibrium_cli/output/maiequilibrium_cli_irr.nc','r')
eiyield5ynew = edat5.variables['irrigation'][0:115,0,:,:]
 



dat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/mai_irr_fert/output/mai_irr_fert_irr.nc','r')
iyield1ynew = dat.variables['irrigation'][0:115,0,:,:]
latisam=dat.variables['lat'][:]
lonisam=dat.variables['lon'][:]
dat2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/mai_fert/output/mai_fert_irr.nc','r')
iyield2ynew = dat2.variables['irrigation'][0:115,0,:,:]

dat3=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/mai_irr/output/mai_irr_irr.nc','r')
iyield3ynew = dat3.variables['irrigation'][0:115,0,:,:]

dat4=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/mai_co2/output/mai_co2_irr.nc','r')
iyield4ynew = dat4.variables['irrigation'][0:115,0,:,:]

dat5=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/mai_cli/output/mai_cli_irr.nc','r')
iyield5ynew = dat5.variables['irrigation'][0:115,0,:,:]




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


maizeto1,lonisam2=shiftgrid(0.5,maizeto,lonisam1,start=True)
maizeto1r,lonisam2=shiftgrid(0.5,maitrop,lonisam1,start=True)

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


x=115
#print iyield1ynew.shape
mmarea=N.zeros((x,360,720))
rmask=N.zeros((x,360,720))
m3maize=N.zeros((x,360,720))
maizeto2=N.zeros((x,360,720))
maizeto2r=N.zeros((x,360,720))
maizeto2i=N.zeros((x,360,720))
maizete2r=N.zeros((x,360,720))
maizete2i=N.zeros((x,360,720))
landfrac2=N.zeros((x,360,720))
gridarea2=N.zeros((x,360,720))
for i in range(0,x):
	for x in range(0,360):
		for y in range(0,720):
			mmarea[i,x,y]=marea[x,y]
                        rmask[i,x,y]=mask[x,y]
                        m3maize[i,x,y]=ncvar_maize[x,y] 
			maizeto2[i,x,y]=maizeto1[i,x,y]
                        maizeto2r[i,x,y]=maizeto1r[i,x,y]
                        gridarea2[i,x,y]=gridarea1[x,y]

iyield1ynew= ma.masked_where(maizeto2<=0.,iyield1ynew)
iyield2ynew= ma.masked_where(maizeto2<=0.,iyield2ynew)
iyield3ynew= ma.masked_where(maizeto2<=0.,iyield3ynew)
iyield4ynew= ma.masked_where(maizeto2<=0.,iyield4ynew)
iyield5ynew= ma.masked_where(maizeto2<=0.,iyield5ynew)
#iyield6ynew= ma.masked_where(maizeto2<=0.,iyield6ynew)

eiyield1ynew= ma.masked_where(maizeto2<=0.,eiyield1ynew)
eiyield2ynew= ma.masked_where(maizeto2<=0.,eiyield2ynew)
eiyield3ynew= ma.masked_where(maizeto2<=0.,eiyield3ynew)
eiyield4ynew= ma.masked_where(maizeto2<=0.,eiyield4ynew)
eiyield5ynew= ma.masked_where(maizeto2<=0.,eiyield5ynew)



ii=N.zeros((9))
nn=N.zeros((9))
co=N.zeros((9))
cli=N.zeros((9))
sii=N.zeros((9))
snn=N.zeros((9))
sco=N.zeros((9))
scli=N.zeros((9))

eii=N.zeros((9))
enn=N.zeros((9))
eco=N.zeros((9))
ecli=N.zeros((9))
esii=N.zeros((9))
esnn=N.zeros((9))
esco=N.zeros((9))
escli=N.zeros((9))


allynew=N.sum(iyield1ynew,axis=(1,2))
allyinew=N.sum(iyield2ynew,axis=(1,2))
allynnew=N.sum(iyield3ynew,axis=(1,2))
allycnew=N.sum(iyield4ynew,axis=(1,2))
allyclinew=N.sum(iyield5ynew,axis=(1,2))

eallynew=N.sum(eiyield1ynew,axis=(1,2))
eallyinew=N.sum(eiyield2ynew,axis=(1,2))
eallynnew=N.sum(eiyield3ynew,axis=(1,2))
eallycnew=N.sum(eiyield4ynew,axis=(1,2))
eallyclinew=N.sum(eiyield5ynew,axis=(1,2))
a1=1960
a2=2016
a11=a1-1901
a12=a2-1901
avs1=N.zeros(8)
avs2=N.zeros(8)
avs3=N.zeros(8)
avs4=N.zeros(8)
avs5=N.zeros(8)

eavs1=N.zeros(8)
eavs2=N.zeros(8)
eavs3=N.zeros(8)
eavs4=N.zeros(8)
eavs5=N.zeros(8)

av1=N.zeros(8)
av2=N.zeros(8)
av3=N.zeros(8)
av4=N.zeros(8)
av5=N.zeros(8)

eav1=N.zeros(8)
eav2=N.zeros(8)
eav3=N.zeros(8)
eav4=N.zeros(8)
eav5=N.zeros(8)
#decadal average
for i in range (0,6):
	c1=a11+i*10
	if i<=4:
		c2=c1+10
	else:
	        c2=c1+6
	av1[i+1]=N.average(allynew[c1:c2])
        av2[i+1]=N.average(allyinew[c1:c2])
        av3[i+1]=N.average(allynnew[c1:c2])
        av4[i+1]=N.average(allycnew[c1:c2])
        av5[i+1]=N.average(allyclinew[c1:c2])

        eav1[i+1]=N.average(eallynew[c1:c2])
        eav2[i+1]=N.average(eallyinew[c1:c2])
        eav3[i+1]=N.average(eallynnew[c1:c2])
        eav4[i+1]=N.average(eallycnew[c1:c2])
        eav5[i+1]=N.average(eallyclinew[c1:c2])
        avs1[i+1]=N.std(allynew[c1:c2])
        avs2[i+1]=N.std(allyinew[c1:c2])
        avs3[i+1]=N.std(allynnew[c1:c2])
        avs4[i+1]=N.std(allycnew[c1:c2])
        avs5[i+1]=N.std(allyclinew[c1:c2])

        eavs1[i+1]=N.std(eallynew[c1:c2])
        eavs2[i+1]=N.std(eallyinew[c1:c2])
        eavs3[i+1]=N.std(eallynnew[c1:c2])
        eavs4[i+1]=N.std(eallycnew[c1:c2])
        eavs5[i+1]=N.std(eallyclinew[c1:c2])


#	print c1,c2	
#av1=ma.masked_where(av1<=0,av1)
#av2=ma.masked_where(av2<=0,av2)
#av3=ma.masked_where(av3<=0,av3)
#av4=ma.masked_where(av4<=0,av4)
#av5=ma.masked_where(av5<=0,av5)
#eav1=ma.masked_where(eav1<=0,eav1)
#eav2=ma.masked_where(eav2<=0,eav2)
#eav3=ma.masked_where(eav3<=0,eav3)
#eav4=ma.masked_where(eav4<=0,eav4)
#eav5=ma.masked_where(eav5<=0,eav5)

#av1=ma.filled(av1, fill_value='nan')
#av2=ma.filled(av2, fill_value='nan')
#av3=ma.filled(av3, fill_value='nan')
#av4=ma.filled(av4, fill_value='nan')
#av5=ma.filled(av5, fill_value='nan')

#eav1=ma.filled(eav1, fill_value='nan')
#eav2=ma.filled(eav2, fill_value='nan')
#eav3=ma.filled(eav3, fill_value='nan')
#eav4=ma.filled(eav4, fill_value='nan')
#eav5=ma.filled(eav5, fill_value='nan')
av1[0]='nan'
av2[0]='nan'
av3[0]='nan'
av4[0]='nan'
av5[0]='nan'
eav1[0]='nan'
eav2[0]='nan'
eav3[0]='nan'
eav4[0]='nan'
eav5[0]='nan'

av1[7]='nan'
av2[7]='nan'
av3[7]='nan'
av4[7]='nan'
av5[7]='nan'
eav1[7]='nan'
eav2[7]='nan'
eav3[7]='nan'
eav4[7]='nan'
eav5[7]='nan'





fig = plt.figure(figsize=(11.5,8))
ax = fig.add_subplot(111)

xx=range(a1,a2)
xdates = [datetime.datetime.strptime(str(int(date)),'%Y') for date in xx]
#gx=['1960s','1970s','1980s','1990s','2000s','2010s']
gx=range(-1,7)
ax.set_xticks([0,1,2,3,4,5])

ax.set_xticklabels(['1960s','1970s','1980s','1990s','2000s','2010s'])
plt.xlim(-1, 6)

linestyle = {"linestyle":"-", "linewidth":2, "markeredgewidth":2, "elinewidth":2, "capsize":2}
linestyle1 = {"linestyle":"--", "linewidth":2, "markeredgewidth":2, "elinewidth":2, "capsize":2}

ax.errorbar(gx, av1, yerr = avs1, color="y", label="S (Base)",**linestyle)
#ax.errorbar(gx, eav1, yerr = eavs1, color="y",label="Equili", **linestyle1)

#ax.errorbar(gx, av2, yerr = avs2, color="r",label="S_Irri", **linestyle)
ax.errorbar(gx, eav2, yerr = eavs2, color="r",label="E_Irri", **linestyle1)

ax.errorbar(gx, av3, yerr = avs3, color="g", label="S_N",**linestyle)
#ax.errorbar(gx, eav3, yerr = eavs3, color="g",label="E_N", **linestyle1)

ax.errorbar(gx, av4, yerr = avs4, color="k",label="S_CO$_{2}$", **linestyle)
#ax.errorbar(gx, eav4, yerr = eavs4, color="k", label="E_CO$_{2}$",**linestyle1)

ax.errorbar(gx, av5, yerr = avs5, color="b", label="S_Cli",**linestyle)
#ax.errorbar(gx, eav5, yerr = eavs5, color="b",label="E_Cli", **linestyle1)



#ax.plot(gx,av1,"yo-",label="S (Base)",linewidth=2)
##ax.plot(gx,eav1,"yo--",label="Equilibrium",linewidth=2)

##ax.plot(gx,av2,"ro-",label="S_Irri",linewidth=2)
#ax.plot(gx,eav2,"ro--",label="E_Irri",linewidth=2)

#ax.plot(gx,av3,"go-",label="S_N",linewidth=2)
##ax.plot(gx,eav3,"go--",label="E_N",linewidth=2)

#ax.plot(gx,av4,"ko-",label="S_CO$_{2}$",linewidth=2)
##ax.plot(gx,eav4,"ko--",label="E_CO$_{2}$",linewidth=2)

#ax.plot(gx,av5,"bo-",label="S_Cli",linewidth=2)
##ax.plot(gx,eav5,"bo--",label="E_Cli",linewidth=2)


#ax.plot_date(xdates,allynew[a11:a12],"y-",label="S (Base)")
#ax.plot_date(xdates,allyinew[a11:a12],"r-",label="S_Irri")
#ax.plot_date(xdates,allynnew[a11:a12],"g-",label="S_N")
#ax.plot_date(xdates,allycnew[a11:a12],"k-",label="S_CO$_{2}$")
#ax.plot_date(xdates,allyclinew[a11:a12],"b-",label="S_cli")

#ax.plot_date(xdates,eallynew[a11:a12],"y:",label="Equili")
#ax.plot_date(xdates,eallyinew[a11:a12],"r:",label="E_Irri")
#ax.plot_date(xdates,eallynnew[a11:a12],"g:",label="E_N")
#ax.plot_date(xdates,eallycnew[a11:a12],"k:",label="E_CO$_{2}$")
#ax.plot_date(xdates,eallyclinew[a11:a12],"b:",label="E_cli")



leg = plt.legend(loc=2,ncol=5, fontsize=16)
leg.get_frame().set_alpha(0.5)
#plt.xlabel("Year",fontsize=18)
plt.ylabel("Irrigation (mm)",fontsize=18)

plt.tick_params(axis='both',labelsize=18)
#ax.xaxis.set_major_formatter(DateFormatter('%Y'))
plt.savefig('maize_yearirr_error.png',dpi=300,bbox_inches='tight')
plt.show()

