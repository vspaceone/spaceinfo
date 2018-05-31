#!/bin/bash


#feh --file list.txt  -F -D 1 -z -Z
while [ 1 ]; do
git pull origin master
sudo fbi -T 1 -t 5 *.jpg -a -noverbose -u
sleep 10
sudo killall fbi
done
