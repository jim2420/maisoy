#!/bin/sh
module load cdo

echo "writing out yield"



name=(maiequilibrium maiequilibrium_fert maiequilibrium_irr maiequilibrium_co2 maiequilibrium_cli soyequilibrium soyequilibrium_fert soyequilibrium_co2 soyequilibrium_irr soyequilibrium_cli)
for i in {0..9}
do
 for f in {1901..2016}
  do
   echo $f ${name[i]}  
  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/his_cru/equili/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,irrigation *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}_irr.nc
rm sam_*.nc
rm crop_*.nc
done

for i in {0..9}
do
 for f in {2015..2100}
  do
   echo $f ${name[i]}  
  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/equili/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,irrigation *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}_irr.nc
rm sam_*.nc
rm crop_*.nc
done
 

for i in {0..9}
do
 for f in {2015..2100}
  do
   echo $f ${name[i]}  
  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/equili/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,irrigation *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}_irr.nc
rm sam_*.nc
rm crop_*.nc
done

