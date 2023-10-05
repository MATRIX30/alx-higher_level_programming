#!/usr/bin/python3
""" This module contains a fucntion
    to say your name in the format
    <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """The main function to say your name

    Args:
        first_name (str): users firstname
        last_name (str, optional): users lastname. Defaults to "".

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
