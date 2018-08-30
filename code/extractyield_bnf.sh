#!/bin/sh
module load cdo

echo "writing out yield"

name=( soy_irr_fert soy_fert mai_co2_cli soy_co2_cli soy_irr_fert mai_irr_fert soy_irr mai_co2 soy_co2 mai_irr soy_cli mai_cli)

for i in {0..1}
do
 for f in {1901..2016}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/vmax1/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,annual_nfix *.bgc-yearly-3d_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}_bnf.nc
rm sam_*.nc
rm crop_*.nc
done
 
