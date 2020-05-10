#!/bin/bash

echo "*=*=*=*=*=*=*$(hostname)*=*=*=*=*=*=*"  >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"

echo >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"

echo "****$(date)****"  >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"

echo >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"

echo "$(hostname) is up and running since $(uptime -p)"  >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"

echo >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"

echo "==================DISK USAGE INFO==================="  >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"
df -hT >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"

echo >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"

echo "==================MEMORY INFO====================="  >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"
free -g >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"

echo  >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"

#echo "DB2 STATUS" >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"

#sudo su - db2inst1 -c "db2start" >> /home/root_EB/EB/results/$(hostname -s)/"$(hostname -s).$(date +"%Y-%m-%d")_sysinfo.txt"
