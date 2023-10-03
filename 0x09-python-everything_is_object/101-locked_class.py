#!/usr/bin/python3
"""module for locked class"""


class LockedClass:
    """this class prevents the creation of
       dynammic attributes except the attribute
       name is 'first_name'
    """
    __slots__ = ['first_name']
