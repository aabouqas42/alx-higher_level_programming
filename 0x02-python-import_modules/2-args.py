#!/usr/bin/python3
import sys
args = sys.argv
if len(args) == 1:
    print("0 arguments.")
else:
    i = 1
    print("{:d} arguments:".format(len(args) - 1))
    while i < len(args):
        print("{:d}: {:s}".format(i, sys.argv[i]))
        i += 1
