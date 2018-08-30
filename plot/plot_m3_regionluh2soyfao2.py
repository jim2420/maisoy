from mpl_toolkits.basemap import Basemap, cm, shiftgrid,interp,maskoceans
from netCDF4 import Dataset as NetCDFFile
import numpy as N
import matplotlib.pyplot as plt
import numpy.ma as ma
import matplotlib.colors as colors

mask=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/Ctry_halfdeg.nc','r')
cou1 = mask.variables['MASK_Country'][:,:]
cou1= ma.masked_where(cou1<=0.0,cou1)

region=NetCDFFile('/project/projectdirs/m1602/datasets4.full/surfdata_05x05.nc','r')
ind = region.variables['REGION_MASK_CRU_NCEP'][:,:]


#area=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/gridareahalf.nc','r')
#gridarea = area.variables['cell_area']

isam=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/rice_cheyenne/his_cru/ric_irr_fert/output/ric_irr_fert.nc','r')
lonisam1=isam.variables['lon'][:]
#ric_i_f=isam.variables['totalyield'][96:103,:,:]
#riceb=N.average(ric_i_f,axis=0)


spam=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/spamsoy_isam.nc','r')
spamy=spam.variables['soyy_total'][:,:]
spampro=spam.variables['soyp_total'][:,:]
spamarea=spam.variables['soya_total'][:,:]


#riceb,lona11=shiftgrid(180.5,riceb,lonisam1,start=False)
ind,lona11=shiftgrid(180.5,ind,lonisam1,start=False)

nclu=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/soybean_AreaYieldProduction.nc','r')
ncvar_m = nclu.variables['soybeanData'][0,0,:,:]
ncvar_y = nclu.variables['soybeanData'][0,1,:,:]
ncvar_a = nclu.variables['soybeanData'][0,4,:,:]
ncvar_p = nclu.variables['soybeanData'][0,5,:,:]

latnc = nclu.variables['latitude'][:]
znc = nclu.variables['level'][:]
lonnc = nclu.variables['longitude'][:]
timenc = nclu.variables['time'][:]
lat_new=N.flipud(latnc)


isam=NetCDFFile('../code/m3_soy.nc','r')
#grow = isam.variables['yieldisam'][96:103,:,:]
lonisam = isam.variables['lon'][:]
latisam = isam.variables['lat'][:]
ryield1 = isam.variables['yieldm3'][:,:]
mearea=isam.variables['m3area'][:,:]
gridarea1=isam.variables['gridarea'][:,:]
#ryield=N.average(grow,axis=0)

isam1=NetCDFFile('../code/isamhiscru_soy_luh2vmax.nc','r')
ryield = isam1.variables['yield'][96:105,:,:]#1997-2005
#ryield=N.average(grow,axis=0)
meareaisam = isam1.variables['area'][96:105,:,:]#1997-2005

meareaisam= ma.masked_where(meareaisam<=0.0,meareaisam)


mearea= ma.masked_where(mearea<=0.0,mearea)

ryield= ma.masked_where(ryield<=0.0,ryield)
ryield1= ma.masked_where(ryield1<=0.0,ryield1)
#ryield= ma.masked_where(ryield1<=0.0,ryield)
#ryield1= ma.masked_where(ryield<=0.0,ryield1)
'''
meareaisam= ma.masked_where(ryield<=0.0,meareaisam)
ryield= ma.masked_where(meareaisam<=0.0,ryield)
meareaisam= ma.masked_where(ryield<=0.0,meareaisam)
'''

region=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/clm/HistoricalGLM_crop_150901.nc','r')

latmask = region.variables['lat'][:]
lonmask = region.variables['lon'][:]

lat_new=N.flipud(latnc)
ncvar_m=N.flipud(ncvar_m)
ncvar_y=N.flipud(ncvar_y)
ncvar_a=N.flipud(ncvar_a)
ncvar_p=N.flipud(ncvar_p)

ind1=N.zeros((9,360,720))
cou=N.zeros((9,360,720))
gridarea=N.zeros((9,360,720))
for i in range(0,9):
        ind1[i,:,:]=ind[:,:]
        cou[i,:,:]=cou1[:,:]
        gridarea[i,:,:]=gridarea1[:,:]


aa1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/iizumi/iizumi.2013JAN29.soybean.1982-2006.30min.nc4','r')
iizumiy=N.zeros((9,360,720))
iizumia=N.zeros((9,360,720))
for i in range(1997,2006):
        xx=i-1982
        j=i-1997
        ya = N.flipud(aa1.variables['yield50'][xx,:,:])#t/ha
        yaa = N.flipud(aa1.variables['area'][xx,:,:])##%
        iizumiy[j,:,:]=ya
        iizumia[j,:,:]=yaa
iizumiy= ma.masked_where(iizumiy<=0.0,iizumiy)
iizumia= ma.masked_where(iizumia<=0.0,iizumia)
iizumiy= ma.masked_where(iizumiy>=(10**18),iizumiy)
iizumia= ma.masked_where(iizumia>=(10**18),iizumia)
iizua=iizumia/100*gridarea1/10000
iizup=iizua*iizumiy


ryield= ma.masked_where(ind1==0.0,ryield)
ryield1= ma.masked_where(ind==0.0,ryield1)
gridarea= ma.masked_where(ind1==0.0,gridarea)
mearea= ma.masked_where(ind==0.0,mearea)
gridarea1= ma.masked_where(ind==0.0,gridarea1)
spamy= ma.masked_where(ind==0.0,spamy)
spampro= ma.masked_where(ind==0.0,spampro)
spamarea= ma.masked_where(ind==0.0,spamarea)
meareaisam= ma.masked_where(ind1==0.0,meareaisam)
iizua= ma.masked_where(ind1==0.0,iizua)
iizup= ma.masked_where(ind1==0.0,iizup)

lon,lat = N.meshgrid(lonmask,latmask)
lon1,lat1 = N.meshgrid(lonnc,lat_new)
isamp=ryield*meareaisam
m3p=ryield1*gridarea1/10000
name=["Global","NA","SA","EU","Africa","PD","USSR","China","SSEA"]

num=9
spampp=N.zeros((num))
spamaa=N.zeros((num))

allarea1=N.zeros((num))
allproisam=N.zeros((num))
allprom3=N.zeros((num))
allyisam=N.zeros((num))
allym3=N.zeros((num))
allgrid=N.zeros((num))
m3grid=N.zeros((num))
isamgrid=N.zeros((num))
for idx in range(0,9):
	m3pmask=N.zeros((360,720))
        mareamask=N.zeros((360,720))
        areak=N.zeros((360,720))
        spamp1=N.zeros((360,720))
        spama1=N.zeros((360,720))
	m3pmask=m3p
	mareamask=mearea
	areak=gridarea1
        spama1=spamarea
        spamp1=spampro
        if idx==5:
                idx=9
        if idx==4 :
                m3pmask=ma.masked_where(ind>5.0,m3pmask)
                mareamask=ma.masked_where(ind>5.0,mareamask)
                areak=ma.masked_where(ind>5.0,areak)
                spama1=ma.masked_where(ind>5.0,spama1)
                spamp1=ma.masked_where(ind>5.0,spamp1)

                m3pmask=ma.masked_where(ind<4.0,m3pmask)
                mareamask=ma.masked_where(ind<4.0,mareamask)
                areak=ma.masked_where(ind<4.0,areak)
                spama1=ma.masked_where(ind<4.0,spama1)
                spamp1=ma.masked_where(ind<4.0,spamp1)
	elif idx==0:
                m3pmask=ma.masked_where(ind==idx,m3pmask)
                mareamask=ma.masked_where(ind==idx,mareamask)
                areak=ma.masked_where(ind==idx,areak)
                spama1=ma.masked_where(ind==idx,spama1)
                spamp1=ma.masked_where(ind==idx,spamp1)

	else:
                m3pmask=ma.masked_where(ind!=idx,m3pmask)
                mareamask=ma.masked_where(ind!=idx,mareamask)
                areak=ma.masked_where(ind!=idx,areak)
                spama1=ma.masked_where(ind!=idx,spama1)
                spamp1=ma.masked_where(ind!=idx,spamp1)
        if idx==9:
                idx=5

        allarea1[idx]=N.sum(mareamask)
        allprom3[idx]=N.sum(m3pmask)
        allgrid[idx]=N.sum(areak)
        spampp[idx]=N.sum(spamp1)
        spamaa[idx]=N.sum(spama1)
	
allym3=allprom3/allarea1
megrid=allprom3/allgrid*10000
#faoyy=faop/allgrid*10000
spamyy=spampp/spamaa
spamgrid=spampp/allgrid*10000



iizuy1=N.zeros((num))
iizuyg1=N.zeros((num))
iizuy1_std=N.zeros((num))
iizuyg1_std=N.zeros((num))

iizua1=N.zeros((num))
iizup1=N.zeros((num))
iizup1_std=N.zeros((num))

iially=N.zeros((num,9))
iiallp=N.zeros((num,9))
iiallg=N.zeros((num,9))
gg=N.zeros((num,9))
luharea=N.zeros((num))
allyisam_std=N.zeros((num))
allproisam_std=N.zeros((num))
isamgrid_std=N.zeros((num))
for idx in range(0,9):
        #print a1[idx],a2[idx]
        isampmask=N.zeros((9,360,720))
        isamarea=N.zeros((9,360,720))
        areak=N.zeros((9,360,720))
        aiizu=N.zeros((9,360,720))
        piizu=N.zeros((9,360,720))
        aiizu=iizua
        piizu=iizup
        areak=gridarea
        isampmask=isamp
        isamarea=meareaisam
        if idx==5:
                idx=9
        if idx==4 :
                isampmask=ma.masked_where(ind1>5.0,isampmask)
                isamarea=ma.masked_where(ind1>5.0,isamarea)
                areak=ma.masked_where(ind1>5.0,areak)
                aiizu=ma.masked_where(ind1>5.0,aiizu)
                piizu=ma.masked_where(ind1>5.0,piizu)

                areak=ma.masked_where(ind1<4.0,areak)
                isampmask=ma.masked_where(ind1<4.0,isampmask)
                isamarea=ma.masked_where(ind1<4.0,isamarea)
                aiizu=ma.masked_where(ind1<4.0,aiizu)
                piizu=ma.masked_where(ind1<4.0,piizu)

        elif idx==0:
   	        isampmask=ma.masked_where(ind1==idx,isampmask)
                isamarea=ma.masked_where(ind1==idx,isamarea)
                areak=ma.masked_where(ind1==idx,areak)
                aiizu=ma.masked_where(ind1==idx,aiizu)
                piizu=ma.masked_where(ind1==idx,piizu)

	else:
                isampmask=ma.masked_where(ind1!=idx,isampmask)
                isamarea=ma.masked_where(ind1!=idx,isamarea)
                areak=ma.masked_where(ind1!=idx,areak)
                aiizu=ma.masked_where(ind1!=idx,aiizu)
                piizu=ma.masked_where(ind1!=idx,piizu)
        if idx==9:
                idx=5

        iizua1[idx]=N.average(N.sum(aiizu,axis=(1,2)))
        luharea[idx]=N.average(N.sum(isamarea,axis=(1,2)))
        iizup1[idx]=N.average((N.sum(piizu,axis=(1,2))))
        iizup1_std[idx]=N.std((N.sum(piizu,axis=(1,2))))

        iizuy1[idx]=N.average(N.sum(piizu,axis=(1,2))/(N.sum(aiizu,axis=(1,2))))
        iizuy1_std[idx]=N.std(N.sum(piizu,axis=(1,2))/(N.sum(aiizu,axis=(1,2))))
        iizuyg1[idx]=N.average((N.sum(piizu,axis=(1,2))/(N.sum(areak,axis=(1,2)))*10000))
        iizuyg1_std[idx]=N.std((N.sum(piizu,axis=(1,2))/(N.sum(areak,axis=(1,2)))*10000))

        allproisam[idx]=N.average((N.sum(isampmask,axis=(1,2))))
#        allyisam[idx]=N.average(N.sum(isampmask,axis=(1,2))/(N.sum(isamarea,axis=(1,2))))
	gg[idx,:]=(N.sum(isampmask,axis=(1,2)))/(N.sum(isamarea,axis=(1,2)))
	allyisam[idx]=N.average([N.average(gg[idx,0:7]),N.average(gg[idx,:]),N.average(gg[idx,:]),N.average(gg[idx,7:9])])
        allproisam_std[idx]=N.std((N.sum(isampmask,axis=(1,2))))
        allyisam_std[idx]=N.std(N.sum(isampmask,axis=(1,2))/(N.sum(isamarea,axis=(1,2))))
        isamgrid[idx]=N.average((N.sum(isampmask,axis=(1,2))/(N.sum(areak,axis=(1,2)))*10000))
        isamgrid_std[idx]=N.std((N.sum(isampmask,axis=(1,2))/(N.sum(areak,axis=(1,2)))*10000))

        iiallp[idx,:]=(N.sum(piizu,axis=(1,2)))
        iially[idx,:]=((N.sum(piizu,axis=(1,2)))/(N.sum(aiizu,axis=(1,2))))
        iiallg[idx,:]=((N.sum(piizu,axis=(1,2)))/(N.sum(areak,axis=(1,2)))*10000)

#fao 1997-2003
afy1=[2.1565,2.2562,2.1901,2.1708,2.3061,2.2925,2.2796,2.2433,2.3175];afp1=[144326230,160128838,157815456,161308456,177020696,180950793,190573602,205548177,214542816]
afy2=[2.6152,2.6227,2.4736,2.5609,2.6243,2.5474,2.2732,2.8312,2.8888];afp2=[75913480,77334780,75004360,77758290,80306670,77345730,69056020,88059530,86662180]
afy3=[2.118333625,2.457455441,2.384073253,2.367219338,2.631042068,2.56479184,2.789658309,2.232616625,2.379824931]
afp3=[41460568,54339498,55340596,57426007,69824765,77053636,93110364,87045929,96024094]
afy4=[3.2128,2.7210,2.8495,2.5344,2.9910,2.9768,2.0547,2.8005,2.8089];afp4=[1655665,1911169,1581825,1319880,1468897,1190786,967199,1181481,1308381]
afy5=[0.8943,1.0156,1.0541,1.0521,1.0757,1.0406,0.9792,1.0262,1.0896];afp5=[751906,937225,928500,945337,1026157,1029535,1009651,1173356,1317271]

afy7=[0.8794,0.7817,0.8267,1.0133,0.9401,1.1659,0.9824,0.9981,1.0461];afp7=[279536,295031,334396,341754,349635,422530,392477,554236,686099]
afy8=[1.7652,1.7826,1.7892,1.6557,1.6248,1.8929,1.6529,1.8148,1.7045];afp8=[14736222,15153263,14245652,15409295,15405928,16505768,15393541,17401780,16348013]
afy9=[1.116131768,1.123041218,1.152187867,0.89624828,0.987956271,0.84485402,1.214255129,0.972689622,1.126156729];
afp9=[8552680,9174099,9183306,6995320,7477924,6104110,9326809,8578783,10241954]


afaoyy1=afp1/allgrid[0]*10000
afaoyy2=afp2/allgrid[1]*10000
afaoyy3=afp3/allgrid[2]*10000
afaoyy4=afp4/allgrid[3]*10000
afaoyy5=afp5/allgrid[4]*10000
afaoyy7=afp7/allgrid[6]*10000
afaoyy8=afp8/allgrid[7]*10000
afaoyy9=afp9/allgrid[8]*10000

'''
for i in range(1,10):
        kc=([allym3[i-1],spamyy[i-1]])
        locals()['fy{0}'.format(i)]=N.concatenate([kc,iially[i-1,:]])
        print kc,locals()['fy{0}'.format(i)],allym3[i-1],iially[i-1,:]
        if i!=6:
                locals()['fy{0}'.format(i)]=N.concatenate([locals()['fy{0}'.format(i)],locals()['afy{0}'.format(i)]])
        locals()['fy{0}'.format(i)]=N.asarray(locals()['fy{0}'.format(i)])
        print kc,locals()['fy{0}'.format(i)],allym3[i-1],iially[i-1,:]

        kc=([megrid[i-1],spamgrid[i-1]])
        locals()['faoyy{0}'.format(i)]=N.concatenate([kc,iiallg[i-1,:]])
        if i!=6:
                locals()['faoyy{0}'.format(i)]=N.concatenate([locals()['faoyy{0}'.format(i)],locals()['afaoyy{0}'.format(i)]])
        locals()['faoyy{0}'.format(i)]=N.asarray(locals()['faoyy{0}'.format(i)])

        kc=([allprom3[i-1],spampp[i-1]])
        locals()['fp{0}'.format(i)]=N.concatenate([kc,iiallp[i-1,:]])
        if i!=6:
                locals()['fp{0}'.format(i)]=N.concatenate([locals()['fp{0}'.format(i)],locals()['afp{0}'.format(i)]])
        locals()['fp{0}'.format(i)]=N.asarray(locals()['fp{0}'.format(i)])
'''


for i in range(1,10):
        aa=N.ma.average(iially[i-1,:])
        kc=(N.ma.average(allym3[i-1]),N.ma.average(spamyy[i-1]),aa)
	
	#print kc
        locals()['fy{0}'.format(i)]=kc
        if i!=6:
		cc=N.ma.average(locals()['afy{0}'.format(i)])
                locals()['fy{0}'.format(i)]=(cc,N.ma.average(allym3[i-1]),N.ma.average(spamyy[i-1]),aa)
	
        locals()['fy{0}'.format(i)]=N.asarray(locals()['fy{0}'.format(i)])
        print kc,locals()['fy{0}'.format(i)],allym3[i-1],iially[i-1,:]

        kc=([megrid[i-1],spamgrid[i-1]])
        locals()['faoyy{0}'.format(i)]=N.concatenate([kc,iiallg[i-1,:]])
        if i!=6:
                locals()['faoyy{0}'.format(i)]=N.concatenate([locals()['faoyy{0}'.format(i)],locals()['afaoyy{0}'.format(i)]])
        locals()['faoyy{0}'.format(i)]=N.asarray(locals()['faoyy{0}'.format(i)])

        kc=([allprom3[i-1],spampp[i-1]])
        locals()['fp{0}'.format(i)]=N.concatenate([kc,iiallp[i-1,:]])
        if i!=6:
                locals()['fp{0}'.format(i)]=N.concatenate([locals()['fp{0}'.format(i)],locals()['afp{0}'.format(i)]])
        locals()['fp{0}'.format(i)]=N.asarray(locals()['fp{0}'.format(i)])


faop=[N.average(fp1),N.average(fp2),N.average(fp3),N.average(fp4),N.average(fp5),N.average(fp6),N.average(fp7),N.average(fp8),N.average(fp9)]
faop_std=[N.std(fp1),N.std(fp2),N.std(fp3),N.std(fp4),N.std(fp5),N.std(fp6),N.std(fp7),N.std(fp8),N.std(fp9)]

faoy=[N.average(fy1),N.average(fy2),N.average(fy3),N.average(fy4),N.average(fy5),N.average(fy6),N.average(fy7),N.average(fy8),N.average(fy9)]
faoy_std=[N.std(fy1),N.std(fy2),N.std(fy3),N.std(fy4),N.std(fy5),N.std(fy6),N.std(fy7),N.std(fy8),N.std(fy9)]

faoyy=[N.average(faoyy1),N.average(faoyy2),N.average(faoyy3),N.average(faoyy4),N.average(faoyy5),N.average(faoyy6),N.average(faoyy7),N.average(faoyy8),N.average(faoyy9)]
faoyy_std=[N.std(faoyy1),N.std(faoyy2),N.std(faoyy3),N.std(faoyy4),N.std(faoyy5),N.std(faoyy6),N.std(faoyy7),N.std(faoyy8),N.std(faoyy9)]

allyisam1=N.zeros(7)
allyisam1_std=N.zeros(7)
faoy1=N.zeros(7)
faoy1_std=N.zeros(7)

allproisam1=N.zeros(7)
allproisam1_std=N.zeros(7)
faop1=N.zeros(7)
faop1_std=N.zeros(7)
isamgrid1=N.zeros(7)
faoyy1=N.zeros(7)
isamgrid1_std=N.zeros(7)
faoyy1_std=N.zeros(7)

for i in range(0,7):
	if i==5 or i==6:
	        allyisam1[i]=allyisam[i+2]
                allyisam1_std[i]=allyisam_std[i+2]
                faoy1[i]=faoy[i+2]
                faoy1_std[i]=faoy_std[i+2]
                allproisam1[i]=allproisam[i+2]
                allproisam1_std[i]=allproisam_std[i+2]
                faop1[i]=faop[i+2]
                faop1_std[i]=faop_std[i+2]
                isamgrid1[i]=isamgrid[i+2]
                isamgrid1_std[i]=isamgrid_std[i+2]
                faoyy1[i]=faoyy[i+2]
                faoyy1_std[i]=faoyy_std[i+2]


	else:
		allyisam1[i]=allyisam[i] 
                allyisam1_std[i]=allyisam_std[i]
                faoy1[i]=faoy[i]
                faoy1_std[i]=faoy_std[i]

                allproisam1[i]=allproisam[i]
                allproisam1_std[i]=allproisam_std[i]
                faop1[i]=faop[i]
                faop1_std[i]=faop_std[i]
                isamgrid1[i]=isamgrid[i]
                isamgrid1_std[i]=isamgrid_std[i]
                faoyy1[i]=faoyy[i]
                faoyy1_std[i]=faoyy_std[i]



fig = plt.figure(figsize=(20,10))
n_groups = 7

#ax = fig.add_subplot(111)
index = N.arange(n_groups)
bar_width = 0.4
opacity = 0.8
rects1 = plt.bar(index+0.1, allyisam1, bar_width,
                 alpha=opacity,
                 color='blue',
                 label='ISAM')
#rects1 = plt.bar(index+0.1, allyisam1, bar_width,yerr=allyisam1_std,ecolor='black', capsize=5,
#                 alpha=opacity,
#                 color='blue',
#                 label='ISAM')
rects0 = plt.bar(index + 0.1+bar_width*1, faoy1, bar_width,yerr=faoy1_std,ecolor='black',error_kw=dict(lw=5, capsize=15, capthick=3),
                 alpha=opacity,
                 color='r',
                 label='Measured Data')

#plt.xlabel('Region',fontsize=50)
plt.ylabel('Yield (t / ha cropland)',fontsize=50)
#plt.ylabel('Yield (t / ha country)',fontsize=35)
plt.xticks(index + bar_width+0.11, ("Global","NA","SA","EU","Africa","China","SSEA"))
#leg=plt.legend(loc=1,ncol=2, fontsize=30)
#leg.get_frame().set_alpha(0.5)
plt.tick_params(axis='both',labelsize=50)


plt.tight_layout()
plt.savefig('nsoy_regionyfvmax1.png')
plt.show()



fig = plt.figure(figsize=(20,10))
n_groups = 7

#ax = fig.add_subplot(111)
index = N.arange(n_groups)
bar_width = 0.4
opacity = 1.0
rects1 = plt.bar(index+0.1, allproisam1, bar_width,yerr=allproisam1_std,ecolor='black', capsize=5,
                 alpha=opacity,
                 color='blue',
                 label='ISAM')
rects0 = plt.bar(index + 0.1+bar_width*1, faop1, bar_width,yerr=faop1_std,ecolor='black', capsize=5,
                 alpha=opacity,
                 color='r',
                 label='Other studies')
#rects3 = plt.bar(index + 0.18+bar_width*3, iizup1, bar_width,yerr=iizup1_std,ecolor='black', capsize=5,
#                 alpha=opacity,
#                 color='y',
#                 label='iizumi')

plt.xlabel('Region',fontsize=35)
plt.ylabel('Production (tons)',fontsize=35)
#plt.ylabel('Yield (t / ha country)',fontsize=35)
plt.xticks(index + bar_width+0.11, ("Global","NA","SA","EU","Africa","China","SSEA"),rotation='vertical')
#lt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
#leg=plt.legend(loc=2,ncol=3, fontsize=35)
#leg.get_frame().set_alpha(0.5)
plt.tick_params(axis='both',labelsize=35)


plt.tight_layout()
plt.savefig('nsoy_regionpfvmax1.png')
plt.show()


fig = plt.figure(figsize=(20,10))
n_groups = 7

#ax = fig.add_subplot(111)
index = N.arange(n_groups)
bar_width = 0.4
opacity = 1.0
rects1 = plt.bar(index+0.1, isamgrid1, bar_width,yerr=isamgrid1_std,ecolor='black', capsize=5,
                 alpha=opacity,
                 color='blue',
                 label='ISAM')
#rects2 = plt.bar(index +0.18+ bar_width*1,megrid , bar_width,
#                 alpha=opacity,
#                 color='g',
#                 label='M3')
rects0 = plt.bar(index + 0.1+bar_width*1, faoyy1, bar_width,yerr=faoyy1_std,ecolor='black', capsize=5,
                 alpha=opacity,
                 color='r',
                 label='Other studies')
#rects0 = plt.bar(index + 0.18+bar_width*3, iizuyg1, bar_width,yerr=iizuyg1_std,ecolor='black', capsize=5,
#                 alpha=opacity,
#                 color='y',
#                 label='Iizumi')
plt.xlabel('Region',fontsize=35)
plt.ylabel('(t grains / ha country)',fontsize=35)
#plt.ylabel('Yield (t / ha country)',fontsize=35)
plt.xticks(index + bar_width+0.11, ("Global","NA","SA","EU","Africa","China","SSEA"),rotation='vertical')
#lt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
#leg=plt.legend(loc=2,ncol=2, fontsize=35)
#leg.get_frame().set_alpha(0.5)
plt.tick_params(axis='both',labelsize=35)


plt.tight_layout()
plt.savefig('nsoy_regiony1vmax1.png')
plt.show()

