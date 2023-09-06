#!/usr/bin/python3
def uppercase(str):
    i = 0
    uperstr = ""
    while str[i]:
        char = str[i]
        if ord(char) >= 97 and ord(char) <= 122 :
            uperstr += chr(ord(char) - 32)
        i += 1
    print("{}".format(uperstr))
