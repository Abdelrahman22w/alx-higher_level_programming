#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -Is "$1" | grep "ALLOW: " | cut -d ' ' -f 2-
