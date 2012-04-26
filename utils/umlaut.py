#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

REPLACE = {"ä": '\\"a',
           "ö": '\\"o',
           "ü": '\\"u',
           "Ä": '\\"A',
           "Ö": '\\"O',
           "Ü": '\\"U'}

with open(sys.argv[1], "r+") as f:
    content = f.read()
    for orig, repl in REPLACE.iteritems():
        content = content.replace(orig, repl)
    f.seek(0)
    f.write(content)
