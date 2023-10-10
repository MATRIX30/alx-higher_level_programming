#!/usr/bin/python3
"""module for a function that reads from a file in utf-8 encoding"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
      filename: The path to the text file to read.
    """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
