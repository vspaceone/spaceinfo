# spaceinfo

This repo provides as interface for displaying multiple webpages in a slideshow.

## So sieht das bei uns aus:
![Bildschirme im Space](spaceinfo.jpg)

## Install
Install python, pip, flask.

More information follows.

## Run
```
bash run.sh
```
This runs on localhost. You have to configure your nginx or apache to redirect to port 8080 from the given url.

## Wie kann ich Pages anlegen
Leg einen Unterordner von `pages` an, in dem eine `index.html` oder eine `link.txt` Datei liegt. Wird eine `link.txt` Datei gefunden wird der darin enthaltene Link geöffnet. Andern falls wird die `index.html` angezeigt.

Einige Beispiel habe ich bereits unter `templates` abgelegt.

## Schwarze Ränder auf RaspberryPi
Disable Overscan via `raspi-config` - `Advanced Options` - `Overscan`

## Licence
Siehe [LICENCE](LICENCE.md)
