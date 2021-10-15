#!/usr/bin/python3
"""inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """nstantiation with width and height
"""

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method must be implemented"""
        return self.__width * self.__height

    def __str__(self):
        """print, the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
