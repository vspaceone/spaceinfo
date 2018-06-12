#!/bin/bash

apt install fbi git

cd /opt

git clone https://github.com/vspaceone/spaceinfo.git

cd spaceinfo


mkdir /etc/spaceinfo

cp spaceinfo.service //lib/systemd/system/spaceinfo.service

systemctl daemon-reload

chmod +x spaceinfo.sh

chmod +x musicinstall.sh

bash musicinstall.sh

echo "Starting Spaceinfo Script..."

bash spaceinfo.sh

systemctl enable spaceinfo

systemctl start spaceinfo
