#!/usr/bin/python3
"""
Sends an HTTP GET request to a URL and prints the value of the X-Request-Id
header in the response.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the script is being run directly
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    # Get the URL from the command-line arguments
    u = sys.argv[1]

    # Send an HTTP GET request to the URL
    r = requests.get(u)

    # Get the value of the X-Request-Id header from the response
    v = r.headers.get("X-Request-Id")

    # Print the value of the X-Request-Id header
    print(v)
