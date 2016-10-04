#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Made by Felipe Sandoval Sibada

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


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
        self.mytags = []

    def startElement(self, name, attr):
        if name == "root-layout":
            width = {"width" : attr.get('width', "")}
            width["height"] = attr.get('height', "")
            width["background-color"] = attr.get('background-color', "")
            tagroot = {"root-layout": width}
            self.mytags.append(tagroot)
        elif name == "region":
            self.id = attr.get('id', "")
            self.bottom = attr.get('bottom', "")
            self.left = attr.get('left', "")
            self.top = attr.get('top', "")

        elif name == "img":
            self.region = attr.get('region', "")
            self.src = attr.get('src', "")
            self.begin = attr.get('begin', "")
            self.dur = attr.get('dur', "")

        elif name == "audio":
            self.src = attr.get('src', "")
            self.begin = attr.get('begin', "")
            self.dur = attr.get('dur', "")

        elif name == "textstream":
            self.src = attr.get('src', "")
            self.region = attr.get('region', "")
    
    def get_tags(self):
        return self.mytags

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
    mytags = sHandler.get_tags()
    for data in mytags:
        print(data)
