#!/usr/bin/python3
"""
7-add_item module
"""


import json
import os
import sys
from sys import argv

save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file
myFile = "add_item.json"
my_json_list = []

if os.path.exists(myFile):
    my_json_list = load_from_json(myFile)
for i in argv[1:]:
    my_json_list.append(i)
save_to_json(my_json_list, myFile)
