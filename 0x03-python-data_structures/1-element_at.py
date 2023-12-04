#!/usr/bin/python3

def element_at(my_list, idx):
    total_elements = len(my_list)
    if idx < 0 or idx > total_elements:
        return None
    return my_list[idx]
