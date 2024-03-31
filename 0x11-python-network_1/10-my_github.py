#!/usr/bin/python3
"""
Retrieves user information from the GitHub API using basic authentication
and prints the user ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # URL for the GitHub API
    url = "https://api.github.com/user"

    # Username and password obtained from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Send GET request to the GitHub API with basic authentication
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    # Parse JSON response
    json_response = response.json()

    # Extract and print the user ID
    user_id = json_response.get("id")
    print(user_id)
