#!/bin/bash

for ip in $(cat idb);
do
echo $ip;
ssh root_EB@$ip "sudo su - db2inst1 -c 'db2 list db directory && db2 list active databases'"

done
