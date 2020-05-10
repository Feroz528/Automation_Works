#!/bin/bash

for x in $(cat cp_app.txt);
do

printf "\nsh_"$x"=AdminTask.BPMShowSnapshot('[ -containerAcronym NTPCRT2 -containerSnapshotAcronym "$x" ]')"

printf "\nprint >> f, sh_"$x"" 


printf "\nda_"$x"=AdminTask.BPMDeactivate('[-containerAcronym NTPCRT2 -containerSnapshotAcronym "$x"]') "

printf "\nprint >> f, da_"$x"" 


printf "\nst_"$x"=AdminTask.BPMStop('[-containerAcronym NTPCRT2 -containerSnapshotAcronym "$x"]')" 

printf "\nprint >> f, st_"$x""

printf "\nun_"$x"=AdminTask.BPMUndeploy('[-containerAcronym NTPCRT2 -containerSnapshotAcronym "$x"]')"

printf "\nprint >> f, un_"$x""

printf "\ndel_"$x"=AdminTask.BPMDeleteSnapshot('[-containerAcronym NTPCRT2 -containerSnapshotAcronyms "$x"]')"

printf "\nprint >> f, del_"$x"\n"

done
