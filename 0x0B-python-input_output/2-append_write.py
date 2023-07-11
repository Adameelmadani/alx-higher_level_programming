#!/usr/bin/python3

"""
This is our module
"""


def append_write(filename="", text=""):
    """
    This is append write
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
