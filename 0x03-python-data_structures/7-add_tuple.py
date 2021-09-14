#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tmp = [0, 0]
    a = list(tuple_a)
    b = list(tuple_b)
    for i in range(0, 2):
        if (i >= len(a)):
            a.append(0)
        if (i >= len(b)):
            b.append(0)
            tmp[i] = a[i] + b[i]

    return tuple(tmp)
