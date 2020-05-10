#!/bin/bash

d=`date '+%d-%m-%Y'`
t=`date '+%b %d %H:%M:%S '`
p=/install/EB
f=$p/APP-STATUS_$d.log

##CHECK DF FUNC
sysstate()
{
echo "$t CHECK MOUNTS POINTS... " >> $f
echo "$t CHECK MOUNTS POINTS... "
disk_data=`timeout 3s df -h`
if [ -z "$disk_data" ]
then
echo "$t MOUNT POINTS NOT AVAILABLE." >> $f
echo "$t MOUNT POINTS NOT AVAILABLE."
echo "$t DF COMMAND NOT RESPONDING. NOT OK." >> $f
echo "$t CHECK MOUNTS POINTS... NOT OK." >> $f
echo "$t CHECK MOUNTS POINTS... NOT OK."
echo "$t Contact Sys Admin." >> $f
echo "$t SCRIPT Exiting..." >> $f
exit
else
echo "$t MOUNTS POINTS AVAILABLE" >> $f
echo "$t MOUNT POINTS... OK." >> $f
echo "$t MOUNT POINTS... OK." 
fi
}
sysstate 

################################
start_db()
{
su - db2inst1 -c db2start
}

####################APP START FUNC
app_start()
{
start_db
app_path=/install/IBM/WebSphere/AppServer/profiles/AppSrv01/bin
appsrv=talcher
echo "$t TRYING TO  START APP SERVER." >> $f
echo "$t Starting App Server..." >> $f
echo "$t Starting App Server..."
sudo $app_path/startServer.sh $appsrv
resp_code=`timeout 3s curl --write-out "%{http_code}\n" --silent --output /dev/null "http://$(hostname)/navigator/login.jsp"`
rcode=200
if [ "$resp_code" == "$rcode" ]
then
echo "$t APP SERVER RC:200 OK." >> $f
echo "$t APP SERVER STARTED SUCCESSFULLY.. " >> $f
echo "$t APP SERVER STARTED SUCCESSFULLY.. "
else
echo "$t APP SERVER NOT STARTED, PLEASE CONTACT APP ADMIN" >> $f
echo "$t APP SERVER NOT STARTED, PLEASE CONTACT APP ADMIN"
fi
}
##############################33i
kill_jvm()
{
echo "$t KILL SCRIPT CALLED." >> $f 
echo "$t KILLING PID's... " >> $f
pids=`ps -ef | grep -i java | awk '{print $2}'`
for pid in $pids;
do
kill -9 $pid
echo "$t KILL SCRIPT RUN COMPLETE." >> $f
done
app_start
}

########
##APP STATE CHECK AND RESOLUTION
app_state() 
{
pscode=200
nscode=500
echo "$t CHECKING APP SERVER STATUS... " >> $f
echo "$t CHECKING APP SERVER STATUS... " 
app_code=`timeout 3s curl --write-out "%{http_code}\n" --silent --output /dev/null "http://$(hostname)/navigator/login.jsp"`
#app_code=500
status=$app_code
#echo $status
if [ "$status" == "$pscode" ]
then
echo "$t APP SERVER IS RUNNING WITH RC:200 OK. " >> $f
echo "$t APP SERVER STATUS... OK. " >> $f
echo "$t APP SERVER STATUS... OK. " 
exit
elif [ "$status" == "$nscode" ]
then
echo "$t APP SERVER STATUS... NOT OK." >> $f
echo "$t APP SERVER STATUS... NOT OK."
echo "$t APP SERVER IS NOT RUNNING WITH RC:500 NOT OK." >> $f
echo "$t CALLING APP START SCRIPT" >> $f
echo "$t CALLING APP START SCRIPT"
kill_jvm
elif [ -z "$status"  ]
then
echo "$t CHECKING APP SERVER STATUS... NOT OK." >> $f
echo "$t APP SERVER IS NOT RUNNING WITH RC:NULL NOT OK." >> $f
echo "$t APP SERVER IS NOT RUNNING WITH RC:NULL NOT OK."
echo "$t CALLING APP START SCRIPT" >> $f
echo "$t CALLING APP START SCRIPT"
kill_jvm
else 
echo "$t UNDEFINDED RCODE.. RESTARTING APP.." >> $f
kill_jvm
fi
}
app_state


