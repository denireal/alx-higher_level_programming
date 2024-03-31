#!/usr/bin/python3

"""
This script sends an HTTP GET request to 'https://intranet.hbtn.io/status'
and prints information about the response content.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
