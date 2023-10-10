#!/usr/bin/python3
"""Module for Geometry class"""


class BaseGeometry:
    """This is the BaseGeometry class"""

    def area(self):
        """area instance method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validate value

        Args:
            name (str): _description_
            value (int): _description_
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
