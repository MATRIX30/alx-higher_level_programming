#!/bin/bash
# takes in a url and display all allowed methods of the server
curl -s -X OPTIONS "$1"
