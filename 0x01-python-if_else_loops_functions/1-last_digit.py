#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = abs(number) % 10

if number < 0:
    i *= -1
if i > 5:
    print("last digit of {:d} is {:d} and is greater than 5"
          .format(number, i))

elif i == 0:
    print("last digit of {:d} is {:d}".format(number, i))

else:
    print("last digit of {} is {} and is less than 6 and not 0"
          .format(number, i))
