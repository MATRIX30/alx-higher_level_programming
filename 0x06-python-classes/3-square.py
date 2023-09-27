#!/usr/bin/python3
"""This is the square class """


class Square:
    """This is an empty Square class
    """
    def __init__(self, size=0):
        """This is the initilization function
        it has a private size member
        Args:
            size: size of square
         """
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Area method that returns the area of the
            current square

        Returns:
                float: area of the current square
        """
        return (self.__size * self.__size)
