#!/bin/sh
module load cdo

name=(maiequilibrium maiequilibrium_fert maiequilibrium_irr maiequilibrium_co2 maiequilibrium_cli soyequilibrium soyequilibrium_fert soyequilibrium_co2 soyequilibrium_irr soyequilibrium_cli)
for i in {0..9}
do
 for f in {1901..2016}
  do
   echo $f ${name[i]}  
  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,g_ET *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}_evp.nc
rm sam_*.nc
rm crop_*.nc
done


echo "writing out yield"
name=( mai_co2_irr soy_co2_irr mai_co2_fert soy_co2_fert mai_co2_cli soy_co2_cli soy_irr_fert mai_irr_fert soy_irr mai_co2 soy_co2 mai_irr soy_cli mai_cli)

for i in {0..13}
do
 for f in {1901..2016}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/fixedirr/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,g_ET *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}_evp.nc
rm sam_*.nc
rm crop_*.nc
done


name=(  soyequilibrium_irr maiequilibrium_irr )
for i in {0..1}
do
 for f in {1901..2016}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/fixedirr/equili/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,g_ET *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}_evp.nc
rm sam_*.nc
rm crop_*.nc
done



name=(mai_cli mai_co2 mai_fert mai_irr  mai_irr_fert soy_cli soy_co2 soy_fert soy_irr soy_irr_fert)
for i in {0..9}
do
 for f in {1901..2016}
  do
   echo $f ${name[i]}  
  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,g_ET *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}_evp.nc
rm sam_*.nc
rm crop_*.nc
done

for i in {0..9}
do
 for f in {2015..2100}
  do
   echo $f ${name[i]}  
  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,g_ET *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}_evp.nc
rm sam_*.nc
rm crop_*.nc
done
 

for i in {0..9}
do
 for f in {2015..2100}
  do
   echo $f ${name[i]}  
  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,g_ET *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}_evp.nc
rm sam_*.nc
rm crop_*.nc
done

