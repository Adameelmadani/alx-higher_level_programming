#!/usr/bin/python3

"""
This is my Rectangle module
"""
from models.base import Base
"""
This is Base class
"""


class Rectangle(Base):
    """
    This is Rectangle class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is The constructor of Rectangle
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        property for width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        self.__width = value

    @property
    def height(self):
        """
        property for height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        self.__height = value

    @property
    def x(self):
        """
        property for x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        self.__x = value

    @property
    def y(self):
        """
        property for y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        setter for y
        """
        self.__y = value
