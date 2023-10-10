#!/usr/bin/python3
"""
    Module to return a JSON representation
    of an object
"""

import json as j


def to_json_string(my_obj):
    """
    function to return the JSON representation
    of an object
    Args:
        my_obj(any type): obj to return its JSON representation

    """

    return j.dumps(my_obj)
