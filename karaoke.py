#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Made by Felipe Sandoval Sibada

import sys
import json
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve


if __name__ == "__main__":
    try:
        attrval = ""
        datatags = ""
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(str(sys.argv[1])))
        mytags = sHandler.get_tags()
        for data in mytags:
            for elem, attr in data.items():
                for k, v in attr.items():
                    if k == "src" and v != "" and len(v) > 7:  # just in case
                        if v[0:7] == "http://":
                            urlretrieve(v, v.split("/")[-1])
                            v = v.split("/")[-1]
                    if v != "":         # omitting null values
                        attrval += "\t" + k + "=" + '"' + v + '"'
                print(elem + attrval)
                datatags += elem + attrval
                attrval = " "
        filename = sys.argv[1].split(".")[0] + ".json"  # file .json = .smil
        with open(filename, "w") as outfile:
            json.dump(datatags,  outfile)
    except IndexError:
        print("Usage: python3 karaoke.py file.smil.")
