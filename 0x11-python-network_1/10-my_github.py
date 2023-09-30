#!/usr/bin/python3
"""Authenticate with github using username and pwd"""
import sys
import requests


class GitAuth(requests.auth.AuthBase):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def __call__(self, r):
        self.headers['username'] = self.user
        self.headers['password'] = self.pwd
        return (r)

if __name__ == "__main__":
    res = requests.get('https://api.github.com/applications/YOUR_CLIENT_ID/token')
