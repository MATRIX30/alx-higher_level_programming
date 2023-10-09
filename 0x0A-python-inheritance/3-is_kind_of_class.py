#!/usr/bin/python3
"""module to verify if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """function to verify if  object is an instance of, or if the object
    is an instance of a class that
    inherited from, the specified class ; otherwise False

    Args:
            obj (_type_): object to test its class
            a_class (class): class to test
    """

    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
