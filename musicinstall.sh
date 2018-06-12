#!/bin/bash
sudo apt-get install git libao-dev libssl-dev libcrypt-openssl-rsa-perl libio-socket-inet6-perl libwww-perl avahi-utils
sudo git clone https://github.com/albertz/shairport.git shairport
cd shairport
sudo make
sudo make install
sudo cp shairport.init.sample /etc/init.d/shairport
cd /etc/init.d
sudo chmod a+x shairport
sudo update-rc.d shairport defaults


sudo cat > /etc/apt/sources.list.d/upmpdcli.list "deb http://www.lesbonscomptes.com/upmpdcli/downloads/raspbian/ stretch main deb-src
http://www.lesbonscomptes.com/upmpdcli/downloads/raspbian/ stretch main"
sudo apt install dirmngr
gpg --keyserver pool.sks-keyservers.net --recv-key F8E3347256922A8AE767605B7808CE96D38B9201
gpg --export '7808CE96D38B9201' | sudo apt-key add -
sudo apt-get update
sudo apt-get install upmpdcli






sudo nano /etc/upmpdcli.conf

cd /etc/init.d
sudo nano shairport
