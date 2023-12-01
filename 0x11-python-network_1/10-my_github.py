#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id.
The first argument will be your username.
The second argument will be your password (in your case, a personal
access token as password).
"""
import sys
from requests.auth import HTTPBasicAuth
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    json_resp = response.json()
    print(json_resp.get("id"))
