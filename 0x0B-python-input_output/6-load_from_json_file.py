#!/usr/bin/python3
"""
    Module to write an object to a text file
    using JSON representation
"""


import json


def load_from_json_file(my_obj, filename):
    """
    function to load an objec from a text file
    using json representation
            Args:
                    my_obj: objecto to be created or loaded
                    filename: file where object is loaded from
    """
    with open(filename, "r") as f:
        my_obj = json.load(f)
