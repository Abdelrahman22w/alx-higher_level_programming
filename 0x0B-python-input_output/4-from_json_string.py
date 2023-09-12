#!/usr/bin/python3
import json
"""Define a function that returns the JSON representation of an object"""


def from_json_string(my_str):
    return json.loads(my_str)
