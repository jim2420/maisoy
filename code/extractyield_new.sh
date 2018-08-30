#!/bin/sh
module load cdo

echo "writing out yield"

name=( soy_irr_fert soy_fert soy_irr soy_co2  soy_cli )

for i in {5..5}
do
 for f in {1901..2016}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/new/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,totalyield *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}.nc
rm sam_*.nc
rm crop_*.nc
done
 
name=( soyequilibrium_cli soyequilibrium_fert soyequilibrium_irr soyequilibrium_co2  soyequilibrium )

for i in {0..4}
do
 for f in {1901..2016}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/new/equili/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,totalyield *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}.nc
rm sam_*.nc
rm crop_*.nc
done

