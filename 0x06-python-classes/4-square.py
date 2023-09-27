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

    @property
    def size(self):
        """ This is the getter for size field
            Returns:
                    int: size of the square to be returned
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ This is the setter method for size
            Args:
                Value : value that would be set to the size of the square
        """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
