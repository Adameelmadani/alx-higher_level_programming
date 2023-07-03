#!/usr/bin/python3

"""
This is say_my_name module
"""


def say_my_name(first_name, last_name=""):
    """
    This function printf full name
    """

    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    elif not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    """
    This doctest module
    """
    doctest.testfile(".tests/3-say_my_name.txt")
