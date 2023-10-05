#!/usr/bin/python3
"""This is a module that contains a function 
that add two numbers a  and b which
are integers  while handling some exceptions
especially edge cases that might arise"""

def add_integer(a, b=98):
    """This function adds two integer of float numbers a and b
    Args:
        a (int/float): an integer or float number
        b (int/float, optional): an integer or float number Defaults to 98.
    Returns:
        int: the sum of a and b
        

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
