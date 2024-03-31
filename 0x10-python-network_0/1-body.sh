#!/bin/bash

# Send a GET request to the URL specified as the first argument
# The -L option instructs curl to follow redirects
# The -s option suppresses progress meter and other unnecessary information
# The -S option displays errors if they occur
curl -LsS "$1"
