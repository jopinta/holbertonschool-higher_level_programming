#!/usr/bin/python3
"""not allowed to import any module"""


def is_same_class(obj, a_class):
    """recieves an object and a class to compare
    """
    if isinstance(obj, a_class):
        return True
    return False
