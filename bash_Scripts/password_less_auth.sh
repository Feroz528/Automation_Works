#!/bin/bash

for ip in $(cat /home/root_EB/bash_Scripts/prod.txt); do

echo "Ip addresses: " $ip
ssh-copy-id -i ~/.ssh/id_rsa.pub $ip
#sshpass -f password.txt ssh-copy-id root_EB@$ip
done
