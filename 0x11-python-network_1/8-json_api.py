#!/usr/bin/python3
"""
Sends a POST request to a URL with a query parameter 'q' and prints the
response.
"""

import sys
import requests

if __name__ == "__main__":
    # URL to send the POST request
    url = "http://0.0.0.0:5000/search_user"
    
    # Set the query parameter 'q' from command-line argument if provided
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # Create payload with query parameter
    payload = {"q": query}
    
    # Send POST request with payload
    response = requests.post(url, data=payload)
    
    # Process the JSON response
    try:
        # Parse JSON response
        json_output = response.json()
        
        # Extract 'id' and 'name' fields from JSON response
        user_id = json_output.get("id")
        user_name = json_output.get("name")
        
        # Print the 'id' and 'name' fields
        if not json_output:
            print("No result")
        else:
            print("[{}] {}".format(user_id, user_name))
    except ValueError:
        # Handle case where response is not a valid JSON
        print("Not a valid JSON")
