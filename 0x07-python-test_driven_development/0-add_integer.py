#!/usr/bin/python3
"""
a and b
must be integers or floats,
 otherwise raise
"""


def add_integer(a, b=98):
    """function
 that adds
 2 integers"""

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a+b)
