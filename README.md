# spaceinfo

Dieses kleine Script läuft auf den Infoterminals im Space.

## Install
Installiere `fbi` und `git`. Checke das Repo nach `/opt/spaceinfo` aus und führe das `install.sh`-Skript aus. Der Service ist dann registiert und kann angeschalten werden.

```
sudo apt install fbi git
cd /opt
git clone https://github.com/vspaceone/spaceinfo.git
cd spaceinfo
sudo bash install.sh
sudo systemctl enable spaceinfo
sudo systemctl start spaceinfo
```

## Wie kann ich Bilder hinzufügen?
Einfach ein mit 1920x1200 Pixeln und im .jpg Format committen und etwas warten. Die Infoterminals holen sich mehrmals täglich die aktualisierten Bilder von GitHub.

## Schwarze Ränder auf RaspberryPi
Disable Overscan via `raspi-config` - `Advanced Options` - `Overscan`

## Bitte die folgenden Dateien nicht im Masterbranch bearbeiten!

+ aptinstall.sh
+ install.sh
+ spaceinfo.sh
+ spaceinfo.service

## Licence
Siehe [LICENCE](LICENCE.md)
