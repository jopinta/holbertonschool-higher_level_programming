#!/usr/bin/python3
""" print a square using #
size must be an integer
"""


def print_square(size):
    """prints a square with the character #."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print("")
