#!/bin/bash
# This script retrieves the Content-Length header from a URL using curl

# curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
# Check if the number of arguments provided is not equal to 1
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response_body=$(curl -s "$1")
size=$(echo -n "$response_body" | wc -c)
echo "Size of the response body: $size bytes"
