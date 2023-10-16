#!/usr/bin/python3
"""Base class module"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor
        Args:
            id (int, optional): class id. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries:list):
        """returns json list representation of list_dictionaries
    
        Args:
            list_dictionaries (list): list of dictionaries
        """
        import json
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
        