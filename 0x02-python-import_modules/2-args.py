#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) == 1:
        print("0 arguments.")
    elif len(args) == 2:
        print("{} argument: ".format(len(args) - 1))
        print("1: {}".format(args[1]))
    else:
        print("{} arguments:".format(len(args) - 1))
        for i in range(1, len(args)):
            print("{}: {}".format(i, args[i]))
