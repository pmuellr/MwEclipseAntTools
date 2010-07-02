#!/bin/python

import os
import sys
import subprocess

PROGRAM = os.path.basename(sys.argv[0])

#--------------------------------------------------------------------
def log(message):
    print "%s: %s" % (PROGRAM, message)
    
#--------------------------------------------------------------------
def error(message):
    log(message)
    sys.exit(1)

#--------------------------------------------------------------------
args = sys.argv[1:]

if len(args) <= 0: error("Expecting a file or directory name as an argument")

path = args[0]
if os.path.isdir(path):
    pass
elif os.path.isfile(path):
    path = os.path.dirname(path)
else:
    error("not a file or directory: %s" % path)

subprocess.call(["open", path])