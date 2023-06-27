#!/usr/bin/python3

"""
This module contains Square class
"""


class Square:
    """
    This class is the square class
    """
    def __init__(self, size=0):
        """
        This is the initialisation

        Args:
             _Square__size (int): size of square
        """
        self._Square__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
