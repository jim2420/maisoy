#!/bin/sh
module load cdo

echo "writing out yield"



name=(mai_cli mai_co2 mai_fert mai_irr  mai_irr_fert soy_cli soy_co2 soy_fert soy_irr soy_irr_fert)
for i in {0..9}
do
 for f in {1901..2016}
  do
   echo $f ${name[i]}  
  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,g_ET,totalyield *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}.nc
rm sam_*.nc
rm crop_*.nc
done


