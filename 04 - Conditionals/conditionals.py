#!/usr/bin/python3.4

a, b = 0, 2

a += 1

a = a + 1

if a < b and a > b:
    print("a {} is less than b {}.".format(a, b))
else:
    print("a {} is greater than b {}.".format(a, b))
