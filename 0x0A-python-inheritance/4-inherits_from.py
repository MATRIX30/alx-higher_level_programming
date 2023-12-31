#!/usr/bin/python3
"""module to verify if object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """function to verify if object is an instance of a class that inherited
        (directly or indirectly) from the specified class;
        otherwise False


    Args:
            obj (_type_): object to test its class
            a_class (class): class to test
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
