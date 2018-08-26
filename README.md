# spaceinfo

Dieses kleine Script läuft auf den Infoterminals im Space.

## Install
Installiere `fbi` und `git`. Checke das Repo nach `/opt/spaceinfo` aus und führe das `install.sh`-Skript aus. Der Service ist dann registiert und kann angeschalten werden.

```
sudo apt install fbi git firefox
cd /opt
git clone https://github.com/vspaceone/spaceinfo.git
cd spaceinfo
sudo bash install.sh
sudo systemctl enable spaceinfo
sudo systemctl start spaceinfo
```

## Wie kann ich Pages (nur FirefoxPages Branch)
Leg einen Unterordner von `pages` an, in dem eine `index.html` oder eine `link.txt` Datei liegt. Wird eine `link.txt` Datei gefunden wird der darin enthaltene Link geöffnet. Andern falls wird die `index.html` angezeigt.

Einige Beispiel habe ich bereits unter `templates` abgelegt.

## Wie kann ich Bilder hinzufügen?
Einfach ein mit 1920x1200 Pixeln und im .jpg Format committen und etwas warten. Die Infoterminals holen sich mehrmals täglich die aktualisierten Bilder von GitHub.

## Bitte die folgenden Dateien nicht im Masterbranch bearbeiten!

+ aptinstall.sh
+ install.sh
+ spaceinfo.sh
+ spaceinfo.service

## Licence
Siehe [LICENCE](LICENCE.md)
