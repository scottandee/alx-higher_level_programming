#!/bin/bash
# This script gets all methods that a server will accept
curl -sI -X OPTIONS "$1" | grep Allow | cut --complement -d " " -f 1
