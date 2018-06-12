#!/bin/bash

sudo apt install fbi

mkdir /etc/spaceinfo

cp spaceinfo.service //lib/systemd/system/spaceinfo.service

systemctl daemon-reload

chmod +x spaceinfo.sh
