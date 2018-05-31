#!/bin/bash

git pull origin master

#feh --file list.txt  -F -D 1 -z -Z
while [ 1 ]; do
sudo fbi -T 1 -t 5 *.jpg -a -noverbose -u
sleep 10
git pull origin master
sudo killall fbi
done
