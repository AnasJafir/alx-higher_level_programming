#!/usr/bin/python3
for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        number = digit1 * 10 + digit2
        if number == 89:
            print("{:02d}".format(number))
        else:
            print("{:02d}".format(number), end=", ")
