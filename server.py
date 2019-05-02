#!/bin/python

import os
import json
import configparser
import sys
import logging

import signal

import flask
app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300

# Constants
VERSION_MAJOR = 0
VERSION_MINOR = 3
VERSION_PATCH = 0
VERSION = "v"+str(VERSION_MAJOR)+"."+str(VERSION_MINOR)+"."+str(VERSION_PATCH)


PORT = 8080
IP = "0.0.0.0"

# Setting up logger
logger = logging.getLogger('server.py')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

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

logger.info("Running version "+VERSION)
logger.info("Starting server...")
signal.signal(signal.SIGTERM, sigterm_handler)
signal.signal(signal.SIGINT, sigint_handler)

#def do_GET(s):
#	s.send_response(200)
#	s.send_header("Content-type","application/json; charset=utf-8")
#	s.end_headers()
#	s.wfile.write(generateDirectory("internal"))

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
    return flask.send_from_directory('pages', path)

@app.route('/version.json')
def getVersion():
	r = (json.dumps({"major":VERSION_MAJOR,"minor":VERSION_MINOR,"patch":VERSION_PATCH,"str":VERSION}, indent=2, sort_keys=True))
	resp = flask.make_response(r, 200)
	resp.headers["Content-type"] = "application/json; charset=utf-8"
	return resp


def getShows():
	p = os.path.relpath("pages")
	slideshows = []

	for d in os.listdir(p):
		if not os.path.isfile(os.path.join("pages",d)):
			for f in os.listdir(os.path.join("pages",d)):
				if f == "config.ini":
					config = configparser.ConfigParser()
					config.read(os.path.join("pages",d,f))
					try:
						for s in config["Page-Settings"]["slideshows"].split(" "):
							if s.strip() != "":
								slideshows.append(s)
					except KeyError:
						pass
	return list(set(slideshows))

def generateDirectory(slideshow):
	directory = []

	servername = ""
	logger.info("Generating directory for slideshow %s" % slideshow)
	DEFAULT_TIMEOUT = 60
	p = os.path.relpath("pages")

	for d in os.listdir(p):
		if not os.path.isfile(os.path.join("pages",d)):
			link = ""
			timeout = DEFAULT_TIMEOUT
			startdate = ""
			enddate = ""
			slideshows = []
			for f in os.listdir(os.path.join("pages",d)):
				if f == "config.ini":
					config = configparser.ConfigParser()
					config.read(os.path.join("pages",d,f))
					try:
						link = config["Page-Settings"]["external_link"]
					except KeyError:
						pass
					try:
						timeout = int(config["Page-Settings"]["timeout"])
					except KeyError:
						pass
					try:
						slideshows =  config["Page-Settings"]["slideshows"].split(" ")
					except KeyError:
						pass
					try:
						startdate = config["Page-Settings"]["startdate"]
					except KeyError:
						pass
					try:
						enddate = config["Page-Settings"]["enddate"]
					except KeyError:
						pass
				if f == "index.html":
					link = os.path.join(servername,"pages",d,f)
				else:
					pass

			# Checking for Errors
			if link == "":
				logger.error(os.path.join("pages",d)+" got no index.html neither config.cfg")
				continue
			if slideshow not in slideshows:
				continue
			directory.append({ "title": d, "link": link, "timeout": timeout, "startdate": startdate, "enddate": enddate})

	ret = (json.dumps(directory, indent=2, sort_keys=True))
	return ret
