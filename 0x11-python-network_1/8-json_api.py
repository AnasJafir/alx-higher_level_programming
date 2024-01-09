#!/usr/bin/python3
"""
Script that takes in a letter
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a params
"""


import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    par = {'q': q}
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    response = requests.post(url, par)
    try:
        data = response.json()
        id, name = data.get('id'), data.get('name')
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
