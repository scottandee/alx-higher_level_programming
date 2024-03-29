#!/usr/bin/python3
"""
This script adds all arguments into
a python file and saves them to a file
"""

import json
import sys
import os.path
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


init_list = []

# We check if that directory exists.
# If it doesn't, we create it and put in an empty list
if not os.path.exists('add_item.json'):
    with open("add_item.json", mode="w", encoding="utf-8") as f:
        f.write(json.dumps(init_list))

# If it does, we load and then append
my_list = load_from_json_file("add_item.json")
for i in range(len(sys.argv)):
    if i == 0:
        continue
    my_list.append(sys.argv[i])

save_to_json_file(my_list, "add_item.json")
