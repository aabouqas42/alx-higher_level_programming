#!/usr/bin/python3

def	matrix_divided(matrix, div):
	row = 0
	while row < len(matrix):
		column = 0
		while column < len(matrix[row]):
			matrix[row][column] /= div
			column += 1
		row += 1
