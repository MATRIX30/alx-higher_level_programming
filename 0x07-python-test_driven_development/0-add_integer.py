#!/usr/bin/python3
"""This is a module that add two numbers a and b which
are integers """


def add_integer(a, b=98):
    """This function adds two numbers a and b
    Args:
        a (int/float): an integer or float number
        b (int/float, optional): an integer or float number Defaults to 98.
    Returns:
        int: the sum of a and b

    >>> add_integer(0, 0)
    0
    >>> add_integer(-1, -1)
    -2
    >>> add_integer(-2.5, -3.5)
    -5
    >>> add_integer(0)
    98
    >>> add_integer()
    Traceback (most recent call last):
        ...
    TypeError: add_integer() missing 1 required positional argument: 'a'
    >>> add_integer((3,5), 3)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(2, "alx")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
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
