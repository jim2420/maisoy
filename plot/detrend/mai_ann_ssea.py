from mpl_toolkits.basemap import Basemap, cm, shiftgrid,interp
from netCDF4 import Dataset as NetCDFFile
import numpy as N
import matplotlib.pyplot as plt
import glob
import numpy.ma as ma
from scipy.interpolate import griddata
import scipy.stats
from matplotlib.dates import DateFormatter
import datetime


def runmean(x,input):
        import pandas as pd
        #mean_zumiy1 = pd.rolling_mean(zumiy, window=5).shift(-2)
        meanout=pd.rolling_mean(input, window=5, center=True)
        mean_zumiy1=pd.rolling_mean(input, window=3, center=True)
        #print mean_zumiy1
        #print meanout
        meanout[1]=mean_zumiy1[1]
        meanout[x-2]=mean_zumiy1[x-2]
        meanout1=input-meanout
        return meanout1

a1=1961
a2=2016
x=a2-a1
faoy=N.zeros(x)
isamy=N.zeros(x)
isamy=[1.987,1.869,1.863,1.879,1.777,1.827,1.925,1.88,1.849,1.932,2.089,1.861,2.017,1.856,2.173,2.047,1.999,2.07,1.875,2.043,2.113,1.866,1.985,2.135,1.961,2.052,1.749,2.046,2.238,2.114,1.924,1.932,2.109,2.184,1.985,2.136,1.989,1.845,2.091,2.218,2.209,1.878,2.11,2.081,2.11,2.167,2.056,2.205,1.951,2.053,2.296,1.937,2.2,1.881,2.048]
faoy=[0.99316908,1.032584509,1.029537587,1.059641505,1.022535965,1.020168226,1.09979993,1.064177762,1.07937811,1.21894032,1.068262528,1.09646681,1.114415242,1.129096378,1.246948335,1.194130991,1.136672442,1.226687022,1.191153763,1.292096014,1.330384093,1.308961546,1.445784924,1.52268287,1.444324776,1.506638992,1.362107806,1.59414592,1.700720131,1.678536489,1.640558304,1.819073629,1.80501237,1.788605717,1.914772599,2.027574432,2.040386526,2.148397666,2.147994643,2.216194937,2.327170041,2.271333577,2.484977744,2.559675565,2.629582297,2.671782367,2.971891218,3.07266782,2.995633344,3.251200786,3.309529238,3.45053253,3.438673247,3.518575276,3.572485015]
isamy=N.asarray(isamy)
faoy=N.asarray(faoy)

aisamy=isamy-N.average(isamy)
afaoy=faoy-N.average(faoy)


mean_isamy=runmean(x,isamy)

mean_faoy=runmean(x,faoy)


fig = plt.figure(figsize=(26,20))


ax = fig.add_subplot(321)
xx=range(a1,a2)


xdates = [datetime.datetime.strptime(str(int(date)),'%Y') for date in xx]

ax.plot_date(xdates,faoy,"ro-",label="FAO",linewidth=2)
ax.plot_date(xdates,isamy,"ko-",label="ISAM")
ax.xaxis.set_major_formatter(DateFormatter('%Y'))
ccp=scipy.stats.pearsonr(isamy,faoy)
leg=plt.legend(['FAO','ISAM {:04.2f}'.format(ccp[0])],fontsize=18)

leg.get_frame().set_alpha(0.5)

plt.xlabel("Year",fontsize=18)
plt.ylabel("Maize yield (t/ha)",fontsize=18)
plt.tick_params(axis='both',labelsize=18)




ax = fig.add_subplot(323)
ax.plot_date(xdates,afaoy,"ro-",label="FAO",linewidth=2)
ax.plot_date(xdates,aisamy,"ko-",label="ISAM")
ax.xaxis.set_major_formatter(DateFormatter('%Y'))

ccp=scipy.stats.pearsonr(aisamy,afaoy)
leg=plt.legend(['FAO','ISAM {:04.2f}'.format(ccp[0])],fontsize=18)
leg.get_frame().set_alpha(0.5)


plt.title("Anormaly by subtracting average",fontsize=18)
plt.xlabel("Year",fontsize=18)
plt.ylabel("Maize yield (t/ha)",fontsize=18)
plt.tick_params(axis='both',labelsize=18)

ax = fig.add_subplot(325)
ax.plot_date(xdates,mean_faoy,"ro-",label="FAO",linewidth=2)
ax.plot_date(xdates,mean_isamy,"ko-",label="ISAM")
ax.xaxis.set_major_formatter(DateFormatter('%Y'))

mean1_isamy=N.zeros([x-2])
mean1_faoy=N.zeros([x-2])

for i in range(1,x-2):
	mean1_isamy[i]=mean_isamy[i]
	mean1_faoy[i]=mean_faoy[i]

ccp=scipy.stats.pearsonr(mean1_isamy,mean1_faoy)

leg=plt.legend(['FAO', 'ISAM {:04.2f}'.format(ccp[0])],fontsize=18,loc=4)
leg.get_frame().set_alpha(0.5)


plt.xlabel("Year",fontsize=18)
plt.ylabel("Maize yield (t/ha)",fontsize=18)
plt.tick_params(axis='both',labelsize=18)

N.savetxt('sseamaize_faocompare.csv', (mean1_isamy,mean1_faoy), delimiter=',')




plt.savefig('maizefao_ssea_long.png',dpi=600,bbox_inches='tight')
plt.show()


