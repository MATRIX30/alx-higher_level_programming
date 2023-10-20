#!/usr/bin/python3
"""test module for square class"""


import unittest
from models.square import Square

class TestSqaure(unittest.TestCase):
    """Test class for Square class"""

    def setUp(self) -> None:
        """setup method for square"""
        self.s1 = Square()
    