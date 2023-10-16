#!/usr/bin/python3
"""Base class module"""


import json


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
    def to_json_string(list_dictionaries: list):
        """returns json list representation of list_dictionaries
        Args:
            list_dictionaries (list): list of dictionaries
        """

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string representation of list_objs
           to a file

        Args:
            list_objs (_type_): list of instances who inherites of Base
             eg list of Rectangle or list of Square instances
        """

        if list_objs is None:
            with open("Base.json", "w") as f:
                json.dump([], f)

        else:
            res = []
            for obj in list_objs:
                res.append(obj.to_dictionary())
            data = cls.to_json_string(res)
            with open("{}.json".format(cls.__name__), "w") as f:
                f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """returns a list of json string representation
           json_string
        Args:
            json_string (json string): _description_

        Returns:
            list: list of objects represented by dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
             dictionary(dic): double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls.__new__(cls, 12, 15)

        if cls.__name__ == "Square":
            dummy = cls.__new__(cls, 5)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns alist of instances from a file"""

    @staticmethod
    def draw(list_rectangles, list_squares):
        pass
