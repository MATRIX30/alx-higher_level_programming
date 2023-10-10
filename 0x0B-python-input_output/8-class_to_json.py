#!/usr/bin/python3
"""function that returns the dictionary description
   with simple data structure (list, dictionary, string,
   integer and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """method to return json serialization of and obj"""
    return vars(obj)
