#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a JSON file."""
import sys
import json

if __name__ == "__main__":
    try:
        with open("add_item.json", "r") as file:
            items = json.load(file)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])

    with open("add_item.json", "w") as file:
        json.dump(items, file)
