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
			self.__class__.__name__, self.id, self.x,
			self.y, self.width
		)
