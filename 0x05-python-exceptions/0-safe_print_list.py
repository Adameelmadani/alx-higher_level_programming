#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if x < 0:
        raise Exception("Number is negative")
    i = j = 0
    for element in my_list:
        i = i + 1
    if x > i:
        x = i
    for j in range(0, x):
        print(my_list[j], end="")
    print("")
    if i == 0:
        return (0)
    return (j + 1)
