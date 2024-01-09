#!/usr/bin/python3
"""
Script that takes Github credentials
and display id using Github API
"""

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/users/{}".format(username)
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    user_id = response.json().get('id')
    print(user_id)
