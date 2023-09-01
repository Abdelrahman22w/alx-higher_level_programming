#!/usr/bin/pyhton3
""" Defines a function that returns the int sum of two numbers """
def add_integer(a, b=98):
	"""Return the integer sums a and b 
	Raises: TypeError: if a or b not an integer or float
	"""
	if (not isinstance(a, int) and not isinstance(a, float)):
		raise TypeError("a must be an integer")
	if (not isinstance(b, int) and not isinstance(b, float)):
		raise TypeError("b must be an integer")
	else:
		return(int(a) + int (b))
