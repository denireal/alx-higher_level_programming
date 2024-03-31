#!/bin/bash
# Bash script to retrieve the content of a URL and count the number of responses

curl -sI "$1" | grep Content-Length | cut -d " " -f2
