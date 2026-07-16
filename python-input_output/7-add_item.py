#!/usr/bin/python3
"""
Script for adding command-line arguments to a list stored in a JSON file.

Usage:
./7-add_item arg1 arg2 arg3 ...

The script reads the current list from the "add_item.json"
file, and appends the given command-line arguments to the list.
If the file does not exist, it will be created with an empty list.
The updated list is then written back to the file.
"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    json_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    json_data = []

for arg in sys.argv[1:]:
    json_data.append(arg)

save_to_json_file(json_data, "add_item.json")
