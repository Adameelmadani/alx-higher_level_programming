#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return (str)
    s = ""
    i = 0
    for c in str:
        if i != n:
            s = s + c
        i = i + 1
    return (s)
