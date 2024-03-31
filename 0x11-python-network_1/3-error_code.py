#!/usr/bin/python3
"""
Fetches content from a URL and prints the response text.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # Check if the script is being run directly
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    # Extract the URL from command-line arguments
    url = sys.argv[1]

    try:
        # Send a request to the URL and handle the response
        with urllib.request.urlopen(url) as response:
            # Read and decode the response text
            response_text = response.read().decode("utf-8")
            # Print the response text
            print(response_text)
    except urllib.error.HTTPError as e:
        # If an HTTP error occurs, print the error code
        print("Error code: {}".format(e.code))
