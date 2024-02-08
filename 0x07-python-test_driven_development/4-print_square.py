#!/usr/bin/python3

def	print_square(size):
	row = 0
	while row < size:
		column = 0
		while column < size:
			print("#", end="")
			column += 1
		row += 1
		print("\n", end="")