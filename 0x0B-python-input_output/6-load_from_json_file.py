#!/usr/bin/python3
"""Define a function that read object"""
import json


def load_from_json_file(filename):
    with open(filename, "w") as f:
        json.load(f)
