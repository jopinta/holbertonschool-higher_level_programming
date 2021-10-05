#!/usr/bin/python3
"""
based on 0-rectangle.py
"""


class Rectangle:
    """new class"""

    def __init__(self, width=0, height=0):
        """method attributes"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """decorator, property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set hieght"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """decorator property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """to calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """ to calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
