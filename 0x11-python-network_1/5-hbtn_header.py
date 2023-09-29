#!/usr/bin/python3
"""Fetching url and getting X-request-id"""
import sys
import requests
r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])
