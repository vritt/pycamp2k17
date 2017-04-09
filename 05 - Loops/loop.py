string = "I am Learning Python"

numbers = range(1, 10)
print(list(numbers))
for x in numbers:
    if x == 5:
        continue
    if x == 8:
        break
    print(x)
