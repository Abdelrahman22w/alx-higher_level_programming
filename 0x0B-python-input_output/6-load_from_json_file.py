#!/usr/bin/python3
"""Define a function that read object"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file"""

    with open(filename) as f:
        return json.load(f)
