#!/usr/bin/python3
"""must use the with statement
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON
"""
    with open(filename, "w") as new_f:
        json.dump(my_obj, new_f)
