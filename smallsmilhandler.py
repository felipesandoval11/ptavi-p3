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
            attroot = {"width": attr.get('width', "")}
            attroot["height"] = attr.get('height', "")
            attroot["background-color"] = attr.get('background-color', "")
            tagroot = {"root-layout": attroot}
            self.mytags.append(tagroot)
        elif name == "region":
            attregion = {"id": attr.get('id', "")}
            attregion["bottom"] = attr.get('bottom', "")
            attregion["left"] = attr.get('left', "")
            attregion["top"] = attr.get('top', "")
            attregion["right"] = attr.get('right', "")
            tagregion = {"region": attregion}
            self.mytags.append(tagregion)
        elif name == "img":
            attrimg = {"region": attr.get('region', "")}
            attrimg["src"] = attr.get('src', "")
            attrimg["begin"] = attr.get('begin', "")
            attrimg["dur"] = attr.get('dur', "")
            tagimg = {"img": attrimg}
            self.mytags.append(tagimg)
        elif name == "audio":
            attraud = {"src": attr.get('src', "")}
            attraud["begin"] = attr.get('begin', "")
            attraud["dur"] = attr.get('dur', "")
            tagaudio = {"audio": attraud}
            self.mytags.append(tagaudio)
        elif name == "textstream":
            attrtext = {"src": attr.get('src', "")}
            attrtext["region"] = attr.get('region', "")
            tagtext = {"textstream": attrtext}
            self.mytags.append(tagtext)

    def get_tags(self):
        return self.mytags

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))

