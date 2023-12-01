#!/usr/bin/python3
"""
This module that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    param = {
        "email": email
    }
    url_query = urllib.parse.urlencode(param)
    the_data = url_query.encode("ascii")
    req = urllib.request.Request(url, the_data)
    with urllib.request.urlopen(req) as response:
        # urllib uses a GET request if you do not pass the data argument.
        # Difference is that POST requests
        # have "side-effects".
        response_string = response.read().decode("utf-8")
        print(response_string)
