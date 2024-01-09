#!/usr/bin/python3
"""
Script that takes an URL and email
send POST request with email as params
display the body of response
"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    response = requests.post(url, email)
    print(response.text)
