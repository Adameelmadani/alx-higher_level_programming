#!/usr/bin/python3

"""
This is rectangle module
"""


class Rectangle:
    """
    This is Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
                my_str = my_str + str(self.print_symbol)
            if i != (self._Rectangle__height - 1):
                my_str = my_str + "\n"
        return (my_str)

    def __repr__(self):
        """
        repr for self
        """
        r_height = self._Rectangle__height
        rep = "Rectangle({}, {})".format(self._Rectangle__width, r_height)
        return (rep)

    def __del__(self):
        """
        deleting a rectangle instance
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the bigger rectangle based on its erea
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return (rect_2)
        return (rect_1)

    @classmethod
    def square(cls, size=0):
        """
        returns a square instance of Rectangle class
        """
        new_rect = cls(size, size)
        return (new_rect)
