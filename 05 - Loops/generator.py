#!/usr/bin/python3.4


def generateFibonacii(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b

for number in generateFibonacii(50):
    print(number)
