#!/usr/bin/python3


def ptint_last_digit(number):
    if number < 0:
        number = number * -1
    res = number % 10
    print("{:d}",format(res), end="")
    return res
