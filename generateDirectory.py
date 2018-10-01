#!/bin/python

import os
import json
import configparser

p = os.path.relpath("pages")
config = configparser.ConfigParser()

directory = []
DEFAULT_TIMEOUT = 10

for d in os.listdir(p):
	if not os.path.isfile(os.path.join("pages",d)):
		link = ""
		timeout = DEFAULT_TIMEOUT
		for i in os.listdir(os.path.join("pages",d)):
			if i == "config.cfg":
				config.read(os.path.join("pages",d,i))
				link = config["Page-Settings"]["external_link"]
				timeout = config["Page-Settings"]["timeout"]
			if i == "index.html":
				link = os.path.join("http://spaceinfo.noppelmax.online","pages",d,i)
			else:
				pass

		# Checking for Errors
		if link == "":
			print("ERR: "+os.path.join("pages",d)+" got no index.html neither config.cfg")
			continue
		directory.append({ "link": link, "timeout": timeout })


print json.dumps(directory, indent=2, sort_keys=True)




