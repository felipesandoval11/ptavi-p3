#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Made by Felipe Sandoval Sibada

from xml.sax import make_parser
import sys
from smallsmilhandler import SmallSMILHandler

if __name__ == "__main__":
    try:
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open(str(sys.argv[1])))
        mytags = sHandler.get_tags()
        for data in mytags:
            for elem, attr in data.items():
                if int(len(data)) == 0:
                    print(elem)
                else:
                    print('\n' + elem, end='')
                for k, v in attr.items():
                    attrval = k + '"' + v + '"'
                    print("\t"+ k + "=" + '"' + v + '"', end=' ')
    except IndexError:
        print("Usage: python3 karaoke.py file.smil.")
