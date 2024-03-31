#!/bin/bash
# This script retrieves the Content-Length header from a URL using curl

# Send a HEAD request to the URL and suppress the progress output (-s)
# The -I option instructs curl to fetch only the headers of the response
# Store the output in a variable for further processing
response=$(curl -sI "$1")

# Use grep to search for the Content-Length header case-insensitively
# Pipe the output to cut, specifying space as the delimiter (-d " ")
# Select the second field (-f 2) which contains the value of Content-Length
# Print the value of Content-Length
grep -i "Content-Length" <<< "$response" | cut -d " " -f 2
