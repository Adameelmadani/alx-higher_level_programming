#!/usr/bin/python3

"""
This is our module
"""
import json
"""
This is json module
"""


def load_from_json_file(filename):
    """
    This is load func
    """
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
