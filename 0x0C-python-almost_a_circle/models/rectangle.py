#!/usr/bin/python3
"""inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """getter 4 width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter is decorated"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getting a value is decorated"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter is decorated"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """method decorated"""
        return self.__x

    @x.setter
    def x(self, x):
        """method has to function as the setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """method decorated"""
        return self.__y

    @x.setter
    def y(self, y):
        """method has to function as the setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area value"""
        return self.__width * self.__height

    def display(self):
        """ public method that prints in stdout """
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for h in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """overriding the __str__ method"""
        id = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h)

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute"""
        arguments = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, arguments[i], args[i])
        else:
            for key, val in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, val)

    def to_dictionary(self):
        """public method that returns the dictionary rep"""

        dictionary = {}
        dictionary["x"] = self.__x
        dictionary["width"] = self.__width
        dictionary["id"] = self.id
        dictionary["height"] = self.__height
        dictionary["y"] = self.__y
        return dictionary
