#!/usr/bin/python3
""" inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        Rectangle.integer_validator(self, "size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """method must be implemented"""
        return self.__size * self.__size
