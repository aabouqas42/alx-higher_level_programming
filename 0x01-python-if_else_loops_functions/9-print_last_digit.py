#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        n = number *- 1
        print(n % 10)
    else:
        print(number % 10
