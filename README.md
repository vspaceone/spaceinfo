# spaceinfo

Dieses kleine Script läuft auf den Infoterminals im Space.

## So sieht das bei uns aus:
![Bildschirme im Space](spaceinfo.jpg)

## Install
```
pip install flask
bash run.sh
```

## Wie kann ich Pages anlegen
Leg einen Unterordner von `pages` an, in dem eine `index.html` oder eine `link.txt` Datei liegt. Wird eine `link.txt` Datei gefunden wird der darin enthaltene Link geöffnet. Andern falls wird die `index.html` angezeigt.

Einige Beispiel habe ich bereits unter `templates` abgelegt.

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
