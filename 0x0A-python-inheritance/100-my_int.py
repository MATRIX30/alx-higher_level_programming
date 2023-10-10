#!/usr/bin/python3
"""Module of my class that inherits from int """


class MyInt(int):
    """stubborn my class that inherits from int"""

    def __ne__(self, other) -> bool:
        """override not equal sign"""
        return self.real == other

    def __eq__(self, other) -> bool:
        """override equality sign"""
        return self.real != other
