#!/usr/bin/python3
"""Sends a request to a URL and displays the value of the X-Request-Id
variable in the response header.
"""

import sys
from urllib import request

if __name__ == "__main__":
    # Get URL from command-line arguments
    url = sys.argv[1]

    # Send request to the URL
    with request.urlopen(url) as response:
        # Retrieve the value of X-Request-Id variable from the response header
        x_request_id = response.headers.get('X-Request-Id')

        # Display the value of the X-Request-Id variable
        print(x_request_id)
