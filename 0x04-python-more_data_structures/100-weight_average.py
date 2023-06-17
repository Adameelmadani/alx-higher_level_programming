#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return (0)
    if len(my_list) == 0:
        return (0)
    s = 0
    a = 0
    for i in range(len(my_list)):
        s = s + (my_list[i][0] * my_list[i][1])
        a = a + my_list[i][1]
    n = s / a
    return (n)
