#!/usr/bin/python3
import sys
args = sys.argv
if len(args) == 1:
    print("0 arguments.")
else:
    i = 1
    print("{} arguments:".format(len(args) - 1))
    while i < len(args):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
