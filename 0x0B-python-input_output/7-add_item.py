#!/usr/bin/python3
"""Script that loads, adds, and save arguments to a Python list"""
from sys import argv

load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file


try:
    list_ = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    list_ = []

for item in argv[1:]:
    list_.append(item)

save_file(list_, 'add_item.json')
