
import math
"""This is a magic class that is the exact representaion as the
    bytecode provided by ALx for advanced task 103
 """


class MagicClass:
    """This is the definition of the class MagicClass
    from scracth
    """
    def __init__(self, radius):
        """main init function of the class

        Args:
            radius (float): floating point radius of the file

        Raises:
            TypeError: _description_
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self._radius = radius

    def area(self):
        """area function calculates the area of  this oblect

        Returns:
            float: the area of the object
        """
        return self._radius ** 2 * math.pi

    def circumference(self):
        """Circumference calculation method

        Returns:
            float: the Method to calculate
               circumference of the object
        """
        return 2 * math.pi * self._radius
