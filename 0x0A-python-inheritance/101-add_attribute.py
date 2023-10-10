#!/usr/bin/python3
"""Module to add an attribute to an object"""


def add_attribute(obj, attrib_name, attrib_value):
    """method to add an attribute

    Args:
            obj (_type_): object whose attribute is to be added
            attrib_name (_type_): the attribute name
            attrib_value (_type_): attribute value
    Raises:
            TypeError: if the attribute cannot be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attrib_name, attrib_value)
