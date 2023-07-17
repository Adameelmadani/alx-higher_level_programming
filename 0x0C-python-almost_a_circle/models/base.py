#!/usr/bin/python3

"""
This module contains the Base class
"""
import json
import os
"""
This is json module
"""
"""
This is os module
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

    @staticmethod
    def from_json_string(json_string):
        """
        This func convert json_string to python_dict
        """
        if json_string is None or json_string == "":
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        This creates a new instance containing elements of dictionary
        """
        if cls.__name__ == "Rectangle":
            b1 = cls(1, 1)
        else:
            b1 = cls(1)
        b1.update(**dictionary)
        return (b1)

    @classmethod
    def load_from_file(cls):
        """
        This func loads from json file
        """
        Base.from_json_string("")
        new_list = []
        f_name = cls.__name__ + ".json"
        if not os.path.exists(f_name):
            return (new_list)
        with open(f_name, "r", encoding="utf-8") as f:
            f_data = json.load(f)
        for element in f_data:
            new_list.append(cls.create(**element))
        return (new_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        This func save csv to file
        """
        f_name = cls.__name__ + ".csv"
        new_list = "[\n"
        if list_objs is not None:
            for e in list_objs:
                if cls.__name__ == "Rectangle":
                    part1 = "{},{},".format(e.id, e.width)
                    part2 = "{},{},{}".format(e.height, e.x, e.y)
                else:
                    part1 = "{},{},".format(e.id, e.size)
                    part2 = "{},{}".format(e.x, e.y)
                my_str = part1 + part2
                new_list += my_str + "\n"
        new_list += "]"
        with open(f_name, "w", encoding="utf-8") as f:
            f.write(new_list)

    @classmethod
    def load_from_file_csv(cls):
        """
        This func load csv from a file
        """
        f_name = cls.__name__ + ".csv"
        new_list = []
        if not os.path.exists(f_name):
            return (new_list)
        with open(f_name, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            new_line = line.strip()
            if new_line == "[" or new_line == "]":
                continue
            w = new_line.split(",")
            if len(w) == 5:
                b1 = cls(int(w[1]), int(w[2]), int(w[3]), int(w[4]), int(w[0]))
            else:
                b1 = cls(int(w[1]), int(w[2]), int(w[3]), int(w[0]))
            new_list.append(b1)
        return (new_list)
