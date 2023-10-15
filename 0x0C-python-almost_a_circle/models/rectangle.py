#!/usr/bin/python3
"""rectangle module"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class implementation

    Args:
            Base (Base): Parent class for rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        NB: use self.attribute = value instead of self.__attribute = value
            so as to use the setters in the constructor hence benefit from
            the various checks used in the setter and not have to repeat code

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        Raises:
                TypeError: if the value entered for width is not an int
                valueError: if the value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        Raises:
                TypeError: if the value entered for y is not an int
                valueError: if the value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
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
        Raises:
                TypeError: if the value entered for height is not an int
                valueError: if the value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        Raises:
                TypeError: if the value entered for x is not an int
                valueError: if the value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """calculates the area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """displays rectangle with using # symbols"""
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print("")