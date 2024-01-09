#!/usr/bin/python3
"""
Script that takes an URL and email
send a POST request to the passed URL
with email as a params
"""


import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
