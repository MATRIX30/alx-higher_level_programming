#!/usr/bin/python3
"""Module for a student class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """init method/ constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that retrieves a dictionary
        representation of a Student
        """
        filter_res = {}
        if attrs is None:
            return vars(self)
        for key in attrs:
            if key in vars(self):
                filter_res[key] = vars(self)[key]
        return filter_res

    def reload_from_json(self, json):
        """method to replace all attributes of student instance"""
        for key in json.keys():
            setattr(self, key, json[key])
