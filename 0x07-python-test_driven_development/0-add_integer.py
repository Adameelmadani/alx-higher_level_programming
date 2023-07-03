#!/usr/bin/python3

"""
This is add module
"""


def add_integer(a, b=98):
    """
    This function returns the addition of two integers
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)


if __name__ == "__main__":
    import doctest
    """
    This is doctest module
    """
    doctest.testfile("./tests/0-add_integer.txt")
