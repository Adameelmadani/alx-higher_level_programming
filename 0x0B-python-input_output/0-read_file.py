#!/usr/bin/python3

"""
This is our modul
"""


def read_file(filename=""):
    """
    This is our func
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
