#!/usr/bin/python3
for number in range(0, 100):
    if number < 10:
        print("0{:d}".format(number), end=', ')
    elif number == 99:
        print("{:d}".format(number))
    else:
        print("{:d}".format(number), end=', ')
