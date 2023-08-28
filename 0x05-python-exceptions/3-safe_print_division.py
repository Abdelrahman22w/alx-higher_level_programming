#!/usr/bin/python3
def safe_print_division(a, b):
	try:
		res = a / b
		print("Inside result:{}".format(res))
	except(TypeError, ZeroDivisionError):
		div = None
		print("Inside result:{}".format(res))
	finally:
		return res
