
import configparser
import os
from enum import Enum
import pathlib


class PageType(Enum):
    INDEXHTML=1
    TEMPLATE=2
    EXTERNALLINK=3



class Page:
    """
    """
    def __init__(self, directory, defaults):

        self.indexhtml_link = None
        self.template = None
        self.external_link = None

        self.directory = directory
        self.defaults = defaults

        # Iterate over the page-directory
        for f in os.listdir(directory):
            if f == "config.ini":
                self._parse_config(directory / f)
            if f == "index.html":
                self.indexhtml_link = pathlib.Path("pages") / directory.name / f
            else:
                # Skip all the other files
                pass

        # index.html overwrites template overwrites external_link
        if not self.indexhtml_link is None:
            self.link = self.indexhtml_link
            self.pagetype = PageType.INDEXHTML

        elif not self.template is None:
            self.link = pathlib.Path("pages") / directory.name / self.template
            self.pagetype = PageType.TEMPLATE

        elif not self.external_link is None:
            self.link = self.external_link
            self.pagetype = PageType.EXTERNALLINK
        else:
            raise Exception(f"Neither specified a index.html, template or external_link! For directory {d}")
			

    def _parse_config(self, pathToConfig):
        config = configparser.RawConfigParser()
        config.read(pathToConfig)

        try:
            self.external_link = config["Page-Settings"]["external_link"].strip('\"')
        except Exception as e:
            pass
        try:
            self.template = config["Page-Settings"]["template"]
            self.template_params = dict({})
            for k in config['Page-Settings'].keys():
                if "template-" in k:
                    self.template_params[k[9:]] = config['Page-Settings'][k]
        except Exception as e:
            pass
        try:
            self.timeout = int(config["Page-Settings"]["timeout"])
        except Exception as e:
            self.timeout = self.defaults["timeout"]
        try:
            self.slideshows =  config["Page-Settings"]["slideshows"].split(" ")
            if '' in self.slideshows:
                self.slideshows = []
        except Exception as e:
            self.slideshows = []
        try:
            self.startdate = config["Page-Settings"]["startdate"]
        except Exception as e:
            self.startdate = self.defaults["startdate"]
        try:
            self.enddate = config["Page-Settings"]["enddate"]
        except Exception as e:
            self.enddate = self.defaults["enddate"]
