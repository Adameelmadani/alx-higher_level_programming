#!/usr/bin/python3
"""POST url with email value"""
import sys
import requests


if __name__ == "__main__":
    r = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(r.text)
