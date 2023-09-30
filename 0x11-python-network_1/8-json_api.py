#!/usr/bin/python3
"""Fetching and posting variable or json"""
import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = ""
    if len(sys.argv) != 1:
        q = sys.argv[1]
    r = requests.post(url, data={'q': q})
    try:
        a = r.json()
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
    else:
        if a:
            print("[{}] {}".format(a.get('id'), a.get('name')))
        else:
            print("No result")
