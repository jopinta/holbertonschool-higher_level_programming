#!/usr/bin/python3
"""  not allowed to import any module"""


def inherits_from(obj, a_class):
    """ if the object is an instance of a class that inherited (directly or indirectly) from the specified class"""

    if type(obj) is a_class and type(obj) is not isinstance(obj, a_class):
            return False
    else:
        return isinstance(obj, a_class)
