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
dat1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/soyregion_rcp85.nc','r')
dat2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/soyregion_rcp45.nc','r')


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
c=['k','b','r','g','m']
g=0
gc=0
fig = plt.figure(figsize=(8,12))
n_groups = 1
index = N.arange(n_groups)
bar_width = 0.005
opacity = 1
for i in xrange(9):
	ax = fig.add_subplot(5,2,i+1)
        ax.spines['bottom'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.yaxis.set_ticks_position('left')
        ax.text(0.05,.03,'{0}'.format(name[i]),fontsize=12,
                horizontalalignment='left',
                transform=ax.transAxes)
#	ax.set_title('{0}'.format(name[i]),fontsize=12)
        ax.tick_params(labelsize=12)
        plt.ylim(-30, 60)
        ax.set_yticks([-30,-15,0,15,30,45,60 ])
	ax.set_xticks([0.015,0.025,0.035,0.045,0.055])
#        if idx==0 or idx==3 or idx==6:
        ax.set_xticklabels(["CO$_{2}$","Climate","Irrig","NF","Land"])
        plt.tick_params(
                    axis='x',          # changes apply to the x-axis
                    which='both',      # both major and minor ticks are affected
                    bottom='on',      # ticks along the bottom edge are off
                    top='off',         # ticks along the top edge are off
                    labelbottom='on') # labels along the bottom edge are off


	gc=0
	x=i+1
	for j in range(0,5):
		xy=gge[gc]
		cc=c[gc]
		if j==0:
			x1=0
			xx=1
		else:
			x1=j*2
			xx=x1+1
                print ['{0}p'.format(xy)]
                plt.bar(0.01+index+bar_width*x1,locals()['{0}p451'.format(xy)][i,19],bar_width,hatch='x',facecolor='none',alpha=opacity,edgecolor=['{0}'.format(cc)])

                plt.bar(0.01+index+bar_width*xx,locals()['{0}p851'.format(xy)][i,19],bar_width,color=['{0}'.format(cc)],alpha=opacity)

#                plt.bar(0.01+index+bar_width*x1,locals()['{0}p451'.format(xy)][i,19],bar_width,alpha=opacity,color=['{0}'.format(cc)],hatch='..')
#                plt.bar(0.01+index+bar_width*xx,locals()['{0}p851'.format(xy)][i,19],bar_width,alpha=opacity,color=['{0}'.format(cc)])
                gc=gc+1

plt.savefig('soy_regiontime10barfuturelu.png',dpi=300,bbox_inches='tight')
plt.show()

