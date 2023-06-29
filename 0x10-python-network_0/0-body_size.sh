#!/bin/bash
# This script takes in a URL and displays the 
# size of the body response
curl -s "$1" | wc -m
