#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) == 1:
        print("0 arguments.")
    elif len(args) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(args) - 1))
    for i in range(len(args) - 1):
            print("{}: {}".format(i + 1, args[i + 1]))
