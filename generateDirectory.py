#!/bin/python

import os
import json
import configparser
import sys
import logging

# Constants
VERSION_MAJOR = 0
VERSION_MINOR = 1
VERSION_PATCH = 0
VERSION = "v"+str(VERSION_MAJOR)+"."+str(VERSION_MINOR)+"."+str(VERSION_PATCH)
# Setting up logger
logger = logging.getLogger('generateDirectory.py')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)


def printUsage():
	print("Usage: generateDirectory.py <slideshow> <servername>")
	print("slideshow:  Adds only pages where this slideshow is")
	print("            noted in the configfile.")
	print("servername: Name the server spaceinfo is running on,")
	print("            so the local pages could be prefixed.")
	print("            Don't forget http(s)://")


def main():

	directory = []

	try:
		slideshow = sys.argv[1]
		servername = sys.argv[2]
	except IndexError:
		printUsage()
		exit()

	logger.info("Running version "+VERSION)
	logger.info("Generating directory for slideshow %s" % slideshow)


	DEFAULT_TIMEOUT = 10

	p = os.path.relpath("pages")

	for d in os.listdir(p):
		if not os.path.isfile(os.path.join("pages",d)):
			link = ""
			timeout = DEFAULT_TIMEOUT
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
						timeout = config["Page-Settings"]["timeout"]
					except KeyError:
						pass
					try:
						slideshows =  config["Page-Settings"]["slideshows"].split(" ")
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
			directory.append({ "link": link, "timeout": timeout })

	file = open("directory_"+slideshow+".json","w")
	file.write(json.dumps(directory, indent=2, sort_keys=True))
	file.close()
	logger.info(file.name+" written")

if __name__ == '__main__':
	main()
	logger.info("Finished")
else:
	print("Run this script as main pls!")



