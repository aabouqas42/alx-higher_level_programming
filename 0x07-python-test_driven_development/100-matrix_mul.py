#!/usr/bin/python3

def matrix_mul(m_a, m_b):
	m_c = [[]];
	a_hight = len(m_a)
	a_width = len(m_a[0])
	b_hight = len(m_b)
	b_width = len(m_b[0])
	if a_width == b_hight:
		i = 0
		while i < a_width:
			j = 0
			while j < b_hight:
				m_c[i][j] = sum(m_a[i][j] * m_b[i][j])
			j += 1
		i += 1
		return m_c
	else:
		print("not valid")
		return None


mtrx1 = [
	[10, 98, 54, 99],
	[1, 9, 5, 9],
	[1, 9, 5, 9],
	[100, 980, 50, 90],
]

mtrx2 = [
	[10, 98, 54, 99],
	[1, 9, 5, 9],
	[1, 9, 5, 9],
	[100, 980, 50, 990],
]

matrix_mul(mtrx1, mtrx2)
