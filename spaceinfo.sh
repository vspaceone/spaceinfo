#!/bin/bash

#sleep 30

#cd /opt/spaceinfo
#git pull origin master

#feh --file list.txt  -F -D 1 -z -Z
while [ 1 ]; do
	for d in pages/*/ ; do
		if [ -f "$d/link.txt" ]; then
			firefox -url "`cat $d/link.txt`"
		else
			firefox -url "$d/index.html"
		fi
		sleep 5
	done
	git pull origin master
done
