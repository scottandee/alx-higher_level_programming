#!/bin/bash
# This script finds the size of the body response 
curl -s "$1" | wc -m
