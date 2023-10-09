#!/usr/bin/python3
"""module to return list of available attributes
and methods of an object
"""


def lookup(obj):
    """function to return attributes and methods of an object obj

    Args:
            obj (any type): object whose attributes and methods we wish
                                            to return
    """
    return dir(obj)
