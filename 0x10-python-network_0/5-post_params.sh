#!/bin/bash
# This scipt sends a POST request and specifies the data
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
