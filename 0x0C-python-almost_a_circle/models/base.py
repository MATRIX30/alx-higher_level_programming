#!/usr/bin/python3
"""Base class module"""


class Base():
    """Base class"""

    __nb_objects = 0
    def __init__(self, id = None):
        """Base class constructor
        Args:
            id (int, optional): class id. Defaults to None.
        """
        if not id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
