from mpl_toolkits.basemap import Basemap, cm, shiftgrid,interp,maskoceans
from netCDF4 import Dataset as NetCDFFile
import numpy as N
import matplotlib.pyplot as plt
import numpy.ma as ma
import matplotlib.colors as colors

mask=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/Ctry_halfdeg.nc','r')
cou1 = mask.variables['MASK_Country'][:,:]
cou1= ma.masked_where(cou1<=0.0,cou1)

region=NetCDFFile('/global/project/projectdirs/m1602/datasets4.full/arbit_init_state_05x05.nc','r')
ind = region.variables['REGION_MASK'][:,:]




#area=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/gridareahalf.nc','r')
#gridarea = area.variables['cell_area']

isam=NetCDFFile('/scratch2/scratchdirs/tslin2/isam/rice_cheyenne/his_cru/ric_irr_fert/output/ric_irr_fert.nc','r')
lonisam1=isam.variables['lon'][:]
ric_i_f=isam.variables['totalyield'][96:103,:,:]
riceb=N.average(ric_i_f,axis=0)


spam=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/spammaize_isam.nc','r')
spamy=spam.variables['maiy_total'][:,:]
spampro=spam.variables['maip_total'][:,:]
spamarea=spam.variables['maia_total'][:,:]

riceb,lona11=shiftgrid(180.5,riceb,lonisam1,start=False)
ind,lona11=shiftgrid(180.5,ind,lonisam1,start=False)

nclu=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/maize_AreaYieldProduction.nc','r')
ncvar_m = nclu.variables['maizeData'][0,0,:,:]
ncvar_y = nclu.variables['maizeData'][0,1,:,:]
ncvar_a = nclu.variables['maizeData'][0,4,:,:]
ncvar_p = nclu.variables['maizeData'][0,5,:,:]

latnc = nclu.variables['latitude'][:]
znc = nclu.variables['level'][:]
lonnc = nclu.variables['longitude'][:]
timenc = nclu.variables['time'][:]
lat_new=N.flipud(latnc)


isam=NetCDFFile('../code/m3_mai.nc','r')
#grow = isam.variables['yieldisam'][96:103,:,:]
lonisam = isam.variables['lon'][:]
latisam = isam.variables['lat'][:]
ryield1 = isam.variables['yieldm3'][:,:]
mearea=isam.variables['m3area'][:,:]
gridarea1=isam.variables['gridarea'][:,:]
#ryield=N.average(grow,axis=0)



isam1=NetCDFFile('../code/isamhiscru_mai_luh2.nc','r')
ryield = isam1.variables['yield'][96:105,:,:]#1997-2005
#ryield=N.average(grow,axis=0)
meareaisam = isam1.variables['area'][96:105,:,:]#1997-2005


meareaisam= ma.masked_where(meareaisam<=0.0,meareaisam)

mearea= ma.masked_where(mearea<=0.0,mearea)

ryield= ma.masked_where(ryield<=0.0,ryield)
ryield1= ma.masked_where(ryield1<=0.0,ryield1)



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



aa1=NetCDFFile('/scratch2/scratchdirs/tslin2/plot/globalcrop/data/iizumi/iizumi.2013JAN29.maize_major.1982-2006.30min.nc4','r')
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

ryield= ma.masked_where(ind1!=8.0,ryield)
ryield1= ma.masked_where(ind!=8.0,ryield1)
gridarea= ma.masked_where(ind1!=8.0,gridarea)
mearea= ma.masked_where(ind!=8.0,mearea)
spamy= ma.masked_where(ind!=8.0,spamy)
spampro= ma.masked_where(ind!=8.0,spampro)
spamarea= ma.masked_where(ind!=8.0,spamarea)
meareaisam= ma.masked_where(ind1!=8.0,meareaisam)
iizua= ma.masked_where(ind1!=8.0,iizua)
iizup= ma.masked_where(ind1!=8.0,iizup)

lon,lat = N.meshgrid(lonmask,latmask)
lon1,lat1 = N.meshgrid(lonnc,lat_new)
isamp=ryield*meareaisam
m3p=ryield1*gridarea1/10000

name=["Nepal","Pakistan","India","Sri Lanka","Bangladesh","Bhutan","Cambodia","Indonesia","Myanmar","Phillipines","Thailand","Vietnam","Laos","Malaysia1"]
a1=[45100,45600,42901,46900,40800,41000,41400,50300,45000,50700,47500,48200,44000,50400]
a2=[45100,45600,42929,46900,40800,41000,41400,50300,45000,50700,47500,48200,44000,44600]
fa1=[794000,799060,802290,819010,824525,825980,836190,834285,849892];fy1=[1.6585,1.7112,1.6776,1.7275,1.8000,1.8291,1.8765,1.9059,2.0191]
fa2=[927700,932600,962200,961700,944000,941600,947100,981800,1042000];fy2=[1.6352,1.7853,1.7169,1.7086,1.7631,1.8448,2.0034,2.8488,2.9843]
fa3=[6321000,6203700,6422100,6611300,6581500,6635200,7343400,7430400,7588300];fy3=[1.7111,1.7969,1.7922,1.8216,1.9996,1.6807,2.0405,1.9073,1.9385]
fa4=[25796,29790,28880,28648,25710,23410,27060,23430,28410];fy4=[0.9959,1.1371,1.0897,1.0838,1.1182,1.1282,1.0957,1.5023,1.4713]
fa5=[2428,4047,3240,4855,19970,29060,29071,50051,66830];fy5=[1.0914,0.7339,1.2346,2.0597,3.2216,4.0349,4.0334,4.8243,5.3311]
fa6=[50000,50000,45000,31000,38000,26118,26849,21788,30700];fy6=[1.7000,1.7000,1.5556,1.5645,1.5789,1.5856,1.8504,4.0495,3.0608]
fa7=[34138,39857,59739,57404,67213,71594,83953,77304,70480];fy7=[1.2427,1.2171,1.5948,2.7345,2.7612,2.0797,3.7472,3.3202,3.5153]
fa8=[3355224,3833820,3456357,3500000,3285900,3126830,3358511,3356914,3625987];fy8=[2.6141,2.6526,2.6629,2.7649,2.8446,3.0655,3.2414,3.3439,3.4539]
fa9=[160660,183323,203557,210437,250501,268307,284494,292588,319297];fy9=[1.8885,1.6250,1.6880,1.7055,2.0918,2.2116,2.4356,2.6354,2.8297]
fa10=[2725875,2354208,2642208,2510342,2486588,2395456,2409828,2527135,2441788];fy10=[1.5894,1.6240,1.7351,1.7970,1.8198,1.8031,1.9153,2.1421,2.1514]
fa11=[1198055,1380480,1206560,1218287,1204697,1146669,1103271,1125119,1072716];fy11=[3.1982,3.3448,3.5526,3.6715,3.7329,3.7145,3.8513,3.8587,3.8161]
fa12=[662900,652377,691800,730200,729500,816400,912700,991100,1052600];fy12=[2.4900,2.4710,2.5341,2.7471,2.9633,3.0759,3.4363,3.4617,3.5979]
fa13=[38000,46400,40730,49000,43870,44956,51670,67500,86000];fy13=[2.0605,2.3685,2.3597,2.3878,2.5500,2.7610,2.7710,3.0148,4.3321]
fa14=[26000,27000,27000,27000,22000,23000,24000,24000,25000];fy14=[1.8462,1.8519,2.1111,2.4074,3.0455,3.0435,3.0000,3.0000,3.0000]

fp1=N.multiply(fa1,fy1);fp2=N.multiply(fa2,fy2);fp3=N.multiply(fa3,fy3);fp4=N.multiply(fa4,fy4);fp5=N.multiply(fa5,fy5);fp6=N.multiply(fa6,fy6);fp7=N.multiply(fa7,fy7);
fp8=N.multiply(fa8,fy8);fp9=N.multiply(fa9,fy9);fp10=N.multiply(fa10,fy10);fp11=N.multiply(fa11,fy11);fp12=N.multiply(fa12,fy12);fp13=N.multiply(fa13,fy13);fp14=N.multiply(fa14,fy14)


#fao at 2000
#faop=[4216465,7203900,127464896,2859900,37627500,44300,4026092,51898000,20986900,12389412,25843878,32529500,2201700,2140800]
#faoy=[2.7028,3.0312,2.8508,3.4374,3.4836,1.7038,2.1155,4.4007,3.3301,3.0681,2.6128,4.2432,3.0606,3.0640]
#faoa=[1560044,2376600,44712000,832000,10801214,26000,1903159,11793000,6302175,4038085,9891200,7666300,719370,698700]


num=14
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
for idx in xrange(num):
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
	if idx==2:
                m3pmask=ma.masked_where(cou1<a1[idx],m3pmask)
                mareamask=ma.masked_where(cou1<a1[idx],mareamask)
                areak=ma.masked_where(cou1<a1[idx],areak)
                spama1=ma.masked_where(cou1<a1[idx],spama1)
                spamp1=ma.masked_where(cou1<a1[idx],spamp1)

                m3pmask=ma.masked_where(cou1>a2[idx],m3pmask)
                mareamask=ma.masked_where(cou1>a2[idx],mareamask)
	        areak=ma.masked_where(cou1>a2[idx],areak)
                spama1=ma.masked_where(cou1>a2[idx],spama1)
                spamp1=ma.masked_where(cou1>a2[idx],spamp1)

	elif idx==13:
	        for i in range(0,360):
        	        for j in range(0,720):
                        	if cou1[i,j]!=a1[idx] and cou1[i,j]!=a2[idx]:
                			m3pmask[i,j]=0
					areak[i,j]=0
                			mareamask[i,j]=0
              				spama1[i,j]=0
                			spamp1[i,j]=0

	else:
#		print idx
        	m3pmask=ma.masked_where(cou1!=a1[idx],m3pmask)
		mareamask=ma.masked_where(cou1!=a1[idx],mareamask)
                areak=ma.masked_where(cou1!=a1[idx],areak)
                spama1=ma.masked_where(cou1!=a1[idx],spama1)
                spamp1=ma.masked_where(cou1!=a1[idx],spamp1)

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


faoyy1=fp1/allgrid[0]*10000;faoyy2=fp2/allgrid[1]*10000;faoyy3=fp3/allgrid[2]*10000;faoyy4=fp4/allgrid[3]*10000;faoyy5=fp5/allgrid[4]*10000;faoyy6=fp6/allgrid[5]*10000;
faoyy7=fp7/allgrid[6]*10000;faoyy8=fp8/allgrid[7]*10000;faoyy9=fp9/allgrid[8]*10000;faoyy10=fp10/allgrid[9]*10000;faoyy11=fp11/allgrid[10]*10000;faoyy12=fp12/allgrid[11]*10000;faoyy13=fp13/allgrid[12]*10000;faoyy14=fp14/allgrid[13]*10000;



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

luharea=N.zeros((num))
allyisam_std=N.zeros((num))
allproisam_std=N.zeros((num))
isamgrid_std=N.zeros((num))

for idx in xrange(num):
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
        if idx==2:
                isampmask=ma.masked_where(cou<a1[idx],isampmask)
                isamarea=ma.masked_where(cou<a1[idx],isamarea)
                areak=ma.masked_where(cou<a1[idx],areak)
                aiizu=ma.masked_where(cou<a1[idx],aiizu)
                piizu=ma.masked_where(cou<a1[idx],piizu)

                areak=ma.masked_where(cou>a2[idx],areak)
                isampmask=ma.masked_where(cou>a2[idx],isampmask)
                isamarea=ma.masked_where(cou>a2[idx],isamarea)
                aiizu=ma.masked_where(cou>a2[idx],aiizu)
                piizu=ma.masked_where(cou>a2[idx],piizu)

        elif idx==13:
		for c in range(0,9):
	                for i in range(0,360):
	                        for j in range(0,720):
	                                if cou[c,i,j]!=a1[idx] and cou[c,i,j]!=a2[idx]:
	                                        isampmask[c,i,j]=0
	                                        isamarea[c,i,j]=0
                                                areak[c,i,j]=0
						aiizu[c,i,j]=0
						piizu[c,i,j]=0
        else:
                isampmask=ma.masked_where(cou!=a1[idx],isampmask)
                isamarea=ma.masked_where(cou!=a1[idx],isamarea)
                areak=ma.masked_where(cou!=a1[idx],areak)
                aiizu=ma.masked_where(cou!=a1[idx],aiizu)
                piizu=ma.masked_where(cou!=a1[idx],piizu)
	iizua1[idx]=N.average(N.sum(aiizu,axis=(1,2)))
        luharea[idx]=N.average(N.sum(isamarea,axis=(1,2)))
        iizup1[idx]=N.average((N.sum(piizu,axis=(1,2))))
        iizup1_std[idx]=N.std((N.sum(piizu,axis=(1,2))))

	iizuy1[idx]=N.average(N.sum(piizu,axis=(1,2))/(N.sum(aiizu,axis=(1,2))))
        iizuy1_std[idx]=N.std(N.sum(piizu,axis=(1,2))/(N.sum(aiizu,axis=(1,2))))
        iizuyg1[idx]=N.average((N.sum(piizu,axis=(1,2))/(N.sum(areak,axis=(1,2)))*10000))
        iizuyg1_std[idx]=N.std((N.sum(piizu,axis=(1,2))/(N.sum(areak,axis=(1,2)))*10000))

        allproisam[idx]=N.average((N.sum(isampmask,axis=(1,2))))
        allyisam[idx]=N.average(N.sum(isampmask,axis=(1,2))/(N.sum(isamarea,axis=(1,2))))
        allproisam_std[idx]=N.std((N.sum(isampmask,axis=(1,2))))
        allyisam_std[idx]=N.std(N.sum(isampmask,axis=(1,2))/(N.sum(isamarea,axis=(1,2))))
        isamgrid[idx]=N.average((N.sum(isampmask,axis=(1,2))/(N.sum(areak,axis=(1,2)))*10000))
        isamgrid_std[idx]=N.std((N.sum(isampmask,axis=(1,2))/(N.sum(areak,axis=(1,2)))*10000))

        iiallp[idx,:]=(N.sum(piizu,axis=(1,2)))
        iially[idx,:]=((N.sum(piizu,axis=(1,2)))/(N.sum(aiizu,axis=(1,2))))
        iiallg[idx,:]=((N.sum(piizu,axis=(1,2)))/(N.sum(areak,axis=(1,2)))*10000)


newm3y=N.zeros((360,720))
newisamy=N.zeros((360,720))
#newarea=N.zeros((360,720))
newm3p=N.zeros((360,720))
newisamp=N.zeros((360,720))
newm3y1=N.zeros((360,720))
newisamy1=N.zeros((360,720))


for i in range(1,15):
        kc=([allym3[i-1],spamyy[i-1]])
        locals()['fy{0}'.format(i)]=N.concatenate([locals()['fy{0}'.format(i)],kc])
        locals()['fy{0}'.format(i)]=N.concatenate([locals()['fy{0}'.format(i)],iially[i-1,:]])
#        print kc,locals()['fy{0}'.format(i)],allym3[i-1],iially[i-1,:]
        locals()['fy{0}'.format(i)]=N.asarray(locals()['fy{0}'.format(i)])
        locals()['fy{0}'.format(i)]= ma.masked_where(locals()['fy{0}'.format(i)]<=0.0,locals()['fy{0}'.format(i)])
        #print kc,locals()['fy{0}'.format(i)],allym3[i-1],iially[i-1,:]

        kc=([megrid[i-1],spamgrid[i-1]])
        locals()['faoyy{0}'.format(i)]=N.concatenate([locals()['faoyy{0}'.format(i)],kc])
        locals()['faoyy{0}'.format(i)]=N.concatenate([locals()['faoyy{0}'.format(i)],iiallg[i-1,:]])
        locals()['faoyy{0}'.format(i)]=N.asarray(locals()['faoyy{0}'.format(i)])
        locals()['faoyy{0}'.format(i)]= ma.masked_where(locals()['faoyy{0}'.format(i)]<=0.0,locals()['faoyy{0}'.format(i)])

	kc=([allprom3[i-1],spampp[i-1]])
        locals()['fp{0}'.format(i)]=N.concatenate([locals()['fp{0}'.format(i)],kc])
        locals()['fp{0}'.format(i)]=N.concatenate([locals()['fp{0}'.format(i)],iiallp[i-1,:]])
        locals()['fp{0}'.format(i)]=N.asarray(locals()['fp{0}'.format(i)])
        locals()['fp{0}'.format(i)]= ma.masked_where(locals()['fp{0}'.format(i)]<=0.0,locals()['fp{0}'.format(i)])

#print fp10
#print fy10
#print faoyy10
#print N.mean(fy5),N.ma.average(fy5)				
faop=[N.ma.average(fp1),N.ma.average(fp2),N.ma.average(fp3),N.ma.average(fp4),N.ma.average(fp5),N.ma.average(fp6),N.ma.average(fp7),N.ma.average(fp8),N.ma.average(fp9),N.ma.average(fp10),N.ma.average(fp11),N.ma.average(fp12),N.ma.average(fp13),N.ma.average(fp14)]
faop_std=[N.ma.std(fp1),N.ma.std(fp2),N.ma.std(fp3),N.ma.std(fp4),N.ma.std(fp5),N.ma.std(fp6),N.ma.std(fp7),N.ma.std(fp8),N.ma.std(fp9),N.ma.std(fp10),N.ma.std(fp11),N.ma.std(fp12),N.ma.std(fp13),N.ma.std(fp14)]

faoy=[N.ma.average(fy1),N.ma.average(fy2),N.ma.average(fy3),N.ma.average(fy4),N.ma.average(fy5),N.ma.average(fy6),N.ma.average(fy7),N.ma.average(fy8),N.ma.average(fy9),N.ma.average(fy10),N.ma.average(fy11),N.ma.average(fy12),N.ma.average(fy13),N.ma.average(fy14)]
faoy_std=[N.ma.std(fy1),N.ma.std(fy2),N.ma.std(fy3),N.ma.std(fy4),N.ma.std(fy5),N.ma.std(fy6),N.ma.std(fy7),N.ma.std(fy8),N.ma.std(fy9),N.ma.std(fy10),N.ma.std(fy11),N.ma.std(fy12),N.ma.std(fy13),N.ma.std(fy14)]

faoyy=[N.ma.average(faoyy1),N.ma.average(faoyy2),N.ma.average(faoyy3),N.ma.average(faoyy4),N.ma.average(faoyy5),N.ma.average(faoyy6),N.ma.average(faoyy7),N.ma.average(faoyy8),N.ma.average(faoyy9),N.ma.average(faoyy10),N.ma.average(faoyy11),N.ma.average(faoyy12),N.ma.average(faoyy13),N.ma.average(faoyy14)]
faoyy_std=[N.ma.std(faoyy1),N.ma.std(faoyy2),N.ma.std(faoyy3),N.ma.std(faoyy4),N.ma.std(faoyy5),N.ma.std(faoyy6),N.ma.std(faoyy7),N.ma.std(faoyy8),N.ma.std(faoyy9),N.ma.std(faoyy10),N.ma.std(faoyy11),N.ma.std(faoyy12),N.ma.std(faoyy13),N.ma.std(faoyy14)]


#faoy=[2.7028,3.0312,2.8508,3.4374,3.4836,1.7038,2.1155,4.4007,3.3301,3.0681,2.6128,4.2432,3.0606,3.0640]
#faoa=[1560044,2376600,44712000,832000,10801214,26000,1903159,11793000,6302175,4038085,9891200,7666300,719370,698700]

N.savetxt('datamai.csv', (allyisam, allyisam_std, faoy,faoy_std,allproisam,allproisam_std,faop,faop_std,isamgrid,isamgrid_std,faoyy,faoyy_std), delimiter=',')

print allyisam
print allyisam_std
print faoy
print faoy_std
print allproisam
print allproisam_std 
print faop
print faop_std
print isamgrid
print isamgrid_std
print faoyy
print faoyy_std
fig = plt.figure(figsize=(20,10))
n_groups = 14

#ax = fig.add_subplot(111)
index = N.arange(n_groups)
bar_width = 0.4
opacity = 1.0
rects1 = plt.bar(index+0.1, allyisam, bar_width,
                 alpha=opacity,
                 color='blue',
                 label='ISAM')
#rects1 = plt.bar(index+0.1, allyisam, bar_width,yerr=allyisam_std,ecolor='black', capsize=5,
#                 alpha=opacity,
#                 color='blue',
#                 label='ISAM')
#rects2 = plt.bar(index +0.18+ bar_width*1,allym3 , bar_width,
#                 alpha=opacity,
#                 color='g',
#                 label='M3')
rects0 = plt.bar(index + 0.1+bar_width*1, faoy, bar_width,yerr=faoy_std,ecolor='black', capsize=5,
                 alpha=opacity,
                 color='r',
                 label='Measured Data')
#rects3 = plt.bar(index + 0.18+bar_width*3, iizuy1, bar_width,yerr=iizuy1_std,ecolor='black', capsize=5,
#                 alpha=opacity,
#                 color='y',
#                 label='Iizumi')

plt.xlabel('Country',fontsize=35)
plt.ylabel('Yield (t / ha cropland)',fontsize=35)
#plt.ylabel('Yield (t / ha country)',fontsize=35)
plt.xticks(index + bar_width+0.11, ("Nepal","Pakistan","India","Sri Lanka","Bangladesh","Bhutan","Cambodia","Indonesia","Myanmar","Phillipines","Thailand","Vietnam","Laos","Malaysia"),rotation='vertical')
#lt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
leg=plt.legend(loc=1,ncol=3, fontsize=35)
#leg.get_frame().set_alpha(0.5)
plt.tick_params(axis='both',labelsize=35)


plt.tight_layout()
plt.savefig('maiyield1_countcombine.png')
plt.show()



fig = plt.figure(figsize=(20,10))
n_groups = 14

#ax = fig.add_subplot(111)
index = N.arange(n_groups)
bar_width = 0.4
opacity = 1.0
rects1 = plt.bar(index+0.1, allproisam, bar_width,yerr=allproisam_std,ecolor='black', capsize=5,
                 alpha=opacity,
                 color='blue',
                 label='ISAM')
#rects2 = plt.bar(index +0.18+ bar_width*1,allprom3 , bar_width,
#                 alpha=opacity,
#                 color='g',
#                 label='M3')
rects0 = plt.bar(index + 0.1+bar_width*1, faop, bar_width,yerr=faop_std,ecolor='black', capsize=5,
                 alpha=opacity,
                 color='r',
                 label='Other studies')
#rects3 = plt.bar(index + 0.18+bar_width*3, iizup1, bar_width,yerr=iizup1_std,ecolor='black', capsize=5,
#                 alpha=opacity,
#                 color='y',
#                 label='iizumi')

plt.xlabel('Country',fontsize=35)
plt.ylabel('Production (tonnes)',fontsize=35)
#plt.ylabel('Yield (t / ha country)',fontsize=35)
plt.xticks(index + bar_width+0.11, ("Nepal","Pakistan","India","Sri Lanka","Bangladesh","Bhutan","Cambodia","Indonesia","Myanmar","Phillipines","Thailand","Vietnam","Laos","Malaysia"),rotation='vertical')
#lt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
#leg=plt.legend(loc=2,ncol=3, fontsize=35)
#leg.get_frame().set_alpha(0.5)
plt.tick_params(axis='both',labelsize=35)


plt.tight_layout()
plt.savefig('maipro_countluh2combine.png')
plt.show()


fig = plt.figure(figsize=(20,10))
n_groups = 14

#ax = fig.add_subplot(111)
index = N.arange(n_groups)
bar_width = 0.4
opacity = 1.0
rects1 = plt.bar(index+0.1, isamgrid, bar_width,yerr=isamgrid_std,ecolor='black', capsize=5,
                 alpha=opacity,
                 color='blue',
                 label='ISAM')
#rects2 = plt.bar(index +0.18+ bar_width*1,megrid , bar_width,
#                 alpha=opacity,
#                 color='g',
#                 label='M3')
rects0 = plt.bar(index + 0.1+bar_width*1, faoyy, bar_width,yerr=faoyy_std,ecolor='black', capsize=5,
                 alpha=opacity,
                 color='r',
                 label='Other studies')
#rects0 = plt.bar(index + 0.18+bar_width*3, iizuyg1, bar_width,yerr=iizuyg1_std,ecolor='black', capsize=5,
#                 alpha=opacity,
#                 color='y',
#                 label='Iizumi')

plt.xlabel('Country',fontsize=35)
plt.ylabel('(t grains / ha country)',fontsize=35)
#plt.ylabel('Yield (t / ha country)',fontsize=35)
plt.xticks(index + bar_width+0.11, ("Nepal","Pakistan","India","Sri Lanka","Bangladesh","Bhutan","Cambodia","Indonesia","Myanmar","Phillipines","Thailand","Vietnam","Laos","Malaysia"),rotation='vertical')
#lt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=2, mode="expand", borderaxespad=0.)
#leg=plt.legend(loc=2,ncol=2, fontsize=35)
#leg.get_frame().set_alpha(0.5)
plt.tick_params(axis='both',labelsize=35)


plt.tight_layout()
plt.savefig('maiyield_countluh2combine.png')
plt.show()

