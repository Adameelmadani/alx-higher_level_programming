#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    i = 0
    for key, value in a_dictionary.items():
        if i == 0:
            s = value
            s_key = key
        else:
            if value > s:
                s = value
                s_key = key
        i = i + 1
    return (s_key)
