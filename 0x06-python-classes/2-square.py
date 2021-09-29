#!/usr/bin/python3
"""class Square"""


class Square:
    """defining a class squeare"""
    __size = None

    def __init__(self, size=0):
        """init with attributte size"""
        if type(size) is int:
            if size >= 0:
                 self.__size = size
            else:
                 raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
