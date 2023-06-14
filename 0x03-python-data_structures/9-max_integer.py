#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    for i in range(0, len(my_list)):
        if i == 0:
            m = my_list[i]
        else:
            if my_list[i] > m:
                m = my_list[i]
    return (m)
