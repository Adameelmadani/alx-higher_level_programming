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
