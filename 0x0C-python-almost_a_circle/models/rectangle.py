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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This function calculate the area of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        This funct displays rectangle
        """
        for k in range(self.__y):
            print("")
        for i in range(self.__height):
            for m in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        This is str representation
        """
        part_1 = "[Rectangle] ({}) {}/{} ".format(self.id, self.__x, self.__y)
        part_2 = "- {}/{}".format(self.__width, self.__height)
        return (part_1 + part_2)

    def update(self, *args, **kwargs):
        """
        This function is for updating rectangle instance
        """
        i = 0
        if args != ():
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        This is dictionary containing elements of Rectangle
        """
        rect_dic = {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
        }
        return (rect_dic)
