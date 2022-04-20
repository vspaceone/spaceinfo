#!/bin/bash

export PATH=$PATH:~/.local/bin
export FLASK_APP=server.py
flask run --host="0.0.0.0" --port="5000"
