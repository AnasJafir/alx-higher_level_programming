#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    a = len(args) - 1
    if a == 0:
        print("0 arguments.")
    elif a == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(a))
    for i in range(a):
            print("{}: {}".format(i + 1, args[i + 1]))
