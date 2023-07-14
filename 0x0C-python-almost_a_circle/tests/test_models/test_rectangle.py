#!/usr/bin/python3

"""
This is the unittest module for Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""
This is Rectangle module
"""
"""
This is unittest module
"""


class TestBase(unittest.TestCase):
    """
    This is TestBase class for testing Rectangle class
    """

    def test_all_numbers(self):
        """
        All numbers
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Rectangle(34, 38)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b2.width, 34)
        self.assertEqual(b2.height, 38)
        self.assertEqual(b2.x, 0)
        self.assertEqual(b2.y, 0)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(3994943939484333)
        self.assertEqual(b4.id, 3994943939484333)
        b5 = Base(-30494930309400303)
        self.assertEqual(b5.id, -30494930309400303)
        b6 = Base()
        self.assertEqual(b6.id, 3)
        b7 = Rectangle(3, 9, 4, 2, 2929)
        self.assertEqual(b7.id, 2929)
        self.assertEqual(b7.x, 4)
        self.assertEqual(b7.y, 2)
        b7.x = 33
        b7.y = 99
        self.assertEqual(b7.x, 33)
        self.assertEqual(b7.y, 99)
        b7.width = 8
        b7.height = 10
        self.assertEqual(b7.width, 8)
        self.assertEqual(b7.height, 10)
        b8 = Base(1)
        self.assertEqual(b8.id, 1)
        """
        Now raising errors
        """
        with self.assertRaises(ValueError):
            e1 = Rectangle(-3, -33, -3, -93, 8)
        with self.assertRaises(TypeError):
            e1 = Rectangle("_", "_", "_", "j", 88)
        with self.assertRaises(ValueError):
            e2 = Rectangle(8, -3, 0, 0, 8)
        with self.assertRaises(TypeError):
            e2 = Rectangle(8, -3, "_", "_", 8)
        with self.assertRaises(ValueError):
            e3 = Rectangle(0, 9, 0, 0, 0)
        """
        Calculating the area of a rectangle
        """
        self.assertEqual(b7.area(), 80)
        self.assertEqual(b2.area(), 34 * 38)
        b7.width = 8
        b7.height = 2
        self.assertEqual(b7.area(), 16)


if __name__ == "__main__":
    unittest.main()
