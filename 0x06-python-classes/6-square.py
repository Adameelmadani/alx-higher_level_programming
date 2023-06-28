#!/usr/bin/python3

"""
This module contains Square class
"""


class Square:
    """
    This class is the square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This is the initialisation

        Args:
             _Square__size (int): size of square
             _Square__position (tuple): position of square
        """
        self._Square__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__position = position
        if (type(position) is not tuple) or (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position[0]) is not int) or (type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """
        This is the getter of position
        """
        return (self._Square__position)

    @position.deleter
    def position(self):
        """
        This is the deleter of position
        """
        self._Square__position = None

    @position.setter
    def position(self, value):
        """
        This is the setter of position
        """
        if (type(position) is not tuple) or (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position[0]) is not int) or (type(position[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0) or (position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = value

    def area(self):
        """
        This method returns the area of a square
        """
        return (self._Square__size ** 2)

    def my_print(self):
        """
        This is the function that prints a square using #
        """
        for i in range(0, self._Square__position[1]):
            print('')
        if self._Square__size == 0:
            print('')
        for j in range(0, self._Square__size):
            for k in range(0, self._Square__size):
                if k == 0:
                    for m in range(0, self._Square__position[0]):
                        print(' ', end='')
                print('#', end='')
            print('')
