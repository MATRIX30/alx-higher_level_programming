#!/usr/bin/python3
"""
    Module to write an object to a text file
    using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    function to write an objec to a text file
    using json representation
            Args:
                    my_obj: objecto to be written
                    filename: file where object will be written to
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
