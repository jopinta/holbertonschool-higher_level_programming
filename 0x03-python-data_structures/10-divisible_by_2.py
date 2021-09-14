#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    tmp = []
    for i in my_list:
        if i % 2 == 0:
            tmp.append(False)
        else:
            tmp.append(True)
            return tmp
