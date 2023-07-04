#!/usr/bin/python3

"""
This is rectangle module
"""


class Rectangle:
    """
    This is Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        This is __init__ function
        """

        for i in [width, height]:
            if i == width:
                my_str = "width"
            else:
                my_str = "height"
            if type(i) is not int:
                raise TypeError("{} must be an integer".format(my_str))
            if i < 0:
                raise ValueError("{} must be >= 0".format(my_str))
        self._Rectangle__width = width
        self._Rectangle__height = height

    @property
    def width(self):
        """
        property for width
        """
        return (self._Rectangle__width)

    @width.setter
    def width(self, val):
        """
        setter for width
        """
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = val

    @width.deleter
    def width(self):
        """
        deleter for width
        """
        del self._Rectangle__width

    @property
    def height(self):
        """
        property for height
        """
        return (self._Rectangle__height)

    @height.setter
    def height(self, val):
        """
        setter for height
        """
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = val

    @height.deleter
    def height(self):
        """
        deleter for height
        """
        del self._Rectangle__height

    def area(self):
        """
        calculate area of rectangle
        """
        return (self._Rectangle__width * self._Rectangle__height)

    def perimeter(self):
        """
        calculate perimeter
        """
        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return (0)
        return (2 * (self._Rectangle__width + self._Rectangle__height))

    def __str__(self):
        """
        string representation
        """
        my_str = ""
        if self._Rectangle__height == 0 or self._Rectangle__width == 0:
            return (my_str)
        for i in range(self._Rectangle__height):
            for j in range(self._Rectangle__width):
                my_str = my_str + "#"
            if i != (self._Rectangle__height - 1):
                my_str = my_str + "\n"
        return (my_str)
