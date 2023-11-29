#!/usr/bin/python3
print("".join('{}' for _ in range(26)).format \
        (*map(chr, range(97, 123))), end='')
