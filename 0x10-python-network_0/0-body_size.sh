#!/bin/bash
# Bash script to retrieve the content of a URL and count the number of characters.

curl -s "${1}" | wc -c
