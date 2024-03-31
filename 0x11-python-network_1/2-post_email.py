#!/usr/bin/python3
"""
Sends a POST request to the specified URL with an email parameter
and prints the response body.
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    param = {
        "email": email
    }
    query_string = urllib.parse.urlencode(param)
    data = query_string.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        response_text = response.read().decode("utf-8")
        print(response_text)
