#!/usr/bin/python3


def fizzbuzz():
    fir i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz ", end="")
        continue
    elif i % 5 == 0:
        print ("Buzz ", end="")
        continue
    elif i % 3 == 0:
        print("Fizz ", end="")
    else:
        print("{:d}".format(i), end="")