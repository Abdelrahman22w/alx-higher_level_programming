#!/usr/bin/python3
""" Defines a printing square function """
def print_square(size):
	"""
	Args:
		size: must be an integer or if it's a float it nust be > 0
	raises:
		TypeError: if size is not int 
		TypeError: if size is float and less than 0
		ValueError: if size less than 0
	"""
	if (not isinstance(size, int)):
		raise TypeError("size must be an integer")
	
	elif (size < 0):
		raise ValueError("size must be >= 0")
	elif (not isinstance(size, float) and size < 0):
		raise TypeError("size must be an integer")
	for i in range(size):
		for j in range(size):
			print("#", end="")
		print("")
