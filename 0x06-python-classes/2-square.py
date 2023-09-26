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
        try:
            if (not isinstance(size, int)):
                raise TypeError
            elif (size < 0):
                raise ValueError
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
