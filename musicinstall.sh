#!/bin/bash
apt-get install git libao-dev libssl-dev libcrypt-openssl-rsa-perl libio-socket-inet6-perl libwww-perl avahi-utils
git clone https://github.com/albertz/shairport.git shairport
cd shairport
bash configure.sh
make
make install
cp shairport.init.sample /etc/init.d/shairport
cd /etc/init.d
chmod a+x shairport
update-rc.d shairport defaults


cat > /etc/apt/sources.list.d/upmpdcli.list $"deb http://www.lesbonscomptes.com/upmpdcli/downloads/raspbian/ stretch main\ndeb-src http://www.lesbonscomptes.com/upmpdcli/downloads/raspbian/ stretch main"
apt install dirmngr
gpg --keyserver pool.sks-keyservers.net --recv-key F8E3347256922A8AE767605B7808CE96D38B9201
gpg --export '7808CE96D38B9201' | sudo apt-key add -
apt-get update
apt-get install upmpdcli mpd






nano /etc/upmpdcli.conf

cd /etc/init.d
nano shairport
cd /opt/spaceinfo
