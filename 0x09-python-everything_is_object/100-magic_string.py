#!/usr/bin/python3
ite = 0


def magic_string():
    global ite
    ite = ite + 1
    my_str = ""
    for i in range(ite):
        if i != (ite - 1):
            my_str += "BestSchool, "
        else:
            my_str += "BestSchool"
    return my_str
