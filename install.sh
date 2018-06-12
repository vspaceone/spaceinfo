#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

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

echo "starting spaceinfo service..."

systemctl enable spaceinfo

echo "sss::end"

echo "SS::START"

systemctl start spaceinfo
