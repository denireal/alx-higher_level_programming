#!/bin/bash
# This script retrieves the Content-Length header from a URL using curl

curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
