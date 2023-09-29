#!/usr/bin/python3
"""Post request with email variable"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    values = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(sys.argv[1], values)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
