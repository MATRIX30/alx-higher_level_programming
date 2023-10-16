#!/usr/bin/python3
"""test module for square class"""


import unittest


class TestSqaure(unittest.TestCase):
    """Test class for Square class"""

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_new_square(self):
        """ Test new square """
        new = Square(3)
        self.assertEqual(new.size, 3)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)
