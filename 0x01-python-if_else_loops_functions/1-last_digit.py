#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = str(number)
last = int(s[-1])
if last < 6 and last > 0:
    print(f"Last digit of {number:d} is {last} and is less than 6 and not 0")
elif last < 0:
    print(f"Last digit of {number:d} is {last} and is less than 6 and not 0")
elif last > 6:
    print(f"Last digit of {number:d} is {last} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {last} and is 0")
