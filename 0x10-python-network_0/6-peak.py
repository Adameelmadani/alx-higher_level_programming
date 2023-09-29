#!/usr/bin/env python3
"""This is our module"""
def find_peak(list_of_integers):
    """find_pack function"""
    if list_of_integers.length == 0:
        return (None)
    for i in range(1, list_of_integers.length - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            return (i);
