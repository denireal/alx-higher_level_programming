#!/usr/bin/python3
"""
Fetches content from a URL using the requests library and prints information
about the response content.
"""

import requests

if __name__ == "__main__":
    # URL to send the GET request
    url = "https://alx-intranet.hbtn.io/status"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Get the content of the response
    content = response.text
    
    # Print information about the response content
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
