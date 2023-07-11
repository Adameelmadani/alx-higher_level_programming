#!/usr/bin/python3

"""
This is our module
"""


def write_file(filename="", text=""):
    """
    This is write funct
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
