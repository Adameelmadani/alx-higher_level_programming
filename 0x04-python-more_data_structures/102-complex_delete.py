#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_key = []
    for key, val in a_dictionary.items():
        if val == value:
            list_key.append(key)
    for i in range(len(list_key)):
        del a_dictionary[list_key[i]]
    return (a_dictionary)
