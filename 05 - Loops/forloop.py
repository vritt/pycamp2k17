#!/usr/bin/python3.4


with open('lines.txt') as file:
    for line in file.readlines():
        print(line, end="")
