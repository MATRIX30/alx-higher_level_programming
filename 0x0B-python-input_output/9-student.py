#!/usr/bin/python3
"""Module for a student class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """init method/ constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method that retrieves a dictionary
        representation of a Student
        """
        return vars(self)
