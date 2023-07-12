#!/usr/bin/python3

"""
This is our module
"""


class Student():
    """
    This is student class
    """
    def __init__(self, first_name, last_name, age):
        """
        This is instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        dic of Student
        """
        return (self.__dict__)
