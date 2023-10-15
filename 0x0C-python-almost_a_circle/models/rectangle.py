#!/usr/bin/python3
"""rectangle module"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class implementation

    Args:
            Base (Base): Parent class for rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width attribute

        Returns:
                type of width: returns the width of the object
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width

        Args:
                value (type of width): value to set width to
        """
        self.__width = value

    @property
    def y(self):
        """getter for y attribute

        Returns:
                type of y: returns the y of the object
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y

        Args:
                value (type of y): value to set y to
        """
        self.__y = value

    @property
    def height(self):
        """getter for height attribute

        Returns:
                type of height: returns the height of the object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height

        Args:
                value (type of height): value to set height to
        """
        self.__height = value
        
    @property
    def x(self):
        """getter for x attribute

        Returns:
                type of x: returns the width of the object
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x

        Args:
                value (type of x): value to set x to
        """
        self.__x = value
        
