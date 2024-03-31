#!/usr/bin/python3
"""
Retrieves information about recent commits from a GitHub repository
and prints the commit SHA and author name.
"""

import sys
import requests

if __name__ == "__main__":
    try:
        # Ensure correct usage of command-line arguments
        if len(sys.argv) != 3:
            print("Usage: ./script.py <repository> <username>")
            sys.exit(1)

        # Extract repository name and username from command-line arguments
        repo, user = sys.argv[1], sys.argv[2]
        
        # Construct the URL for retrieving commits
        commits_url = f"https://api.github.com/repos/{user}/{repo}/commits"
        
        # Send a GET request to the commits URL
        response = requests.get(commits_url)
        
        # Ensure a successful response
        response.raise_for_status()
        
        # Parse the JSON response
        commits_data = response.json()
        
        # Print information about recent commits
        for commit in commits_data[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except (IndexError, requests.RequestException) as e:
        print("Error:", e)
