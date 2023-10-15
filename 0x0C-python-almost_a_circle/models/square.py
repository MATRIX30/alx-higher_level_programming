#!/usr/bin/python3
"""module for square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class

    Args:
        Rectangle (Rectangle): Rectangle base class from which square
                            inherites
    """

    def __init__(self, size, x=0, y=0, id=None):
        """constructor for square

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """print method

        Returns:
            str: string representation of square class
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """method to assign new values to attributes"""
        if bool(args):
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width, self.height = args[1], args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width, self.height = args[1], args[1]
                self.x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.width, self.height = args[1], args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            if "id" in kwargs.keys():
                self.id = kwargs["id"]
            if "size" in kwargs.keys():
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs.keys():
                self.x = kwargs["x"]
            if "y" in kwargs.keys():
                self.y = kwargs["y"]
