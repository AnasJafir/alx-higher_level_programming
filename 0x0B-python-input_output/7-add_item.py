#!/usr/bin/python3
""" Load, add, save  """
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    # Try to load the existing list from the file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty list
    items = []

# Add the arguments to the list
items.extend(sys.argv[1:])

# Save the list back to the file
save_to_json_file(items, filename)
