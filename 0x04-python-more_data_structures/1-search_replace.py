#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_newList = []

    for i in my_list:
        if search == i:
            i = replace
        my_newList.append(i)
    return my_newList
