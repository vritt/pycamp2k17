#!/usr/bin/python3.4


class Fibonacci(object):
    """description for Fibonacci"""

    def __init__(self, limit):
        self.limit = limit

    def generate(self):
        a, b = 0, 1
        while b < self.limit:
            yield b
            a, b = b, a + b

fib = Fibonacci(150)

for number in fib.generate():
    print(number, end=" ")
print("Done")
