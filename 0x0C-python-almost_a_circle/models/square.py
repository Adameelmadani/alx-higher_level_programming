#!/usr/bin/python3

"""
This is square module
"""
from models.base import Base
from models.rectangle import Rectangle
"""
This is base module
"""
"""
This is rectangle module
"""


class Square(Rectangle):
    """
    This is square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This is instentiation
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This is str representation of square
        """
        part1 = "[Square] ({}) {}/".format(self.id, self._Rectangle__x)
        part2 = "{} - {}".format(self._Rectangle__y, self._Rectangle__width)
        return (part1 + part2)

    @property
    def size(self):
        """
        This is size getter
        """
        return (self._Rectangle__width)

    @size.setter
    def size(self, value):
        """
        This is size setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        This is update func for square class
        """
        i = 0
        if args != ():
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i = i + 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
