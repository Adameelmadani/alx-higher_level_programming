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

    def to_json(self, attrs=None):
        """
        dic of Student
        """
        my_dic = self.__dict__
        new_dic = {}
        if attrs is not None:
            for i in attrs:
                if type(i) is not str:
                    return (my_dic)
            for i in attrs:
                if i in my_dic.keys():
                    new_dic[i] = my_dic[i]
            return (new_dic)
        return (my_dic)
