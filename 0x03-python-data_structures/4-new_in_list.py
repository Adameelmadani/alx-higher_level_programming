#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return (None)
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    new_list = []
    for i in range(0, len(my_list)):
        if i == idx:
            new_list.append(element)
            continue
        new_list.append(my_list[i])
    return (new_list)
