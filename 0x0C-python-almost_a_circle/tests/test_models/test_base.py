#!/usr/bin/python3

"""
This is the unittest module for Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""
This is Base module
"""
"""
This is Rectangle module
"""
"""
This is unittest module
"""
"""
This is square module
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
        b6 = Base(1)
        self.assertEqual(b6.id, 1)
        b7 = Base(2)
        self.assertEqual(b7.id, 2)
        b8 = Base(1)
        self.assertEqual(b8.id, 1)

    def test_to_dictionary(self):
        """
        Testing to_dictionary func
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        str_a = {'x': 2, 'y': 8, 'id': 1, 'height': 7, 'width': 10}
        self.assertEqual(dictionary, str_a)
        a = Base.to_json_string([dictionary])
        str_b = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'
        self.assertEqual(a, str_b)
        b = Base.to_json_string([])
        self.assertEqual(b, "[]")
        c = Base.to_json_string(None)
        self.assertEqual(c, "[]")

    def test_save_to_file(self):
        """
        Testing save_to_file func
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as f:
            my_str = f.read()
        part1 = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}, '
        part2 = '{"x": 0, "y": 0, "id": 2, "height": 4, "width": 2}]'
        self.assertEqual(my_str, part1 + part2)
        s1 = Square(10, 7, 2, 3)
        Square.save_to_file([s1, r1])
        with open("Square.json", "r") as fs:
            my_sstr = fs.read()
        spart1 = '[{"id": 3, "x": 7, "size": 10, "y": 2}, '
        spart2 = '{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'
        self.assertEqual(my_sstr, spart1 + spart2)

    def test_from_json_string(self):
        """
        Testing from_json_string func
        """
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Square.from_json_string("[]"), [])
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        a = Square.to_json_string(list_input)
        self.assertEqual(Square.from_json_string(a), list_input)

    def test_create(self):
        """
        Testing create func
        """
        r1 = Rectangle(3, 5, 1, 0, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), str(r1))
        self.assertEqual(r1 == r2, False)
        dics = {'size': 4, 'id': 2}
        s2 = Square.create(**dics)
        self.assertEqual(str(s2), "[Square] (2) 0/0 - 4")


if __name__ == "__main__":
    unittest.main()
