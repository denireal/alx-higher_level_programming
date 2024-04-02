#!/bin/bash
# Script to send a DELETE request to a URL using curl

# Send a DELETE request to the provided URL and suppress output
curl -s "$1" -X DELETE
