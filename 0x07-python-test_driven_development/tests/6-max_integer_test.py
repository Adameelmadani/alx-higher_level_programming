#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This is TextMaxInteger class
    """

    def test_normallist(self):
        """
        This function test normal lists
        """

        self.assertEqual(max_integer([3, 8, 9, 48, 38]), 48)
        self.assertEqual(max_integer([3, -8, 0, -48, -38]), 3)
        self.assertEqual(max_integer([3]), 3)

    def test_nonelist(self):

        """
        This function test none list
        """
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
