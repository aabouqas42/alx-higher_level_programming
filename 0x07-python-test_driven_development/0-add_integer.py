#!/usr/bin/python3
def	add_integer(a, b=98):
	if not isinstance(a, int):
		print("a must be an integer")
		return
	if not isinstance(b, int):
		print("b must be an integer")
		return
	return (a + b)