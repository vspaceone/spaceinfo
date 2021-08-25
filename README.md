# spaceinfo

This repo provides as interface for displaying multiple webpages in a slideshow.

## So sieht das bei uns aus:
![Bildschirme im Space](spaceinfo.jpg)

## Install
### Install via anaconda
```
conda create --name spaceinfo python=3.5
conda activate spaceinfo
pip install -r requirements.txt
```
### Install via venv
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

Activate the environment with
```
conda activate spaceinfo
```
if you use anaconda and 
```
source venv/bin/activate
```
if you use venv. Then run

```
bash run.sh
```

This runs on localhost. You have to configure your nginx or apache to redirect to port 8080 from the given url.

## How to add slides?
Add your slides to the [spaceinfo-pages](https://github.com/vspaceone/spaceinfo-pages) repository to show them in on the spaceinfo-terminals.

## Schwarze Ränder auf RaspberryPi
Disable Overscan via `raspi-config` - `Advanced Options` - `Overscan`

## Licence
Siehe [LICENCE](LICENCE.md)
