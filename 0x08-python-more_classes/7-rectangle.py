#!/usr/bin/python3
"""
based on 0-rectangle.py
"""


class Rectangle:
    """new class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """method attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ Delete method """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        return self.__height*2 + self.__width*2

    def __str__(self):
        """make object readable"""
        if self.__witdh == 0 or self.__height == 0:
                return ""
        p = str(self.print_symbol) * self.__witdh
        for i in range(self.__height - 1):
                p += "\n"
                p += str(self.print_symbol) * self.__witdh
        return p


    def __repr__(self):
        """ need code that reproduces object"""
        w = self.__width
        return "Rectangle({:d}, {:d})".format(w, self.__height)
