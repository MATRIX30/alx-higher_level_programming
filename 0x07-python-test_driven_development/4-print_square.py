#!/usr/bin/python3
"""module to print a square of # """


def print_square(size):
    """main square print function

    Args:
            size (int): the size of the square to print

   
    """
    if isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
        size = int(size)
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(size):
            print("#", end="")
        if i != size - 1:
            print("")
        else:
            print(end="\n")
