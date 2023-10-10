#!/usr/bin/python3
"""
    Module to append to a file
    and return number of characters added
"""


def append_write(filename="", text=""):
    """
    function to append to a file and
    return the number of charcaters added

    Args:
                filename(str): path to file represented as string
                text(str): text to be appended to file

    """
    with open(filename, "a", encoding="utf-8") as f:
        number_of_writes = f.write(text)
    return number_of_writes
