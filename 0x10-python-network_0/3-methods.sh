#!/bin/bash
# takes in a url and display all allowed methods of the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
