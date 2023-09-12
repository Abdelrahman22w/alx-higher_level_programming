#!/usr/bin/python3

"""open and read a text from a file"""

def read_file(filename=""):
    """print the text in the file"""
    with open(filename, encoding = "UTF8") as f:
        print(f.read(), end = "")
