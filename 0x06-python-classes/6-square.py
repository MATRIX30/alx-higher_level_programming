#!/usr/bin/python3
"""This is the square class """


class Square:
    """This is an empty Square class
    """
    def __init__(self, size=0, position=(0,0)):
        """This is the initilization function
        it has a private size member
        Args:
            size(int): size of square
            position(tuple): this is a tuple of the positon of the square
         """
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        
	""" Defining getters and setters"""
    @property
    def size(self):
        """ This is the getter for size field
            Returns:
                    int: size of the square to be returned
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ This is the setter method for size
            Args:
                Value : value that would be set to the size of the square
        """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

	@property
	def position(self):
		""" getter for position property
			Returns:
				position(tuple): position tuple is returned
  		"""
		return (self.__position)

	@position.setter
 	def position(self, value):
		"""setter for position"""
		if (isinstance(value, tuple) and len(value) == 2) \
      	and (isinstance(value[0], int) and isinstance(value[1], int)) \
		and (value[0] >= 0 and value[1] >= 0):
				self.__position = value
		else:
			raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Area method that returns the area of the
            current square

            Returns:
                    float: area of the current square
        """
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print(end="\n")
        else:
            i = 0
            j = 0
            while (i < self.__size):
                while (j < self.__size):
                    print("#", end="")
                    j += 1
                print(end="\n")
                j = 0
                i += 1
