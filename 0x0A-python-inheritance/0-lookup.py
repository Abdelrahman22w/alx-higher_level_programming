#!/usr/bin/python3
"""Define a method that return a list"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
