#!/usr/bin/python3
""" Module for rectangle class with a width and height"""


class Rectangle:
    """This is the main Rectangle Classs
    """
    def __init__(self, width=0, height=0) -> None:
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for width

        Returns:
            int: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width

        Args:
            value (int): width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height attribute getter method

        Returns:
            int: the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height

        Args:
            value (int): the height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
