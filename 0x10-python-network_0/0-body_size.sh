#!/bin/bash
# takes url n sends requests to url and displays the body size of the response
curl -s -o /dev/null -w "%{size_download}\n" "$1"
