counter = 0
with open("ABC.txt", "r") as file:
    data = file.read()
    print("Contents of File:")
    print("="*25)
    print(data)
    print("="*25)
    for line in data.split("\n"):
        if line[-1].lower() == "a":
            counter += 1
print("The number of lines ending with 'a' is:", counter)