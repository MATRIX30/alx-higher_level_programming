#!/usr/bin/python3
"""Base class module"""


class Base:
    """Base class"""

    __nb_objects = 0
    import json

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
        import json

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
        import json

        if list_objs is None:
            with open("Base.json", "w") as f:
                f.write("[]")

        else:
            with open("{:s}.json".format(cls.__name__), "w") as f:
                res = []
                for obj in list_objs:
                    res.append(obj.to_dictionary())
                data = cls.to_json_string(res)
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
            import json

            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
             dictionary(dic): double pointer to a dictionary
        """

        dummy = cls.__new__(cls)

        dummy.update(**dictionary)
        return dummy
