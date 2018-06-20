#!/bin/bash

#sleep 30

#cd /opt/spaceinfo
#git pull origin master

#feh --file list.txt  -F -D 1 -z -Z
while [ 1 ]; do
	for d in pages/*/ ; do
		if [ -f "$d/before.sh" ]; then
			bash before.sh
		fi
		if [ -f "$d/link.txt" ]; then
			echo "Loading link"
			firefox -url "`cat $d/link.txt`"
		elif [ -f "$d/index.html" ]; then
			echo "Loading index.html"
			firefox -url "$d/index.html"
		else
			echo "Error: $d does contain neither link.txt nor index.html"
			continue
		fi
		if [ -f "$d/after.sh" ]; then
			bash after.sh
		fi
		sleep 3
	done
	git pull origin master
done
