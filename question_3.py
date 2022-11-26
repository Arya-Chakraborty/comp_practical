counter = 0
with open("DIGIT.txt", "r") as file:
    data = file.read()
    print("="*25)
    print(data)
    print("="*25)
    for line in data.split("\n"):
        for char in line:
            if char.isdigit():
                counter += 1
print("Number of characters in file:", counter)