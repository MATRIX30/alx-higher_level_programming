#!/usr/bin/python3
"""
    Module to return an object (python data structure)
     represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    function to return object stored in json string
            Args:
                    my_str(str): json string object
    """
    return json.loads(my_str)
