#!/usr/bin/python3
for i in range(0, 100):
    if (i < 10) & (i >= 0):
        s = "0{}".format(i)
    else:
        s = "{}".format(i)
    if i != 99:
        print("{}, ".format(s), end='')
    else:
        print(s)
