#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} <a> <operator> <b>".format(args[0]))
        exit(1)
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
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    exit(0)
    
        
