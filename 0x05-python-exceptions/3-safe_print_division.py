#!/usr/bin/python3
def safe_print_division(a, b):
	try:
		res = a / b
	except (TypeError, ZeroDivisionError):
		div = None
	finally:
		print("Inside result: {}".format(res))
	return res
