#!/usr/bin/python3
def text_indentation(text):
	i = 0
	while i < len(text):
		print(text[i], end="")
		if text[i] == '.' or text[i] == '?' or text[i] == ':':
			print("\n\n", end="")
		i += 1
