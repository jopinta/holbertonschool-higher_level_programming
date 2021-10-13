#!/usr/bin/python3
"""not allowed to import any module
"""


class Student:
    """class that defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representationof the class"""
        return self.__dict__
