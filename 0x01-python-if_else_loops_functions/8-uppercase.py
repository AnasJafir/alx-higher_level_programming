#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        character = ord(str[i])
        if character >= 97 and character <= 122:
            character = character - 32
        print("{}".format(chr(character)), end="")
    print()
