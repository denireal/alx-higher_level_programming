#!/bin/bash
# Script to send a DELETE request to a URL using curl

# Output a message indicating a DELETE request is being made
echo "I'm a DELETE request"

# Send a DELETE request to the provided URL and suppress output
curl -s "$1" -X DELETE
