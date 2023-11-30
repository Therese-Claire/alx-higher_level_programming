#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    sorted_names = sorted(defined_name for defined_name in names
            if not defined_name.startswith("__"))
    for defined_name in sorted_names:
        print(defined_name)
