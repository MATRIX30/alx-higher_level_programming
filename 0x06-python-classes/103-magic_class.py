
import math


class MagicClass:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self._radius = radius

    def area(self):
        return self._radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self._radius
