dic1 = dict(eval(input("Dictionary 1: ")))
dic2 = dict(eval(input("Dictionary 2: ")))

dic3 = {}
for elem in dic1:
    if elem in dic2 and elem not in dic3:
        dic3[elem] = abs(dic1[elem] - dic2[elem])
print(dic3)