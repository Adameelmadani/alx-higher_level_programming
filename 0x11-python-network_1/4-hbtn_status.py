#!/usr/bin/python3
"""Fetching url"""
import requests
r = requests.get('https://alx-intranet.hbtn.io/status').text
print("Body response:")
print("\t- type: {}".format(type(r)))
print("\t- content: {}".format(r))
