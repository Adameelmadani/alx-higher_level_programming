#!/usr/bin/python3

"""
This is the unittest module for Square class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""
This is Rectangle module
"""
"""
This is unittest module
"""
"""
This is base module
"""
"""
This is square module
"""


class TestBase(unittest.TestCase):
    """
    This is TestBase class for testing Square class
    """

    def test_all_numbers(self):
        """
        All numbers
        """
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s2 = Square(3, 8, 9, 83)
        self.assertEqual(s2.x, 8)
        self.assertEqual(s2.y, 9)
        self.assertEqual(s2.id, 83)
        s2.x = 32
        s2.y = 83
        self.assertEqual(str(s2), "[Square] (83) 32/83 - 3")
        s3 = Square(8, 0, 0, 1)
        s3.size = 10
        self.assertEqual(str(s3), "[Square] (1) 0/0 - 10")
        self.assertEqual(s3.size, 10)

    def test_errors_att(self):
        """
        Now raising errors
        """
        with self.assertRaises(ValueError):
            e1 = Square(-3, -33, -3, -93)
        with self.assertRaises(TypeError):
            e1 = Square("_", "_", "_", "j")
        with self.assertRaises(ValueError):
            e2 = Square(8, -3, 0, 0)
        with self.assertRaises(TypeError):
            e2 = Square(8, -3, "_", "_")
        with self.assertRaises(ValueError):
            e3 = Square(0, 9, 0, 0)
        s1 = Square(2, 0, 0, 3)
        with self.assertRaises(ValueError):
            s1.size = 0
        with self.assertRaises(TypeError):
            s1.size = "h"

    def test_area(self):
        """
        Calculating the area of a square
        """
        a1 = Square(34)
        a2 = Square(10)
        self.assertEqual(a2.area(), 100)
        self.assertEqual(a1.area(), 34 * 34)

    def test_str(self):
        """
        Testing str of square instance
        """
        r1 = Square(4, 6, 2, 1)
        self.assertEqual(str(r1), "[Square] (1) 6/2 - 4")

    def test_update(self):
        """
        Testing update
        """
        u1 = Square(10, 10, 10, 10)
        self.assertEqual(str(u1), "[Square] (10) 10/10 - 10")
        u1.update(89)
        self.assertEqual(str(u1), "[Square] (89) 10/10 - 10")
        u1.update(89, 2)
        self.assertEqual(str(u1), "[Square] (89) 10/10 - 2")
        u1.update(89, 2, 3)
        self.assertEqual(str(u1), "[Square] (89) 10/10 - 2")
        u1.update(89, 2, 3, 4)
        self.assertEqual(str(u1), "[Square] (89) 4/10 - 2")

    def test_update_the_update(self):
        """
        Testing the 9th task
        """
        ur1 = Square(10, 10, 10, 10)
        self.assertEqual(str(ur1), "[Square] (10) 10/10 - 10")
        """
        ur1.update(size=1)
        self.assertEqual(str(ur1), "[Square] (10) 10/10 - 1")
        ur1.update(size=1, x=2)
        self.assertEqual(str(ur1), "[Square] (10) 2/10 - 1")
        ur1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(ur1), "[Square] (89) 3/1 - 2")
        ur1.update(x=1, y=3, size=4)
        self.assertEqual(str(ur1), "[Square] (89) 1/3 - 4")
        ur1.update(2, 5, x=3)
        self.assertEqual(str(ur1), "[Square] (2) 1/3 - 5")
        """


if __name__ == "__main__":
    unittest.main()
