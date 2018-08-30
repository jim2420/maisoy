#!/bin/sh
module load cdo

echo "writing out yield"

name=( soy_cli soy_co2 soy_fert soy_irr soy_irr_fert)

for i in {0..4}
do
 for f in {2015..2100}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/noaclimate/${name[i]}/output
#  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,totalyield *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}.nc
rm sam_*.nc
rm crop_*.nc
done
 

for i in {0..4}
do
 for f in {2015..2100}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/noaclimate/${name[i]}/output
#  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,totalyield *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}.nc
rm sam_*.nc
rm crop_*.nc
done
name=( soyequilibrium soyequilibrium_fert soyequilibrium_co2 soyequilibrium_irr soyequilibrium_cli)
for i in {0..4}
do
 for f in {2015..2100}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/noaclimate/equili/${name[i]}/output
#  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp45/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,totalyield *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}.nc
rm sam_*.nc
rm crop_*.nc
done


for i in {0..4}
do
 for f in {2015..2100}
  do
   echo $f ${name[i]}  
cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/noaclimate/equili/${name[i]}/output
#  cd /scratch2/scratchdirs/tslin2/isam/maisoy_cheyenne/rcp85/${name[i]}/output
   echo *_crop_$f.nc crop_$f.nc
   cdo selname,totalyield *_crop_$f.nc crop_$f.nc
   cdo setyear,$f crop_$f.nc sam_$f.nc
  done
cdo mergetime sam_*.nc ${name[i]}.nc
rm sam_*.nc
rm crop_*.nc
done

