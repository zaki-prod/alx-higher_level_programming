#!/usr/bin/python3
# function that prints the number and thier hexadecimal equivalents
for i in range(100):
    print("{} {}".format(i, hex(i)[2:].upper()))
