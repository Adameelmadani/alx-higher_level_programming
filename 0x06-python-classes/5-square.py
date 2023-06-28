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

    @property
    def size(self):
        """
        This is the getter of size
        """
        return (self._Square__size)

    @size.deleter
    def size(self):
        """
        This is the deleter of size
        """
        self._Square__size = None

    @size.setter
    def size(self, value):
        """"
        This is the setter of size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """
        This method returns the area of a square
        """
        return (self._Square__size ** 2)

    def my_print(self):
        """
        This is the function that prints a square using #
        """
        if self._Square__size == 0:
            print('')
        for i in range(0, self._Square__size):
            for i in range(0, self._Square__size):
                print('#', end='')
            print('')
