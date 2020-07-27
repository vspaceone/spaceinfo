#!/bin/python

import os
import json
import configparser
import sys
import logging
from urllib.parse import unquote
import signal

import flask


# Constants
VERSION_MAJOR = 0
VERSION_MINOR = 4
VERSION_PATCH = 2
VERSION = "v"+str(VERSION_MAJOR)+"."+str(VERSION_MINOR)+"."+str(VERSION_PATCH)


# Defaults
pathToPages = "../spaceinfo-pages"

# Setting up logger
logger = logging.getLogger('server.py')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(lineno)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)



logger.info("Running version "+VERSION)
logger.info("Starting server...")


#def do_GET(s):
#	s.send_response(200)
#	s.send_header("Content-type","application/json; charset=utf-8")
#	s.end_headers()
#	s.wfile.write(generateDirectory("internal"))

srvconfig = configparser.RawConfigParser()
srvconfig.read("config.ini")

try:
	pathToPages = srvconfig["Server-Settings"]["pathToPages"].replace("\\\\","\\")
	logger.warning(pathToPages)
except:
	pass

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300
#app.config["SERVER_NAME"] = "127.0.0.1:8080"

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'must-validate'
    return response

def sigterm_handler(_signo,_stack_frame):
	logger.info("SIGTERM received. Cleaning up...")
	sys.exit(0)

def sigint_handler(_signo, _stack_frame):
	logger.info("SIGINT received. Cleaning up...")
	sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)
signal.signal(signal.SIGINT, sigint_handler)



def printUsage():
	print("Usage: server.py")

@app.route("/")
def listShows():
	print(getShows())
	resp = flask.make_response(flask.render_template('home.html', shows = getShows(), version=VERSION), 200)
	resp.headers["Content-type"] = "text/html; charset=utf-8"
	return resp

@app.route("/shows/<showname>.json")
def loadShowJSON(showname):
	resp = flask.make_response(generateDirectory(showname), 200)
	resp.headers["Content-type"] = "application/json; charset=utf-8"
	return resp

@app.route("/shows/<showname>.html")
def displayShow(showname):
	resp = flask.make_response(flask.render_template('start.html', showname=showname, version=VERSION), 200)
	resp.headers["Content-type"] = "text/html; charset=utf-8"
	return resp

@app.route("/shows/overviews/<showname>.html")
def displayShowOverview(showname):
	resp = flask.make_response(flask.render_template('overview.html', showname=showname, version=VERSION), 200)
	resp.headers["Content-type"] = "text/html; charset=utf-8"
	return resp

@app.route('/pages/<path:path>')
def sendStatic(path):
    return flask.send_from_directory(pathToPages, path)

@app.route('/version.json')
def getVersion():
	r = (json.dumps({"major":VERSION_MAJOR,"minor":VERSION_MINOR,"patch":VERSION_PATCH,"str":VERSION}, indent=2, sort_keys=True))
	resp = flask.make_response(r, 200)
	resp.headers["Content-type"] = "application/json; charset=utf-8"
	return resp


def getShows():
	p = os.path.relpath(pathToPages)
	slideshows = []

	for d in os.listdir(p):
		if not os.path.isfile(os.path.join(pathToPages,d)):
			for f in os.listdir(os.path.join(pathToPages,d)):
				if f == "config.ini":
					config = configparser.RawConfigParser()
					try:
						config.read(os.path.join(pathToPages,d,f))
						for s in config["Page-Settings"]["slideshows"].split(" "):
							if s.strip() != "":
								slideshows.append(s)
					except Exception as e:
						print(e)
						pass
	return list(set(slideshows))

def generateDirectory(slideshow):
	directory = []

	servername = ""
	logger.info("Generating directory for slideshow %s" % slideshow)
	DEFAULT_TIMEOUT = 60
	p = os.path.relpath(pathToPages)

	for d in os.listdir(p):
		if not os.path.isfile(os.path.join(pathToPages,d)):
			link = ""
			timeout = DEFAULT_TIMEOUT
			startdate = ""
			enddate = ""
			slideshows = []
			for f in os.listdir(os.path.join(pathToPages,d)):
				if f == "config.ini":
					config = configparser.RawConfigParser()
					config.read(os.path.join(pathToPages,d,f))


					try:
						link = config["Page-Settings"]["external_link"].strip('\"')
					except Exception as e:
						pass
					try:
						timeout = int(config["Page-Settings"]["timeout"])
					except Exception as e:
						pass
					try:
						slideshows =  config["Page-Settings"]["slideshows"].split(" ")
					except Exception as e:
						pass
					try:
						startdate = config["Page-Settings"]["startdate"]
					except Exception as e:
						pass
					try:
						enddate = config["Page-Settings"]["enddate"]
					except Exception as e:
						pass
				if f == "index.html":
					link = os.path.join(servername,"pages",d,f)
				else:
					pass

			# Checking for Errors
			if link == "":
				logger.error(os.path.join(pathToPages,d)+" got no index.html neither config.ini")
				continue
			if slideshow not in slideshows:
				continue
			directory.append({ "title": d, "link": link, "timeout": timeout, "startdate": startdate, "enddate": enddate})

	ret = (json.dumps(directory, indent=2, sort_keys=True))
	return ret
