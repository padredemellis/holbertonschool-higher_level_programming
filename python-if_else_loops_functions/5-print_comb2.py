#!/usr/bin/python3
for n in range(0, 100):
    print("{:02}".format(n), "{}".format(" "), sep=",", end="")
    if (n == 99):
        print("{}".format(n))
