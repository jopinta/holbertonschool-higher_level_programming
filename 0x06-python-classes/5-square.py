#!/usr/bin/python3
"""class Square to deine a square"""


class Square:
    """defining a class squeare"""

    def __init__(self, size=0):
        """init with attributte size"""
        self.__size = size

    @property
    def size(self):
        """property to it"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter to it"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Public instance method hat returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """public instance method to print square"""
        if self.__size > 0:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
