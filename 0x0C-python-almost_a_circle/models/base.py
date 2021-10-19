#!/usr/bin/python3
"""the first class"""
import json


class Base():
    """private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
#JSON is one of the standard formats for sharing data representation.
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string rep"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        """ string rep a list of dictionaries"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)
