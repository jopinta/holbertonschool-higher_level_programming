#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    tmp_ls = list(my_list)
    tmp_ls[idx] = element
    return tmp_ls
