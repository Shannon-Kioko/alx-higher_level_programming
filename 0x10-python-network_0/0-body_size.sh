#!/bin/bash
# script takes in a URL, sends a request to that URL
#and displays size of the body of the response.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
