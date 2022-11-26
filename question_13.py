def duplicates(lis):
    dup = []
    for elem in lis:
        if lis.count(elem) > 1 and elem not in dup:
            dup.append(elem)
    return dup

lis = list(eval(input("Original List: ")))
print("Duplicates:", duplicates(lis))