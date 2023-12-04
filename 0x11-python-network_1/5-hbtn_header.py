#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id var in the header of the response.
Only imported packages are requests and sys
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    val = response.headers.get("X-Request-Id")
    print(val)
