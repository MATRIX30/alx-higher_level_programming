#!/bin/bash
# bash script to DELETE request to url passd as first argument and displays body of response
curl -s -X DELETE "$1"
