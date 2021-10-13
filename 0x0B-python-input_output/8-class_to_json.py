#!/usr/bin/python3
"""not allowed to import any module"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure for JSON se
rialization of an object:
"""

    return obj.__dict__
