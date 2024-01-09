#!/usr/bin/python3
"""
Script that takes Github credentials
and display id using Github API
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    response = requests.get("https://api.github.com/user", auth=auth)
    user_id = response.json().get("id")
    print(user_id)
