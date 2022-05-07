#!/bin/python

import os
import json
import configparser
import sys
import logging
from urllib.parse import unquote
import signal
import pathlib
import flask
import jinja2


from Page import Page,PageType

# Constants
VERSION_MAJOR = 0
VERSION_MINOR = 4
VERSION_PATCH = 3
VERSION = "v"+str(VERSION_MAJOR)+"."+str(VERSION_MINOR)+"."+str(VERSION_PATCH)




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

pathToPages = pathlib.Path("../spaceinfo-pages/pages")
pathToTemplates = pathlib.Path("../spaceinfo-pages/templates")

serverconfig = configparser.RawConfigParser()
serverconfig.read("config.ini")

try:
	pathToPages = pathlib.Path(serverconfig["Server-Settings"]["pathToPages"].replace("\\\\","\\"))
	logger.warning(pathToPages)
except:
	pass

try:
	pathToTemplates = pathlib.Path(serverconfig["Server-Settings"]["pathToTemplates"].replace("\\\\","\\"))
	logger.warning(pathToPages)
except:
	pass

assert pathToPages.exists()
assert pathToTemplates.exists()

DEFAULTS = dict({
	"timeout": 60,
	"startdate": "",
	"enddate": ""
})


app = flask.Flask(__name__)
my_loader = jinja2.ChoiceLoader([
app.jinja_loader,
	jinja2.FileSystemLoader(pathToTemplates),
])
app.jinja_loader = my_loader

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'must-validate'
    return response

# Register signal handlers
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

@app.route('/pages/<pagename>/<path:path>')
def sendStatic(pagename,path):
	page = Page(pathToPages / pagename, DEFAULTS)
	path = pathlib.Path(path)

	if (pathToPages / pagename / path).exists():
		return flask.send_from_directory(pathToPages / pagename, path)
	else:
		resp = flask.make_response(flask.render_template(page.template, template_folder=pathToTemplates, **page.template_params), 200)
		resp.headers["Content-type"] = "text/html; charset=utf-8"
		return resp


@app.route('/version.json')
def getVersion():
	r = (json.dumps({"major":VERSION_MAJOR,"minor":VERSION_MINOR,"patch":VERSION_PATCH,"str":VERSION}, indent=2, sort_keys=True))
	resp = flask.make_response(r, 200)
	resp.headers["Content-type"] = "application/json; charset=utf-8"
	return resp


def getShows():
	slideshows = []

	for directory in pathToPages.iterdir():
		if not directory.is_file():
			print(directory,Page(directory,DEFAULTS).slideshows)
			slideshows.extend(Page(directory,DEFAULTS).slideshows)
	return list(set(slideshows))

def generateDirectory(slideshow):
	result = []

	servername = ""
	logger.info("Generating directory for slideshow %s" % slideshow)
	
	for directory in pathToPages.iterdir():
		if not directory.is_file():
			page = Page(directory,DEFAULTS)
			if slideshow in page.slideshows:
				result.append({ "title": str(directory), "link": str(page.link), "timeout": int(page.timeout), "startdate": page.startdate, "enddate": page.enddate})

	ret = (json.dumps(result, indent=2, sort_keys=True))
	return ret
