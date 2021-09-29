#!/usr/bin/python3
"""class Square to deine a square"""


class Square:
    """defining a class squeare"""
    __size = 

    def __init__(self, size=0):
        """initialize with attributte size"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("Size must be >= 0")
        else:
            raise TypeError("size must be an integer")
