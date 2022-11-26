def letterCount(string):
    l = []
    string = string.lower()
    for i in string:
        if i not in l:
            l.append(i)
    l.sort()
    print("="*30)
    print("Alphabet \t Frequency")
    print("="*30)
    for i in l:
        print(i,"\t",string.count(i))
letterCount(input("Enter string: "))