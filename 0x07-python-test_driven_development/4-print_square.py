#!/usr/bin/python3

"""
This is print square
"""


def print_square(size):
    """
    This is print_square function
    """

    if not type(size) is int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")


if __name__ == "__main__":
    import doctest
    """
    This is doctest module
    """
    doctest.testfile("./tests/4-print_square.txt")
