#!/usr/bin/python3
"""
This search API module takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q, if not set q="".
If the response body is properly JSON formatted and not empty, display the
id and name like this: [<id>] <name>, Otherwise: Display Not a valid JSON
if the JSON is invalid and Display No result if the JSON is empty
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {"q": q}
    response = requests.post(url, data=payload)
    try:
        json_resp = response.json()
        if not json_resp:
            print("No result")
        else:
            the_id = json_resp.get("id")
            u_name = json_resp.get("name")
            print("[{}] {}".format(the_id, u_name))
    except ValueError as invalid_json:
        print("Not a valid JSON")
