#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    tmp = []
    for i in my_list:
        if i % 2 == 0:
            tmp.append(True)
        else:
            tmp.append(False)
            return tmp
