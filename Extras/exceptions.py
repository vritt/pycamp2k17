#!/usr/bin/python3.4

try:
    file = open('lines.txt')

    for line in file.readlines():
        print(line, end="")

except Exception as e:
    print(e)

print("We are done.")
