#!/usr/bin/python3
"""
Script that lists the last 10 commits of a given repo
"""


import sys
import requests

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner, repository
            )
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f"{sha}: {author}")
