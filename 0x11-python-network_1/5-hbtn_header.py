#!/usr/bin/python3
"""Fetching url and getting X-request-id"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
