#!/bin/sh
module load cdo

echo "writing out yield"



name=(maiequilibrium maiequilibrium_fert maiequilibrium_irr maiequilibrium_co2 maiequilibrium_cli soyequilibrium soyequilibrium_fert soyequilibrium_co2 soyequilibrium_irr soyequilibrium_cli)
for i in {1..1}
do
 for f in {1901..2016}
  do
   echo $f ${name[i]}  
  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,g_ET,totalyield *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}.nc
rm sam_*.nc
rm crop_*.nc
done


