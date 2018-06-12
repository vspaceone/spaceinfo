#!/bin/bash

sudo apt install fbi

mkdir /etc/spaceinfo

cp spaceinfo.service //lib/systemd/system/spaceinfo.service

systemctl daemon-reload

chmod +x spaceinfo.sh

chmod +x musicinstall.sh

./musicinstall.sh

echo "Starting Spaceinfo Script..."

./spaceinfo.sh
