dic = dict(
    one=1, two=2, three=3
)
print(dic)

for x in sorted(dic.values()):
    print(x)

dic2 = {'one1': 4, 'three1': 8}
dic.update(dic2)
print(dic)
