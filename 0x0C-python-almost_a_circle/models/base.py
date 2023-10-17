#!/usr/bin/python3
"""Base class module"""


import json
import csv
import os


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
        res = []
        if list_objs is None:
            with open("Base.json", "w") as f:
                json.dump(res, f)
        else:
            for obj in list_objs:
                res.append(obj.to_dictionary())

        data = cls.to_json_string(res)
        with open("{:s}.json".format(cls.__name__), "w") as f:
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
            dummy = cls(1, 1)

        if cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file"""
        file_name = "{:s}.json".format(cls.__name__)
        with open(file_name, "r") as f:
            json_list = f.read()

        res = []
        if not os.path.exists(file_name):
            pass
        lst_obj = cls.from_json_string(json_list)

        for obj in lst_obj:
            res.append(cls.create(**obj))
        return res

    @staticmethod
    def drawi(list_rectangles, list_squares):
        """sd"""
        pass
