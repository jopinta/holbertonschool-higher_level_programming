#!/usr/bin/python3
"""must use the with statement
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file
"""
    with open(filename) as new_f:
        return json.load(new_f)
