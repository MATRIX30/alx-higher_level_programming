#!/usr/bin/python3
"""Module of my class that inherits from int """


class MyInt(int):
    def __ne__(self, other) -> bool:
        if self != other:
            return False
        return True

    def __eq__(self, other) -> bool:
        if self == other:
            return False
        return True
