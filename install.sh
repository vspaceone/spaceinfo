#!/bin/bash


mkdir /opt/tempLogger

rm /opt/tempUpdater/tempLogger.sh

cp tempLogger.sh /opt/tempLogger/

mkdir /etc/tempLogger

cp tempLogger.service //lib/systemd/system/tempLogger.service

systemctl daemon-reload
