#!/usr/bin/python3
for i in range(ord("a"), ord("z") + 1):
    if chr(i) != "e" and chr(i) != "q":
        print("{:s}".format(chr(i)), end="")
