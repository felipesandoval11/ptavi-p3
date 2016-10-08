#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Made by Felipe Sandoval Sibada

import sys
import json
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve


class KaraokeLocal:
    def __init__(self, file):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(file))
        self.mytags = sHandler.get_tags()
        self.separate = False

    def __str__(self):
        self.datatags = ""
        self.attrval = ""
        for data in self.mytags:
            for elem, attr in data.items():
                for k, v in attr.items():
                    if self.separate and k == "src" and v != "" and len(v) > 7:
                        if v[0:7] == "http://":
                            urlretrieve(v, v.split("/")[-1])
                            v = v.split("/")[-1]
                    if v != "":         # omitting null values
                        self.attrval += "\t" + k + "=" + '"' + v + '"'
                self.datatags += elem + self.attrval + '\n'
                self.attrval = ""
        return self.datatags

    def to_json(self, name):
        self.name = name + ".json"      # file .json = .smil
        with open(self.name, "w") as outfile:
            json.dump(self.datatags,  outfile)

    def do_local(self):
        self.separate = True
        self.__str__()

    def do_json(self, name="local"):
        if name != "local":
            name = sys.argv[1].split(".")[0]      # file .json = .smil
        self.to_json(name)

if __name__ == "__main__":
    try:
        object = KaraokeLocal(sys.argv[1])
        object.__str__()
        print(object)
        object.do_json(sys.argv[1])
        object.do_local()
        object.do_json()
        print(object)
    except IndexError:
        print("Usage: python3 karaoke.py file.smil.")
