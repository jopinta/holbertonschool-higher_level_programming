#!/usr/bin/python3
"""not allowed to import any module
"""


def append_write(filename="", text=""):
    """append a string at the end of text file
"""

    with open(filename, "a") as file:
        f = file.write(text)
    return f
