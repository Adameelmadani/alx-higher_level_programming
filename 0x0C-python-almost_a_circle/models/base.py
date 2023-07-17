#!/usr/bin/python3

"""
This module contains the Base class
"""
import json
"""
This is json module
"""


class Base:
    """
    This is the base class of all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the constructor of Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This funct returns string representation of JSON dict
        """
        if list_dictionaries is None:
            return ("[]")
        if list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This is class method is saves the JSON rep of list_objs
        """
        my_list = list_objs
        if list_objs is None:
            my_list = []
        my_file = cls.__name__ + ".json"
        new_list = []
        for i in my_list:
            new_list.append(i.to_dictionary())
        with open(my_file, "w", encoding="utf-8") as f:
            f.write(Base.to_json_string(new_list))
