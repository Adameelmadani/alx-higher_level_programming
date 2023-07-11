#!/usr/bin/python3

"""
our module
"""
import sy
import json
import os
"""
os modul
"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
load module
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""
save module
"""

if not os.path.exists("add_item.json"):
    save_to_json_file([], "add_item.json")
elif load_from_json_file("add_item.json") == "\n":
    save_to_json_file([], "add_item.json")
first_list = load_from_json_file("add_item.json")
for i in range(1, len(sys.argv)):
    first_list.append(sys.argv[i])
save_to_json_file(first_list, "add_item.json")
