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




dat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/soy1901_2015region.nc','r')
dat1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/soyregion_rcp85new.nc','r')
dat2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/soyregion_rcp45new.nc','r')


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

        locals()['e{0}y45n'.format(i)] = N.concatenate([locals()['e{0}p'.format(i)][:,:],locals()['e{0}p45'.format(i)][:,1:86]],axis=1)
        locals()['e{0}y85n'.format(i)] = N.concatenate([locals()['e{0}p'.format(i)][:,:],locals()['e{0}p85'.format(i)][:,1:86]],axis=1)

        locals()['i{0}y45n'.format(i)] = N.concatenate([locals()['i{0}p'.format(i)][:,:],locals()['i{0}p45'.format(i)][:,1:86]],axis=1)
        locals()['i{0}y85n'.format(i)] = N.concatenate([locals()['i{0}p'.format(i)][:,:],locals()['i{0}p85'.format(i)][:,1:86]],axis=1)
'''
for i in range(1,6):
        locals()['e{0}p45n'.format(i)] = N.concatenate([locals()['e{0}p'.format(i)][:,:],locals()['e{0}p45'.format(i)][:,1:86]],axis=1)
        locals()['e{0}p85n'.format(i)] = N.concatenate([locals()['e{0}p'.format(i)][:,:],locals()['e{0}p85'.format(i)][:,1:86]],axis=1)

        locals()['i{0}p45n'.format(i)] = N.concatenate([locals()['i{0}p'.format(i)][:,:],locals()['i{0}p45'.format(i)][:,1:86]],axis=1)
        locals()['i{0}p85n'.format(i)] = N.concatenate([locals()['i{0}p'.format(i)][:,:],locals()['i{0}p85'.format(i)][:,1:86]],axis=1)

        locals()['e{0}y45n'.format(i)] = N.concatenate([locals()['e{0}y'.format(i)][:,:],locals()['e{0}y45'.format(i)][:,1:86]],axis=1)
        locals()['e{0}y85n'.format(i)] = N.concatenate([locals()['e{0}y'.format(i)][:,:],locals()['e{0}y85'.format(i)][:,1:86]],axis=1)

        locals()['i{0}y45n'.format(i)] = N.concatenate([locals()['i{0}y'.format(i)][:,:],locals()['i{0}y45'.format(i)][:,1:86]],axis=1)
        locals()['i{0}y85n'.format(i)] = N.concatenate([locals()['i{0}y'.format(i)][:,:],locals()['i{0}y85'.format(i)][:,1:86]],axis=1)
'''
dat=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/soy1901_2015regionfixedlu.nc','r')
dat1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/soyregion_rcp85fixedlu.nc','r')
dat2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/soyregion_rcp45fixedlu.nc','r')
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

        locals()['ae{0}y45n'.format(i)] = N.concatenate([locals()['ae{0}p'.format(i)][:,:],locals()['ae{0}p45'.format(i)][:,1:86]],axis=1)
        locals()['ae{0}y85n'.format(i)] = N.concatenate([locals()['ae{0}p'.format(i)][:,:],locals()['ae{0}p85'.format(i)][:,1:86]],axis=1)

        locals()['ai{0}y45n'.format(i)] = N.concatenate([locals()['ai{0}p'.format(i)][:,:],locals()['ai{0}p45'.format(i)][:,1:86]],axis=1)
        locals()['ai{0}y85n'.format(i)] = N.concatenate([locals()['ai{0}p'.format(i)][:,:],locals()['ai{0}p85'.format(i)][:,1:86]],axis=1)


#print e1p45n.shape,e1p45n[1,:]
#print e1p[1,:]
#print e1p45[1,:]

eip = (e2y-e1y)/i1y*100
efp = (e3y-e1y)/i1y*100
ecop = (e4y-e1y)/i1y*100
eclp = (e5y-e1y)/i1y*100
elup = (e1y-ae1y)/i1y*100

lup=(i1y-ai1y)/i1y*100
ip = (i1y-i2y)/i1y*100
fp = (i1y-i3y)/i1y*100
cop = (i1y-i4y)/i1y*100
clp = (i1y-i5y)/i1y*100

eip45 = (e2y45n-e1y45n)/i1y45n*100
efp45 = (e3y45n-e1y45n)/i1y45n*100
ecop45 = (e4y45n-e1y45n)/i1y45n*100
eclp45 = (e5y45n-e1y45n)/i1y45n*100
elup45= (e1y45n-ae1y45n)/i1y45n*100

ip45 = (i1y45n-i2y45n)/i1y45n*100
fp45 = (i1y45n-i3y45n)/i1y45n*100
cop45 = (i1y45n-i4y45n)/i1y45n*100
clp45 = (i1y45n-i5y45n)/i1y45n*100
lup45= (i1y45n-ai1y45n)/i1y45n*100

eip85 = (e2y85n-e1y85n)/i1y85n*100
efp85 = (e3y85n-e1y85n)/i1y85n*100
ecop85 = (e4y85n-e1y85n)/i1y85n*100
eclp85 = (e5y85n-e1y85n)/i1y85n*100
elup85= (e1y85n-ae1y85n)/i1y85n*100

ip85 = (i1y85n-i2y85n)/i1y85n*100
fp85 = (i1y85n-i3y85n)/i1y85n*100
cop85 = (i1y85n-i4y85n)/i1y85n*100
clp85 = (i1y85n-i5y85n)/i1y85n*100
lup85= (i1y85n-ai1y85n)/i1y85n*100
'''
eip45 = (e2y45n-e1y45n)
efp45 = (e3y45n-e1y45n)
ecop45 = (e4y45n-e1y45n)
eclp45 = (e5y45n-e1y45n)
elup45= (e1y45n-ae1y45n)

ip45 = (i1y45n-i2y45n)
fp45 = (i1y45n-i3y45n)
cop45 = (i1y45n-i4y45n)
clp45 = (i1y45n-i5y45n)
lup45= (i1y45n-ai1y45n)

eip85 = (e2y85n-e1y85n)
efp85 = (e3y85n-e1y85n)
ecop85 = (e4y85n-e1y85n)
eclp85 = (e5y85n-e1y85n)
elup85= (e1y85n-ae1y85n)

ip85 = (i1y85n-i2y85n)
fp85 = (i1y85n-i3y85n)
cop85 = (i1y85n-i4y85n)
clp85 = (i1y85n-i5y85n)
lup85= (i1y85n-ai1y85n)
'''
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
	if i==0:
		x1=0+10*i
	else:
		x1=(0+10*i)-1
	x=9+10*i
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
fig = plt.figure(figsize=(6,9))
n_groups = 1
index = N.arange(n_groups)
bar_width = 0.038
opacity = 1.0
name1=['CO$_{2}$','Climate','Irigation','N fertilizer']
for i in xrange(4):
	ax = fig.add_subplot(4,1,i+1)

#ax.set_xticklabels(['1960s','1970s','1980s','1990s','2000s','2010s'])
#	plt.ylim(-75, 75)
	x=i+1
	gx=xrange(1960,2101,10)
	if i==0 :
		plt.ylim(0, 60)
#		
        if i==1:
                plt.ylim(-25, 15)
        if i==2:
                plt.ylim(-10, 50)
        if i==3 :
                plt.ylim(0, 18)

	
	xy=gge[g]
	print ['e{0}p'.format(xy)]
        plt.bar(0.01+index+bar_width*1,locals()['e{0}p451'.format(xy)][0,19],bar_width,alpha=opacity,color='b')
                #plt.bar(0.01+index+bar_width*1,locals()['e{0}p851'.format(xy)][0,5:20],"k-",label="Global",linewidth=2)

        plt.bar(0.04+index+bar_width*3,locals()['e{0}p451'.format(xy)][1,19],bar_width,alpha=opacity,color='b')
        plt.bar(0.07+index+bar_width*5,locals()['e{0}p451'.format(xy)][2,19],bar_width,alpha=opacity,color='b')
        plt.bar(0.10+index+bar_width*7,locals()['e{0}p451'.format(xy)][3,19],bar_width,alpha=opacity,color='b')
        plt.bar(0.13+index+bar_width*9,locals()['e{0}p451'.format(xy)][4,19],bar_width,alpha=opacity,color='b')
        plt.bar(0.16+index+bar_width*11,locals()['e{0}p451'.format(xy)][7,19],bar_width,alpha=opacity,color='b')
        plt.bar(0.19+index+bar_width*13,locals()['e{0}p451'.format(xy)][8,19],bar_width,alpha=opacity,color='b')


	g=g+1


	xy=gge[gc]
        print ['{0}p'.format(xy)]
        plt.bar(0.01+index+bar_width*2,locals()['{0}p451'.format(xy)][0,19],bar_width,alpha=opacity,color='r')
        plt.bar(0.04+index+bar_width*4,locals()['{0}p451'.format(xy)][1,19],bar_width,alpha=opacity,color='r')
        plt.bar(0.07+index+bar_width*6,locals()['{0}p451'.format(xy)][2,19],bar_width,alpha=opacity,color='r')
        plt.bar(0.10+index+bar_width*8,locals()['{0}p451'.format(xy)][3,19],bar_width,alpha=opacity,color='r')
        plt.bar(0.13+index+bar_width*10,locals()['{0}p451'.format(xy)][4,19],bar_width,alpha=opacity,color='r')
        plt.bar(0.16+index+bar_width*12,locals()['{0}p451'.format(xy)][7,19],bar_width,alpha=opacity,color='r')
        plt.bar(0.19+index+bar_width*14,locals()['{0}p451'.format(xy)][8,19],bar_width,alpha=opacity,color='r')


        gc=gc+1

#	if i==9 or i==8:
#		plt.xlabel("Year",fontsize=12)
        plt.xticks([0.09,0.19,0.30,0.40,0.51,0.61,0.72])
        ax.set_xticklabels(["Global","NA","SA","EU","Africa","China","SSEA"])
	if i==3:
	        ax.set_xticklabels(["Global","NA","SA","EU","Africa","China","SSEA"])
	else:
		ax.set_xticklabels([])
        #plt.xticks(0.05,0.15,0.25,0.35,0.45,0.55,0.65)

        plt.ylabel("(%)",fontsize=12)

        ax.text(0.01,.83,'{0}'.format(name1[i]),fontsize=14,
                horizontalalignment='left',
                transform=ax.transAxes)
        plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom='on',      # ticks along the bottom edge are off
            top='off',         # ticks along the top edge are off
            labelbottom='on') # labels along the bottom edge are off

g=0
N.savetxt('soyrcp45.csv', (ecop451[g,19],cop451[g,19],eclp451[g,19],clp451[g,19],eip451[g,19],ip451[g,19],efp451[g,19],fp451[g,19]), delimiter=',')
N.savetxt('soyrcp85.csv', (ecop851[g,19],cop851[g,19],eclp851[g,19],clp851[g,19],eip851[g,19],ip851[g,19],efp851[g,19],fp851[g,19]), delimiter=',')


#leg = plt.legend(loc=2,ncol=5, fontsize=16)
#leg.get_frame().set_alpha(0.5)
#plt.xlabel("Year",fontsize=18)
#plt.ylabel("Production (tonnes)",fontsize=18)

#plt.tick_params(axis='both',labelsize=18)
#ax.xaxis.set_major_formatter(DateFormatter('%Y'))
plt.savefig('soy_region2090srcp45new.png',dpi=300,bbox_inches='tight')
plt.show()

