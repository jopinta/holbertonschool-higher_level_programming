#!/usr/bin/python3
"""yall assume that all the elements of the list will be of type int
"""


class MyList(list):
    """
class MyList that inherits from list"""


    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        new_list = self.copy()
        new_list.sort()
        print(new_list)
