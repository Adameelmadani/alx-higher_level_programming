#!/usr/bin/python3
import urllib.request
"""Fetching url"""
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    print("Body response:")
    body = response.read()
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
