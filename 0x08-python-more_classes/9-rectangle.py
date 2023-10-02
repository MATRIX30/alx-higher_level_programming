#!/usr/bin/python3
""" Module for rectangle class with a width and height"""


class Rectangle:
    """This is the main Rectangle Classs"""

    # public class attributes
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for width

        Returns:
            int: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width

        Args:
            value (int): width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height attribute getter method

        Returns:
            int: the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height

        Args:
            value (int): the height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """method to calculate area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self) -> int:
        """method to return perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self) -> str:
        str_rep = ""
        if self.__height == 0 or self.__width == 0:
            return str_rep
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                # str_rep = str_rep.join(self.print_symbol)
                str_rep += str(self.print_symbol)
                # print("#", end="")

            if i < self.__height - 1:
                # print("\n")
                str_rep += "\n"
                # str_rep = str_rep.join("\n")
        return str_rep

    def __repr__(self):
        """this method must take a string that contains the representatiosn
            of the attributes of the objecct
        Returns:
            str: representation of the object
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Method to delete an object of the rectangle class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method def bigger_or_equal(rect_1, rect_2): that returns
           the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): instance of Rectangle
            rect_2 (Rectangle): instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """method to convert rectangle to square

        Args:
            size (int, optional): size of the square. Defaults to 0.

        Returns:
            Rectangle: a square representation of a rectangle
        """
        return cls(size, size)
