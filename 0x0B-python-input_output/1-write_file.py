#!/usr/bin/python3
"""module to write to a file"""


def write_file(filename="", text=""):
    """function to write <text> into file <filename>"""
    with open(filename, "w", encoding='utf-8') as f:
        write_count = f.write(text)
    return write_count
