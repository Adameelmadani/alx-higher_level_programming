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
