#!/usr/bin/python3
import json
"""Define a function that read object"""


def load_from_json_file(filename):
    with open(filename, "w") as f:
        json.load(f)
