#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n1umber = number
if number < 0:
    n1umber = -number
d = n1umber % 10
if d == 0:
    print(f"Last digit of {number} is {d} and is 0")
elif d < 6:
    print(f"Last digit of {number} is {d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {d} and is greater than 5")
