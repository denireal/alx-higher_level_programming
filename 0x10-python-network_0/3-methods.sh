#!/bin/bash
# Takes a URL and displays all HTTP methods the server accepts
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
