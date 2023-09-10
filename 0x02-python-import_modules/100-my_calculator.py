#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
args = sys.argv
if len(args) > 4 or len(args) < 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
else:
    if args[1].isdigit():
        n1 = int(args[1])
    if args[3].isdigit():
        n2 = int(args[3])
    if args[2] == '+':
        print("{:d} + {:d} = {:d}".format(n1, n2, add(n1, n2)))
    elif args[2] == '-':
        print("{:d} - {:d} = {:d}".format(n1, n2, sub(n1, n2)))
    elif args[2] == '*':
        print("{:d} * {:d} = {:d}".format(n1, n2, mul(n1, n2)))
    elif args[2] == '/':
        print("{:d} / {:d} = {:d}".format(n1, n2, div(n1, n2)))
