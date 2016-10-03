#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Made by Felipe Sandoval Sibada

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

mydata = {}
mylistdata = []

class SmallSMILHandler(ContentHandler):
    def __init__(self):
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.begin = ""
        self.dur = ""
        self.region = ""

    def startElement(self, name, attr):
        if name == "root-layout":
            self.width = attr.get('width', "")
            self.height = attr.get('height', "")
            self.backgroundcolor = attr.get('background-color', "")
        elif name == "region":
            self.id = attr.get('id', "")
            self.bottom = attr.get('bottom', "")
            self.left = attr.get('left', "")
            self.top = attr.get('top', "")
            mydata.update({name:[self.id, self.bottom,
            self.left, self.bottom]})
            mylistdata.append(mydata)
        elif name == "img":
            self.region = attr.get('region', "")
            self.src = attr.get('src', "")
            self.begin = attr.get('begin', "")
            self.dur = attr.get('dur', "")
            mydata.update({name:[self.src, self.region,
            self.begin, self.dur]})
            mylistdata.append(mydata)
        elif name == "audio":
            self.src = attr.get('src', "")
            self.begin = attr.get('begin', "")
            self.dur = attr.get('dur', "")
            mydata.update({name:[self.src, self.begin,
            self.dur]})
            mylistdata.append(mydata)
        elif name == "textstream":
            self.src = attr.get('src', "")
            self.region = attr.get('region', "")
            mydata.update({name:[self.src, self.region]})
            mylistdata.append(mydata)

    def get_tags(self):
        return self.mydata

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))