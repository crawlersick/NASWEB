#!/usr/bin/env bash
/home/sick/msda.sh
sleep 10
cd /home/sick/tools/autodown
pwd > /tmp/tttttt
nohup ./auto_down_bat.sh > /home/sick/Downloads/auto.log 2>&1 &
#nohup ./ep_autodown.sh > /tmp/ep.log 2>&1 &
cd /home/sick/NASWEB/src
#nohup ./run.sh > /tmp/NASWEB.log 2>&1 &
./runuwsgi.sh
exit 0
