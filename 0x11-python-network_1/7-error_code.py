#!/usr/bin/python3
"""Fetching url and handling exceptions"""
import sys
import requests


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(r.status_code))
