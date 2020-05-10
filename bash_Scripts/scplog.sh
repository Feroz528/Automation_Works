#!/bin/bash

for f in $(cat bpmprod);
do 
ssh root_EB@$f hostname $up
echo $up 
scp root_EB@$f:/install/EB/BpmCustomLogs/archive/NTPCPPF-2020-04-15-1.log.gz '$up'_log.tar.gz

done

