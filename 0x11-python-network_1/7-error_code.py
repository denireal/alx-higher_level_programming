#!/usr/bin/python3
"""
Fetches content from a URL using the requests library and
prints the response body.
"""

import sys
import requests

if __name__ == "__main__":
    # Check if the script is being run directly
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    # Get the URL from the command-line arguments
    u = sys.argv[1]

    # Send a GET request to the URL
    r = requests.get(u)

    # Get the response body
    b = r.text

    # Check if the status code is an error
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        # Print the response body
        print(b)
