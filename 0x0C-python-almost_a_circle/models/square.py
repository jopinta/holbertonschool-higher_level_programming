#!/usr/bin/python3
"""a Square is a special Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """same attributes and same methods."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """overloading method """
        w = self.__width
        x = self.__x
        y = self.__y
        id = self.id
        return "[Square] ({}) {}/{} - {}".format(id, x, y, w)

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute"""
        names = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, names[i], args[i])
        else:
            for key, val in kwargs.items():
                if key in names:
                    setattr(self, key, val)

    def to_dictionary(self):
        """public method that returns the dictionary rep"""

        dictionary = {}
        dictionary["id"] = self.id
        dictionary["x"] = self.__x
        dictionary["size"] = self.__height
        dictionary["y"] = self.__y
        return dictionary
