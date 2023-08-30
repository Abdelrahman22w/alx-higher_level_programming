#!/usr/bin/python3
class Square:
	def __init__(self, size=0):
		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		if size < 0:
			raise ValueError("size must be >= 0")
		self.__size = size
	@property
	def size(self):
		return self.__size
	@size.setter
	def size(self, new_value):
		if not isinstance(new_value, int):
			raise TypeError("size must be an integer")
		if new_value < 0:
			raise ValueError("size must be >= 0")
		self.__size = new_value
	def area(self):
		return (self.__size * self.__size)
