#!/usr/bin/python3

"""open and append a text from a file"""

def append_write(filename="", text=""):
    """
    print the text in the file
    Return: the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
