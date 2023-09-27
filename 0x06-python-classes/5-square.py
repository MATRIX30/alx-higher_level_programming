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

    def area(self):
        """ Area method that returns the area of the
            current square

            Returns:
                    float: area of the current square
        """
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print(end="\n")
        else:
            i = 0
            j = 0
            while (i < self.__size):
                while (j < self.__size):
                    print("#", end="")
                    j += 1
                print(end="\n")
                j = 0
                i += 1
