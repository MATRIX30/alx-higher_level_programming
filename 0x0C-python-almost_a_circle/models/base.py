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
            dummy = cls.__new__(cls, 12, 15)

        if cls.__name__ == "Square":
            dummy = cls.__new__(cls, 5)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file"""
        """file_name = "{:s}.json".format(cls.__name__)
        with open(file_name, "r") as f:
            json_list = f.read()

        res = []
        lst_obj = cls.from_json_string(json_list)
        print(type(lst_obj))
        for obj in lst_obj:
            res.append(cls.create(**obj))
        """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    @staticmethod
    def draw(list_rectangles, list_squares):
        pass

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method that saves a CSV file"""
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ["id", "width", "height", "x", "y"]
        else:
            list_dic = ["0", "0", "0", "0"]
            list_keys = ["id", "size", "x", "y"]

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, "w") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """Method that loads a CSV file"""
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ["id", "width", "height", "x", "y"]
        else:
            list_keys = ["id", "size", "x", "y"]

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins
