#!/bin/sh
module load cdo

echo "writing out yield"

name=( soy_irr_fert mai_irr_fert soy_irr mai_co2 soy_co2 mai_irr soy_cli mai_cli mai_fert soy_fert)

for i in {0..9}
do
 for f in {2015..2100}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85new/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,g_ET,totalyield *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}.nc
rm sam_*.nc
rm crop_*.nc
done
 

name=(  soyequilibrium_irr maiequilibrium_irr soyequilibrium maiequilibrium soyequilibrium_co2 maiequilibrium_co2 soyequilibrium_cli maiequilibrium_cli soyequilibrium_fert maiequilibrium_fert)
for i in {0..9}
do
 for f in {2015..2100}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85new/equili/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,g_ET,totalyield *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}.nc
rm sam_*.nc
rm crop_*.nc
done

