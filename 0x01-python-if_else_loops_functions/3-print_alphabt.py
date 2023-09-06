#!/usr/bin/python3
i = ord('a')
while i <= ord('z'):
    if i == 101 or i == 113:
        i += 1
    else:
        print("{}".format(chr(i)), end="")
        i += 1
