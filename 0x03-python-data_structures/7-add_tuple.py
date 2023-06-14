#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        s_tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        s_tuple_a = tuple_a + (0, )
    else:
        s_tuple_a = tuple_a
    if len(tuple_b) == 0:
        s_tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        s_tuple_b = tuple_b + (0, )
    else:
        s_tuple_b = tuple_b
    for i in range(0, 2):
        if i == 0:
            add_tuple_f = (s_tuple_a[i] + s_tuple_b[i], )
        else:
            add_tuple = add_tuple_f + (s_tuple_a[i] + s_tuple_b[i], )
    return (add_tuple)
