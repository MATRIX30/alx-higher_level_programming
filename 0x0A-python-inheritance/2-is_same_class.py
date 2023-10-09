#!/usr/bin/python3
"""module to verify if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """function to verify if obj is an instance a_class

    Args:
            obj (_type_): object to test its class
            a_class (class): class to test
    """
    if isinstance(obj, a_class):
        if not issubclass(obj, a_class):
            return True
    return False
