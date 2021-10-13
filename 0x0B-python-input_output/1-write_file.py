#!/usr/bin/python3
"""not allowed to import any module
"""


def write_file(filename="", text=""):
    """writes a string to a text file
"""

    with open(filename, "w") as file:
        f = file.write(text)
    return f
