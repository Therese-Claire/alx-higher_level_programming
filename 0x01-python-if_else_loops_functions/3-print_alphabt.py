#!/usr/bin/python3
print("".join('{}' for _ in range(24)).format(
    *[chr(i) for i in range(97, 123) if chr(i) not in ['q', 'e']]),
     end= '')
