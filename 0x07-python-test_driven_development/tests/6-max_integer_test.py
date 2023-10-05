#!/usr/bin/python3
"""Module to find max_integer in a list"""


import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """This the test class for max integer"""

    def test_max_integer_empty_list(self):
        """testing for empty list"""
        self.assertIsNone(max_integer([]))

    def test_max_integer_string_list(self):
        """testing list with str item"""
        with self.assertRaises(TypeError):
            max_integer(["alx", 2, 4, 5])

    def test_max_integer_string(self):
        """testing list with str item"""
        with self.assertRaises(AssertionError):
            max_integer("alx")

    def test_max_integer_increasing_order_list(self):
        """list in increasing order"""
        self.assertEqual(max_integer([-2, -1, 1, 2, 4]), 4)

    def test_max_integer_decreasing_order_list(self):
        """list in increasing order"""
        self.assertEqual(max_integer([8, 3, -4, -7, -10]), 8)

    def test_max_integer_all_identical_list(self):
        """list in increasing order"""
        self.assertEqual(max_integer([-2, -2, -2, -2]), -2)

    def test_max_integer_at_middle_list(self):
        """list in increasing order"""
        self.assertEqual(max_integer([-2, -1, 1, 0, -4]), 1)

    def test_max_integer_single_item_list(self):
        """list in increasing order"""
        self.assertEqual(max_integer([-4]), -4)
