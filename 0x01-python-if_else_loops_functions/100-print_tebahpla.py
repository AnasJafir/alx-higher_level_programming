#!/usr/bin/python3
for i in range(122, 96, -1):
        if i % 2 == 0:
            alpha = chr(i)
        else:
            alpha = chr(i - 32)
        print("{}".format(alpha), end='')
