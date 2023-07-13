#!/usr/bin/python3

"""
This is the unittest module for Base class
"""
import unittest
from models.base import Base
"""
This is Base module
"""
"""
This is unittest module
"""


class TestBase(unittest.TestCase):
    """
    This is TestBase class for testing Base class
    """

    def test_all_numbers(self):
        """
        All numbers
        """
        b1 = Base(20)
        self.assertEqual(b1.id, 20)
        b2 = Base(-34)
        self.assertEqual(b2.id, -34)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(3994943939484333)
        self.assertEqual(b4.id, 3994943939484333)
        b5 = Base(-30494930309400303)
        self.assertEqual(b5.id, -30494930309400303)
        b6 = Base()
        self.assertEqual(b6.id, 1)
        b7 = Base()
        self.assertEqual(b7.id, 2)
        b8 = Base(1)
        self.assertEqual(b8.id, 1)


if __name__ == "__main__":
    unittest.main()
