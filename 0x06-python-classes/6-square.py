#!/usr/bin/python3
class Square:
	def __init__(self, size=0, position=(0, 0)):
		self.size = size
		self.position = position
	def __str__(self):
		self.my_print()
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
	@property
	def position(self):
		return self.__position
	@position.setter
	def position(self, new_value):
		if not isinstance(new_value, tuple):
			raise TypeError('position must be a tuple of 2 positive integers')
		if len(new_value) != 2:
			raise TypeError('position must be a tuple of 2 positive integers')
		if len([i for i in new_value if isinstance(i, int) and i >= 0]) != 2:
			raise TypeError('position must be a tuple of 2 positive integers')
		self.__position = new_value

	def area(self):
		return (self.__size * self.__size)
	def pos_print(self):
		position = ""
		if self.size == 0:
			return "/n"
		for j in range(self.position[1]):
			position += "/n"
		for j in range(self.size):
			for i in range(self.position[0]):
				position += " "
			for k in range(self.size):
				position += "/n"
		return position
	def my_print(self):
		print(self.pos_print(), end='')
