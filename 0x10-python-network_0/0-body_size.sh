#!/bin/bash
# A Bash script takes in a URL, sends a request to that URLand displays size of the body of the response.
curl -sI "$1" | grep -i "content-length" | awk '{print $2}'
