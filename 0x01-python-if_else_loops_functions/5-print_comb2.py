#!/usr/bin/python3
i = 0
def prt(str, n):
    print(str.format(n), end="")
    
while i <= 99:
    if i <= 9:
        prt("0{}, ",i)
    elif i == 99:
        prt("{}\n",i)
    else:
        prt("{}, ",i)
    i += 1
