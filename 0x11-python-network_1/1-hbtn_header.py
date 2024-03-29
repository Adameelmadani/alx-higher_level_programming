#!/usr/bin/python3
"""Get request so that we print X-request_id in the response header"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
