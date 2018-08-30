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


country=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/Ctry_halfdeg.nc','r')
#print iizumi
coun = country.variables['MASK_Country'][:,:]
#area=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/gridareahalf.nc','r')
#gridarea = area.variables['cell_area'][:,:]
#gridlon = area.variables['lon'][:]

#gridarea,gridlon = shiftgrid(180.5,gridarea,gridlon,start=False)



def annualyield(year,couna,counb):
    bb=year-1901
    aa=year-1901
    region1=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_soy_luh2new.nc','r')
    maitrop = region1.variables['area'][bb,:,:]
    maitrop=ma.masked_where(maitrop<=0,maitrop)
    maitrop=ma.filled(maitrop, fill_value=0.)

    maizeto = maitrop
    




    clm3n2=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/code/isamhiscru_soy_luh2new.nc','r')
    isamcrumai2 = clm3n2.variables['yield'][aa,:,:]
    isamcrumai2= ma.masked_where(isamcrumai2<=0,isamcrumai2)
    isamcrumai2=ma.filled(isamcrumai2, fill_value=0.)

 
    yieldclm1=0
    yieldclm=0.
    yieldisam=0.
    yieldisamc=0.
    yieldisamc2=0.
    yieldisamc3=0.

    a=0
    harea=0
    yieldc1=0
    yieldc=0.
    yieldi=0.
    yieldic=0.
    yieldic2=0.
    yieldic3=0.

    #USA 11501~11550
    for xx in range(0,360):
        for yy in range(0,720):
            if coun[xx,yy] >=couna and  coun[xx,yy] <=counb:
                harea=maizeto[xx,yy]+ harea
                yieldisamc2=(isamcrumai2[xx,yy]*maizeto[xx,yy])+yieldisamc2

                a=a+1
    yieldic2=yieldisamc2/harea

    return harea, yieldc,yieldi,yieldic,yieldclm,yieldisam,yieldisamc,yieldic2,yieldic3,yieldisamc2,yieldisamc3,yieldc1
    #return harea
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

#illzmui only 1983~2005
a1=1961
a2=2016
x=a2-a1
toarea= N.zeros(x)
zumiy= N.zeros(x)
clmy= N.zeros(x)
clmyn=N.zeros(x)
clmpn=N.zeros(x)
isamy= N.zeros(x)
zumip= N.zeros(x)
clmp= N.zeros(x)
isamp= N.zeros(x)
isamy1= N.zeros(x)
isamp1= N.zeros(x)
isamy2= N.zeros(x)
isamp2= N.zeros(x)
isamy3= N.zeros(x)
isamp3= N.zeros(x)
faoy=N.zeros(x)
faop=N.zeros(x)
#global
faoy1=[11287,11384,11561,11323,12279,13723,13494,14345,14523,14800,15189,14896,15851,14079,16574,15443,17561,16264,17492,16001,17538,17586,16201,17143,19063,18199,19052,17047,18288,18958,18725,20310,19361,21825,20312,21316,21565,22562,21901,21708,23061,22925,22796,22433,23175,23240,24370,23983,22481,25781,25197,22894,24999,26044,26757]

#us
#faoy1=[68380,71082,50893,66981,74074,74930,75225,53109,72978,74380,68172,82526,63211,86997,71230,79777,79522,84382,83979,85910,86733,81179,89246,100636,92852]
#faop1=[206222000,209180000,106030000,194880000,225453008,208943008,181142000,125194000,191319008,201532000,189866496,240719008,160984992,255292992,187968992,234527008,233867008,247882000,239548992,251852210,241375035,227765357,256227304,299873563,282260662]

c=0.0001
faoy=N.multiply(faoy1,c)
#name=["Global","USA","China","Brazil","Argentina","Mexico","India","Ukraine","Indonesia","France","Southafrica"]
#range1=[10100,11501,41501,20301,20101,11101,42901,47800,50300,42200,33900]
#range2=[50700,11550,41529,20327,20124,11132,42929,47800,50300,42200,33900]

#name=["Italy","Canada","Vietnam","Hungary","Romania","Philippines","Thailand","Chile","Spain","Nigeria","Germany"]
#range1=[43400,10201,48200,42700,46000,50700,47500,20400,46800,33400,42500]
#range2=[43400,10212,48200,42700,46000,50700,47500,20400,46800,33400,42500]

name=["Global"]
range1=[10100]
range2=[50700]
#name=["US"]
#range1=[11501]
#range2=[11550]

for i, name1 in enumerate(name):
        a=0
        clmy1=N.zeros(x)
	toarea= N.zeros(x)
	zumiy= N.zeros(x)
	clmy= N.zeros(x)
	isamy= N.zeros(x)
	zumip= N.zeros(x)
	clmp= N.zeros(x)
	isamp= N.zeros(x)
	isamy1= N.zeros(x)
	isamp1= N.zeros(x)
        isamy2= N.zeros(x)
        isamp2= N.zeros(x)
        isamy3= N.zeros(x)
        isamp3= N.zeros(x)

        clmyn=N.zeros(x)
        clmpn=N.zeros(x)
	for num in range(a1,a2):
    
	    reu=annualyield(num,range1[i],range2[i])
            clmy1[a]=reu[11]
	    toarea[a]=reu[0]
	    isamy1[a]=reu[3]
	    clmy[a]=reu[1]
	    isamp1[a]=reu[5]
	    clmp[a]=reu[4]
	    isamy[a]=reu[2]
	    isamp[a]=reu[6]
            isamy2[a]=reu[7]
            isamp2[a]=reu[9]
            isamy3[a]=reu[8]
            isamp3[a]=reu[10]

	    a=a+1

	azumiy=zumiy-N.average(zumiy)
	aisamy=isamy-N.average(isamy)
	aclmy=clmy-N.average(clmy)
	azumip=zumip-N.average(zumip)
	aisamp=isamp-N.average(isamp)
	aclmp=clmp-N.average(clmp)
	aisamy1=isamy1-N.average(isamy1)
	aisamp1=isamp1-N.average(isamp1)
        aisamy2=isamy2-N.average(isamy2)
        aisamp2=isamp2-N.average(isamp2)
        aisamy3=isamy3-N.average(isamy3)
        aisamp3=isamp3-N.average(isamp3)

        afaoy=faoy-N.average(faoy)
        aclmyn=clmyn-N.average(clmyn)
        aclmpn=clmpn-N.average(clmpn)


	mean_zumiy=runmean(x,zumiy)
	mean_isamy=runmean(x,isamy)
	mean_clmy=runmean(x,clmy)
	mean_zumip=runmean(x,zumip)
	mean_isamp=runmean(x,isamp)
	mean_clmp=runmean(x,clmp)
	mean_isamy1=runmean(x,isamy1)
	mean_isamp1=runmean(x,isamp1)
        mean_isamy2=runmean(x,isamy2)
        mean_isamp2=runmean(x,isamp2)
        mean_isamy3=runmean(x,isamy3)
        mean_isamp3=runmean(x,isamp3)

        mean_faoy=runmean(x,faoy)
        mean_clmyn=runmean(x,clmyn)
        mean_clmpn=runmean(x,clmpn)


	fig = plt.figure(figsize=(26,20))


	ax = fig.add_subplot(321)
	xx=range(a1,a2)

#plt.ylim((0,12))

	xdates = [datetime.datetime.strptime(str(int(date)),'%Y') for date in xx]
#plt.xticks(xdates, xdates)

	ax.plot_date(xdates,faoy,"ro-",label="FAO",linewidth=2)
        ax.plot_date(xdates,isamy2,"ko-",label="ISAM")


	ax.xaxis.set_major_formatter(DateFormatter('%Y'))
	ccp=scipy.stats.pearsonr(isamy,faoy)
	ccp1=scipy.stats.pearsonr(isamy1,faoy)
	ccp2=scipy.stats.pearsonr(clmy,faoy)
        ccp3=scipy.stats.pearsonr(isamy2,faoy)
        ccp4=scipy.stats.pearsonr(isamy3,faoy)
        ccp5=scipy.stats.pearsonr(clmy1,faoy)

        leg=plt.legend(['FAO','ISAM {:04.2f}'.format(ccp3[0])],fontsize=18)

#leg = plt.legend(loc=2,fancybox=True, fontsize=14)
	leg.get_frame().set_alpha(0.5)

	plt.xlabel("Year",fontsize=18)
	plt.ylabel("Soybean yield (t/ha)",fontsize=18)
	plt.title("Yield",fontsize=18)
	plt.tick_params(axis='both',labelsize=18)




	ax = fig.add_subplot(323)
        ax.plot_date(xdates,afaoy,"ro-",label="FAO",linewidth=2)
        ax.plot_date(xdates,aisamy2,"ko-",label="ISAM")

	ax.xaxis.set_major_formatter(DateFormatter('%Y'))

	ccp=scipy.stats.pearsonr(aisamy,afaoy)
	ccp1=scipy.stats.pearsonr(aisamy1,afaoy)
	ccp2=scipy.stats.pearsonr(aclmy,afaoy)
        ccp3=scipy.stats.pearsonr(aisamy2,afaoy)
        leg=plt.legend(['FAO','ISAM {:04.2f}'.format(ccp3[0])],fontsize=18)

#	leg=plt.legend(['FAO', 'ISAM-NCEP {:05.3f}'.format(ccp[0]),'ISAM-CESM {:05.3f}'.format(ccp1[0]),'CLM-N {:05.3f}'.format(ccp2[0]),'CLM {:05.3f}'.format(ccp3[0])])
#        leg=plt.legend(['FAO', 'ISAM-NCEP {:04.2f}'.format(ccp[0]),'ISAM-CESM {:04.2f}'.format(ccp1[0]),'CLM {:04.2f}'.format(ccp2[0])],loc=4,fontsize=18)

#leg = plt.legend(loc=2,fancybox=True, fontsize=14)
	leg.get_frame().set_alpha(0.5)


	plt.title("Anormaly by subtracting average",fontsize=18)
	plt.xlabel("Year",fontsize=18)
	plt.ylabel("Soybean yield (t/ha)",fontsize=18)
	plt.tick_params(axis='both',labelsize=18)






	ax = fig.add_subplot(325)
        ax.plot_date(xdates,mean_faoy,"ro-",label="FAO",linewidth=2)
        ax.plot_date(xdates,mean_isamy2,"ko-",label="ISAM")
        ax.xaxis.set_major_formatter(DateFormatter('%Y'))

	mean1_isamy=N.zeros([x-2])
	mean1_faoy=N.zeros([x-2])
	mean1_isamy1=N.zeros([x-2])
        mean1_isamy2=N.zeros([x-2])
        mean1_isamy3=N.zeros([x-2])
	mean1_clmy=N.zeros([x-2])

	for i in range(1,x-2):
		mean1_isamy[i]=mean_isamy[i]
		mean1_faoy[i]=mean_faoy[i]
		mean1_isamy1[i]=mean_isamy1[i]
		mean1_clmy[i]=mean_clmy[i]
                mean1_isamy2[i]=mean_isamy2[i]
                mean1_isamy3[i]=mean_isamy3[i]

	ccp=scipy.stats.pearsonr(mean1_isamy,mean1_faoy)
	ccp1=scipy.stats.pearsonr(mean1_isamy1,mean1_faoy)
	ccp2=scipy.stats.pearsonr(mean1_clmy,mean1_faoy)
        ccp3=scipy.stats.pearsonr(mean1_isamy2,mean1_faoy)
        ccp4=scipy.stats.pearsonr(mean1_isamy3,mean1_faoy)

#        ccp3=scipy.stats.pearsonr(mean1_clmyn,mean1_faoy)
#	leg=plt.legend(['FAO', 'ISAM-NCEP {:05.3f}'.format(ccp[0]),'ISAM-CESM {:05.3f}'.format(ccp1[0]),'CLM-N {:05.3f}'.format(ccp2[0]),'CLM {:05.3f}'.format(ccp3[0])])
#        leg=plt.legend(['FAO', 'ISAM-NCEP {:04.2f}'.format(ccp[0]),'ISAM-CESM {:04.2f}'.format(ccp1[0]),'CLM {:04.2f}'.format(ccp2[0])],loc=4,fontsize=18)
#leg = plt.legend(loc=2,fancybox=True, fontsize=14)
        leg=plt.legend(['FAO', 'ISAM {:04.2f}'.format(ccp3[0])],fontsize=18,loc=4)

	leg.get_frame().set_alpha(0.5)


#	plt.title("Anormaly by subtracting a moving mean average",fontsize=18)
	plt.xlabel("Year",fontsize=18)
	plt.ylabel("Soybean yield (t/ha)",fontsize=18)
	plt.tick_params(axis='both',labelsize=18)



	plt.savefig('soy_faoclm_{0}_paper1_long.png'.format(name1),dpi=600,bbox_inches='tight')
plt.show()


