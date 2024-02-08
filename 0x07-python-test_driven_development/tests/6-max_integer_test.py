#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	def test_max(self):
		ints = [30, 22 , 100, 11]
		max_value = max_integer(ints)
		self.assertEqual(max_value, 100, "Expected 100 found {}".format(max_value))

if __name__ == '__main__':
	unittest.main()