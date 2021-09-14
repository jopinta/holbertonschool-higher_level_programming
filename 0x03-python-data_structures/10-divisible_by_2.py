#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    tmp_ls = []
    for i in my_list:
        if (i % 2 == 0):
            tmp_ls.append(True)
        else:
            tmp_ls.append(False)
    return (tmp_ls)
