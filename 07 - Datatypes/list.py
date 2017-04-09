mylist = [1, 2, 3, "hi", "new"]
newlist = [8, 9, 7]
# print(dir(mylist))
print("Start list", mylist)

for x in mylist:
    print(x)

mylist.append(8)
mylist.insert(2, 8)
print("New list", mylist)

thirtdlist = mylist + newlist

print(thirtdlist)
