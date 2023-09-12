#!/usr/bin/python3

"""open and write a text from a file"""

def write_file(filename="", text=""):
    """
    print the text in the file
    Return: the number of characters
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
