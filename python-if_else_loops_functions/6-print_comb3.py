#!/usr/bin/python3
for n in range(10):
    for x in range(10):
        if x > n:
            if n == 8 and x == 9:
                print("89")
            else:
                print("{}{}, ".format(n, x), end="")

