#!/usr/bin/python3
"""Defines a text-indentation function."""
   
"""Print text with two new lines after each '.', '?', and ':'.
	Args:
		text (string): The text to be printed
	Raises:
		TypeError: If text is not a string
"""
def text_indentation(text):
	if (not isinstance(text, str)):
		raise TypeError("text must be a string")
	
	count = 0
	while count < len(text) and text[count] == ' ':
		count += 1
	while count < len(text):
		print(text[count], end="")
		if (text[count] == "/n" or text[count] in ".?:"):
			if (text[count] in ".?:"):
				print("/n")
			count += 1
			while count < len(text) and text[count] == " ":
				count += 1
			continue
		count += 1
