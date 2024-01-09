#!/usr/bin/python3
"""
Script that takes in a letter
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a params
"""


import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})

    try:
        resp_dict = response.json()
        if resp_dict:
            print(f"[{resp_dict['id']}] {resp_dict['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
