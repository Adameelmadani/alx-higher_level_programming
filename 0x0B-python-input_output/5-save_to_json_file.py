#!/usr/bin/python3

"""
This is our module
"""
import json
"""
This is json module
"""


def save_to_json_file(my_obj, filename):
    """
    This is save json obj to file
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
