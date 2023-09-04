#!/usr/bin/python3
"""A class defined Rectangle"""
class Rectangle:
	"""defined class"""
	def __init__(self, width=0, height=0):
		"""initializing the rectangle components
		Args:
			width: the rectangle width
			height: the rectangle height
		Raises:
			TypeError: if size is not int
			ValueError: if size is negative
		"""
		
		self.width = width
		self.height = height

	@property
	def width(self):
		"""make width attribute"""
		return self.__width
	
	@width.setter
	def width(self, value):
		"""set width attribute"""
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value
		
	@property
	def height(self):
		"""make height attribute"""
		return self.__height

	@height.setter
	def height(self, value):
		"""set height attribute"""
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value

	def area(self):
		"""Return the area of the rectangle"""
		return (self.__width * self.__height)
	def perimeter(self):
		"""Return the perimeter of the rectangle"""
		return ((self.__width * 2) + (self.__height * 2))
		
	