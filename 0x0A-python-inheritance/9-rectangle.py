#!/usr/bin/python3

"""
This is our module
"""


class BaseGeometry:
    """
    This is class
    """
    def area(self):
        """
        This is p inst meth
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This is funct
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    This class inherate from basegeom
    """
    def __init__(self, width, height):
        """
        This is initi
        """
        self._Rectangle__width = width
        self._Rectangle__height = height
        self.integer_validator("width", self._Rectangle__width)
        self.integer_validator("height", self._Rectangle__height)

    def area(self):
        """
        This is our fucnt
        """
        return (self._Rectangle__width * self._Rectangle__height)

    def __str__(self):
        """
        This is str
        """
        s = "{}/{}".format(self._Rectangle__width, self._Rectangle__height)
        return ("[Rectangle] " + s)
