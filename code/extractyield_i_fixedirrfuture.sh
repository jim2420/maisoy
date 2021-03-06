#!/bin/sh
module load cdo

echo "writing out yield"

name=( soy_irr_fert mai_irr_fert soy_irr mai_co2 soy_co2 mai_irr soy_cli mai_cli)

for i in {0..7}
do
 for f in {2015..2100}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/fixedirr/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,totalyield *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}.nc
rm sam_*.nc
rm crop_*.nc
done
 

name=(  soyequilibrium_irr maiequilibrium_irr )
for i in {0..1}
do
 for f in {2015..2100}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/fixedirr/equili/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,totalyield *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}.nc
rm sam_*.nc
rm crop_*.nc
done

