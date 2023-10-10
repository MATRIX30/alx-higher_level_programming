#!/usr/bin/python3
"""module to search and update or add a newline"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after
    each line containing a specific string.

    Args:
        filename: The name of the file to append to.
        search_string: The string to search for in the file.
        new_string: The string to insert after each line containing
        the search string.

    Returns:
        None.
    """
    with open(filename, "r+") as f:
        # lines = f.readlines()
        res = []
        for line in f:
            res.append(line)
            if search_string in line:
                res.append(new_string)
        f.seek(0)
        f.writelines(res)
