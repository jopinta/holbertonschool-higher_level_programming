#!/usr/bin/python3
"""not allowed to import any module
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:
"""

    with open(filename) as f:
        print(f.read(), end='')
