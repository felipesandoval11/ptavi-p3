#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Made by Felipe Sandoval Sibada

from xml.sax import make_parser
import sys
from smallsmilhandler import SmallSMILHandler


if __name__ == "__main__":
    try:
        attrval = " "
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(str(sys.argv[1])))
        mytags = sHandler.get_tags()
        for data in mytags:
            for elem, attr in data.items():
                for k, v in attr.items():
                    if v != "":         # omitting null values
                        attrval += "\t" + k + "=" + '"' + v + '"'
                print(elem + attrval)
                attrval = " "
    except IndexError:
        print("Usage: python3 karaoke.py file.smil.")
