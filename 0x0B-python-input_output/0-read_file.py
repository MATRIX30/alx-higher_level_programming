#!/usr/bin/python3
"""module for a function that reads from a file in utf-8 encoding"""


def read_file(filename=""):
    """method to read from file

    Args:
            filename (str, optional): filename to read from. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
