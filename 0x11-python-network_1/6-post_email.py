#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter
and prints the response body.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the script is being run directly
    if len(sys.argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        sys.exit(1)

    # Get URL and email from command-line arguments
    u = sys.argv[1]
    e = sys.argv[2]

    # Create payload with email parameter
    p = {"email": e}

    # Send POST request with payload
    r = requests.post(u, data=p)

    # Print response body
    print(r.text)
