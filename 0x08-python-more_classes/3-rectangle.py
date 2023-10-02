#!/usr/bin/python3
""" Module for rectangle class with a width and height"""


class Rectangle:
    """This is the main Rectangle Classs"""

    def __init__(self, width=0, height=0) -> None:
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

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

    def area(self) -> int:
        """method to calculate area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self) -> int:
        """method to return perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self) -> str:
        str_rep = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                str_rep += "#"
                # print("#", end="")
            # print("\n")
            if i < self.__height - 1:
                str_rep += "\n"
        return str_rep
