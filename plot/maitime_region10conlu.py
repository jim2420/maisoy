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




dat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/mai1901_2015region.nc','r')
dat1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/mairegion_rcp85.nc','r')
dat2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/mairegion_rcp45.nc','r')


for i in range(1,6):
	locals()['e{0}p'.format(i)] = dat.variables['e{0}p'.format(i)][:,:]
        locals()['e{0}y'.format(i)] = dat.variables['e{0}y'.format(i)][:,:]
        locals()['e{0}g'.format(i)] = dat.variables['e{0}g'.format(i)][:,:]

        locals()['e{0}p85'.format(i)] = dat1.variables['e{0}p'.format(i)][:,:]
        locals()['e{0}y85'.format(i)] = dat1.variables['e{0}y'.format(i)][:,:]
        locals()['e{0}g85'.format(i)] = dat1.variables['e{0}g'.format(i)][:,:]

        locals()['e{0}p45'.format(i)] = dat2.variables['e{0}p'.format(i)][:,:]
        locals()['e{0}y45'.format(i)] = dat2.variables['e{0}y'.format(i)][:,:]
        locals()['e{0}g45'.format(i)] = dat2.variables['e{0}g'.format(i)][:,:]

        locals()['i{0}p'.format(i)] = dat.variables['i{0}p'.format(i)][:,:]
        locals()['i{0}y'.format(i)] = dat.variables['i{0}y'.format(i)][:,:]
        locals()['i{0}g'.format(i)] = dat.variables['i{0}g'.format(i)][:,:]

        locals()['i{0}p85'.format(i)] = dat1.variables['i{0}p'.format(i)][:,:]
        locals()['i{0}y85'.format(i)] = dat1.variables['i{0}y'.format(i)][:,:]
        locals()['i{0}g85'.format(i)] = dat1.variables['i{0}g'.format(i)][:,:]

        locals()['i{0}p45'.format(i)] = dat2.variables['i{0}p'.format(i)][:,:]
        locals()['i{0}y45'.format(i)] = dat2.variables['i{0}y'.format(i)][:,:]
        locals()['i{0}g45'.format(i)] = dat2.variables['i{0}g'.format(i)][:,:]

for i in range(1,6):
        locals()['e{0}p45n'.format(i)] = N.concatenate([locals()['e{0}p'.format(i)][:,:],locals()['e{0}p45'.format(i)][:,1:86]],axis=1)
        locals()['e{0}p85n'.format(i)] = N.concatenate([locals()['e{0}p'.format(i)][:,:],locals()['e{0}p85'.format(i)][:,1:86]],axis=1)

        locals()['i{0}p45n'.format(i)] = N.concatenate([locals()['i{0}p'.format(i)][:,:],locals()['i{0}p45'.format(i)][:,1:86]],axis=1)
        locals()['i{0}p85n'.format(i)] = N.concatenate([locals()['i{0}p'.format(i)][:,:],locals()['i{0}p85'.format(i)][:,1:86]],axis=1)


dat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/mai1901_2015regionfixedlu.nc','r')
dat1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/mairegion_rcp85fixedlu.nc','r')
dat2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/mairegion_rcp45fixedlu.nc','r')
for i in range(1,6):
        locals()['ae{0}p'.format(i)] = dat.variables['e{0}p'.format(i)][:,:]
        locals()['ae{0}y'.format(i)] = dat.variables['e{0}y'.format(i)][:,:]
        locals()['ae{0}g'.format(i)] = dat.variables['e{0}g'.format(i)][:,:]

        locals()['ae{0}p85'.format(i)] = dat1.variables['e{0}p'.format(i)][:,:]
        locals()['ae{0}y85'.format(i)] = dat1.variables['e{0}y'.format(i)][:,:]
        locals()['ae{0}g85'.format(i)] = dat1.variables['e{0}g'.format(i)][:,:]

        locals()['ae{0}p45'.format(i)] = dat2.variables['e{0}p'.format(i)][:,:]
        locals()['ae{0}y45'.format(i)] = dat2.variables['e{0}y'.format(i)][:,:]
        locals()['ae{0}g45'.format(i)] = dat2.variables['e{0}g'.format(i)][:,:]

        locals()['ai{0}p'.format(i)] = dat.variables['i{0}p'.format(i)][:,:]
        locals()['ai{0}y'.format(i)] = dat.variables['i{0}y'.format(i)][:,:]
        locals()['ai{0}g'.format(i)] = dat.variables['i{0}g'.format(i)][:,:]

        locals()['ai{0}p85'.format(i)] = dat1.variables['i{0}p'.format(i)][:,:]
        locals()['ai{0}y85'.format(i)] = dat1.variables['i{0}y'.format(i)][:,:]
        locals()['ai{0}g85'.format(i)] = dat1.variables['i{0}g'.format(i)][:,:]

        locals()['ai{0}p45'.format(i)] = dat2.variables['i{0}p'.format(i)][:,:]
        locals()['ai{0}y45'.format(i)] = dat2.variables['i{0}y'.format(i)][:,:]
        locals()['ai{0}g45'.format(i)] = dat2.variables['i{0}g'.format(i)][:,:]

for i in range(1,6):
        locals()['ae{0}p45n'.format(i)] = N.concatenate([locals()['ae{0}p'.format(i)][:,:],locals()['ae{0}p45'.format(i)][:,1:86]],axis=1)
        locals()['ae{0}p85n'.format(i)] = N.concatenate([locals()['ae{0}p'.format(i)][:,:],locals()['ae{0}p85'.format(i)][:,1:86]],axis=1)

        locals()['ai{0}p45n'.format(i)] = N.concatenate([locals()['ai{0}p'.format(i)][:,:],locals()['ai{0}p45'.format(i)][:,1:86]],axis=1)
        locals()['ai{0}p85n'.format(i)] = N.concatenate([locals()['ai{0}p'.format(i)][:,:],locals()['ai{0}p85'.format(i)][:,1:86]],axis=1)



#print e1p45n.shape,e1p45n[1,:]
#print e1p[1,:]
#print e1p45[1,:]

eip = (e2p-e1p)/i1p*100
efp = (e3p-e1p)/i1p*100
ecop = (e4p-e1p)/i1p*100
eclp = (e5p-e1p)/i1p*100
elup = (e1p-ae1p)/i1p*100

lup=(i1p-ai1p)/i1p*100
ip = (i1p-i2p)/i1p*100
fp = (i1p-i3p)/i1p*100
cop = (i1p-i4p)/i1p*100
clp = (i1p-i5p)/i1p*100

eip45 = (e2p45n-e1p45n)/i1p45n*100
efp45 = (e3p45n-e1p45n)/i1p45n*100
ecop45 = (e4p45n-e1p45n)/i1p45n*100
eclp45 = (e5p45n-e1p45n)/i1p45n*100
elup45= (e1p45n-ae1p45n)/i1p45n*100

ip45 = (i1p45n-i2p45n)/i1p45n*100
fp45 = (i1p45n-i3p45n)/i1p45n*100
cop45 = (i1p45n-i4p45n)/i1p45n*100
clp45 = (i1p45n-i5p45n)/i1p45n*100
lup45= (i1p45n-ai1p45n)/i1p45n*100

eip85 = (e2p85n-e1p85n)/i1p85n*100
efp85 = (e3p85n-e1p85n)/i1p85n*100
ecop85 = (e4p85n-e1p85n)/i1p85n*100
eclp85 = (e5p85n-e1p85n)/i1p85n*100
elup85= (e1p85n-ae1p85n)/i1p85n*100

ip85 = (i1p85n-i2p85n)/i1p85n*100
fp85 = (i1p85n-i3p85n)/i1p85n*100
cop85 = (i1p85n-i4p85n)/i1p85n*100
clp85 = (i1p85n-i5p85n)/i1p85n*100
lup85= (i1p85n-ai1p85n)/i1p85n*100

eip451=N.zeros((9,20))
efp451=N.zeros((9,20))
ecop451=N.zeros((9,20))
eclp451=N.zeros((9,20))
elup451=N.zeros((9,20))

eip851=N.zeros((9,20))
efp851=N.zeros((9,20))
ecop851=N.zeros((9,20))
eclp851=N.zeros((9,20))
elup851=N.zeros((9,20))

ip451=N.zeros((9,20))
fp451=N.zeros((9,20))
cop451=N.zeros((9,20))
clp451=N.zeros((9,20))
lup451=N.zeros((9,20))

ip851=N.zeros((9,20))
fp851=N.zeros((9,20))
cop851=N.zeros((9,20))
clp851=N.zeros((9,20))
lup851=N.zeros((9,20))


for i in range(0,20):
	x1=0+10*i
	x=10+10*i
	eip451[:,i]=N.average(eip45[:,x1:x],axis=1)
        efp451[:,i]=N.average(efp45[:,x1:x],axis=1)
        ecop451[:,i]=N.average(ecop45[:,x1:x],axis=1)
        eclp451[:,i]=N.average(eclp45[:,x1:x],axis=1)
        elup451[:,i]=N.average(elup45[:,x1:x],axis=1)

        ip451[:,i]=N.average(ip45[:,x1:x],axis=1)
        fp451[:,i]=N.average(fp45[:,x1:x],axis=1)
        cop451[:,i]=N.average(cop45[:,x1:x],axis=1)
        clp451[:,i]=N.average(clp45[:,x1:x],axis=1)
        lup451[:,i]=N.average(lup45[:,x1:x],axis=1)


        eip851[:,i]=N.average(eip85[:,x1:x],axis=1)
        efp851[:,i]=N.average(efp85[:,x1:x],axis=1)
        ecop851[:,i]=N.average(ecop85[:,x1:x],axis=1)
        eclp851[:,i]=N.average(eclp85[:,x1:x],axis=1)
        elup851[:,i]=N.average(elup85[:,x1:x],axis=1)


        ip851[:,i]=N.average(ip85[:,x1:x],axis=1)
        fp851[:,i]=N.average(fp85[:,x1:x],axis=1)
        cop851[:,i]=N.average(cop85[:,x1:x],axis=1)
        clp851[:,i]=N.average(clp85[:,x1:x],axis=1)
        lup851[:,i]=N.average(lup85[:,x1:x],axis=1)


name=["Global","NA","SA","EU","Africa","PD","USSR","China","SSEA"]

gge=['co','cl','i','f','lu']
g=0
gc=0
fig = plt.figure(figsize=(12,8))
n_groups = 5
index = N.arange(n_groups)
bar_width = 0.11
opacity = 0.6

for i in xrange(10):
	ax = fig.add_subplot(5,2,i+1)

#ax.set_xticklabels(['1960s','1970s','1980s','1990s','2000s','2010s'])
#	plt.ylim(-75, 75)
	x=i+1
	gx=xrange(1960,2101,10)
	if i==0 or i==1:
		plt.ylim(0, 20)
		
        if i==2 or i==3:
                plt.ylim(-30, 25)
        if i==4 or i==5:
                plt.ylim(0, 60)
        if i==6 or i==7:
                plt.ylim(0, 25)
        if i==8 or i==9:
                plt.ylim(-20, 90)

	
	if i==0 or i==2 or i==4 or i==6 or i==8: 
		xy=gge[g]
		print ['e{0}p'.format(xy)]
                plt.bar(0.01+index+bar_width*1,locals()['e{0}p451'.format(xy)][0,5:10],bar_width,alpha=opacity,color='black')
                #plt.bar(0.01+index+bar_width*1,locals()['e{0}p851'.format(xy)][0,5:20],"k-",label="Global",linewidth=2)

                plt.bar(0.01+index+bar_width*2,locals()['e{0}p451'.format(xy)][1,5:10],bar_width,alpha=opacity,color='r')
                plt.bar(0.01+index+bar_width*3,locals()['e{0}p451'.format(xy)][2,5:10],bar_width,alpha=opacity,color='y')
                plt.bar(0.01+index+bar_width*4,locals()['e{0}p451'.format(xy)][3,5:10],bar_width,alpha=opacity,color='m')
                plt.bar(0.01+index+bar_width*5,locals()['e{0}p451'.format(xy)][4,5:10],bar_width,alpha=opacity,color='c')
                plt.bar(0.01+index+bar_width*6,locals()['e{0}p451'.format(xy)][7,5:10],bar_width,alpha=opacity,color='b')
                plt.bar(0.01+index+bar_width*7,locals()['e{0}p451'.format(xy)][8,5:10],bar_width,alpha=opacity,color='g')


		#plt.bar(0.01+index+bar_width*1,locals()['e{0}p851'.format(xy)][1,5:20],"r-",label="NA",linewidth=1)
		#plt.bar(0.01+index+bar_width*1,locals()['e{0}p851'.format(xy)][2,5:20],"y-",label="SA",linewidth=1)

		#plt.bar(0.01+index+bar_width*1,locals()['e{0}p851'.format(xy)][3,5:20],"m-",label="EU",linewidth=1)
		#plt.bar(0.01+index+bar_width*1,locals()['e{0}p851'.format(xy)][4,5:20],"c-",label="Africa",linewidth=1)

		#plt.bar(0.01+index+bar_width*1,locals()['e{0}p851'.format(xy)][7,5:20],"b-",label="China",linewidth=1)
		#plt.bar(0.01+index+bar_width*1,locals()['e{0}p851'.format(xy)][8,5:20],"g-",label="SSEA",linewidth=1)
		g=g+1
#		plt.xticks(index + bar_width+0.37, ('1960s','1970s','1980s','1990s','2000s'))

	elif i==1 or i==3 or i==5 or i==7 or i==9:
#                ax.set_yticklabels([])

		xy=gge[gc]
                print ['{0}p'.format(xy)]
                plt.bar(0.01+index+bar_width*1,locals()['{0}p451'.format(xy)][0,5:10],bar_width,alpha=opacity,color='k')
                #plt.bar(0.01+index+bar_width*1,locals()['{0}p851'.format(xy)][0,5:20],"k-",label="Global",linewidth=2)


                plt.bar(0.01+index+bar_width*2,locals()['{0}p451'.format(xy)][1,5:10],bar_width,alpha=opacity,color='r')
                plt.bar(0.01+index+bar_width*3,locals()['{0}p451'.format(xy)][2,5:10],bar_width,alpha=opacity,color='y')
                plt.bar(0.01+index+bar_width*4,locals()['{0}p451'.format(xy)][3,5:10],bar_width,alpha=opacity,color='m')
                plt.bar(0.01+index+bar_width*5,locals()['{0}p451'.format(xy)][4,5:10],bar_width,alpha=opacity,color='c')
                plt.bar(0.01+index+bar_width*6,locals()['{0}p451'.format(xy)][7,5:10],bar_width,alpha=opacity,color='b')
                plt.bar(0.01+index+bar_width*7,locals()['{0}p451'.format(xy)][8,5:10],bar_width,alpha=opacity,color='g')


                #plt.bar(0.01+index+bar_width*1,locals()['{0}p851'.format(xy)][1,5:20],"r-",label="NA",linewidth=1)
                #plt.bar(0.01+index+bar_width*1,locals()['{0}p851'.format(xy)][2,5:20],"y-",label="SA",linewidth=1)
                #plt.bar(0.01+index+bar_width*1,locals()['{0}p851'.format(xy)][3,5:20],"m-",label="EU",linewidth=1)
                #plt.bar(0.01+index+bar_width*1,locals()['{0}p851'.format(xy)][4,5:20],"c-",label="Africa",linewidth=1)
                #plt.bar(0.01+index+bar_width*1,locals()['{0}p851'.format(xy)][7,5:20],"b-",label="China",linewidth=1)
                #plt.bar(0.01+index+bar_width*1,locals()['{0}p851'.format(xy)][8,5:20],"g-",label="SSEA",linewidth=1)
                gc=gc+1
#                plt.xticks(index + bar_width+0.37, ('1960s','1970s','1980s','1990s','2000s'))

	if i==9 or i==8:
#		plt.xlabel("Year",fontsize=12)
                plt.xticks(index + bar_width+0.4, ('1960s','1970s','1980s','1990s','2000s'))

	else:
		ax.set_xticklabels([])
                plt.xticks(index + bar_width+0.4)

        if i==0:
                plt.title("Direct effect",fontsize=12)
		plt.ylabel("CO2 (%)",fontsize=12)
        if i==1:
                plt.title("Direct X Interactive effect",fontsize=12)

        if i==2:
                plt.ylabel("Climate (%)",fontsize=12)

        if i==4:
                plt.ylabel("Irrigation (%)",fontsize=12)

        if i==6:
                plt.ylabel("N fertilizer (%)",fontsize=12)
        if i==8:
                plt.ylabel("Land (%)",fontsize=12)


#leg = plt.legend(loc=2,ncol=5, fontsize=16)
#leg.get_frame().set_alpha(0.5)
#plt.xlabel("Year",fontsize=18)
#plt.ylabel("Production (tonnes)",fontsize=18)

#plt.tick_params(axis='both',labelsize=18)
#ax.xaxis.set_major_formatter(DateFormatter('%Y'))
plt.savefig('maize_regiontime10barlu.png',dpi=300,bbox_inches='tight')
plt.show()

