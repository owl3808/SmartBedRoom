#!/bin/bash
CWD=$PWD
BASEDIR="$(readlink -f $(dirname $0))"

if [ ! "$(whoami)" == "root" ]; then
	echo "should run as root, try 'sudo ./start.sh'"
	exit
fi
cd $BASEDIR
python /home/pi/SmartBedRoom/SmartBedRoom.py
