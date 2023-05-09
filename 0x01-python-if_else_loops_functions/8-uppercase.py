#!/usr/bin/python3
def convert_char_to_uper(character):
    if ord(character) >= 97 and ord(character) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)


def convert_string_uppercase(str):
    new = ""
    for character in str:
        new += "%c" % to_uper(character)
    print("{:s}".format(new))
