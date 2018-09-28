#!/bin/bash

sleep 30

cd /opt/spaceinfo
git pull origin master

#feh --file list.txt  -F -D 1 -z -Z
while [ 1 ]; do
	echo "New loop started"
	sudo fbi -T 1 -t 20 /opt/spaceinfo/imgs/* -a -noverbose -u
	sleep 1800
	git pull origin master
	sudo killall fbi
done
