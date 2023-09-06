#!/usr/bin/python3
def uppercase(str):
    i = 0
    uperstr = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            uperstr += chr(ord(char) - 32)
        elif ord(char) == 32:
            uperstr += " "
        else:
            uperstr += char
    print("{}".format(uperstr))
