def count_words():
    counter = 0
    with open("ABC.txt", "r") as file:
        data = file.read()
        print("Contents of Text File:")
        print("="*25)
        print(data)
        print("="*25)
        for line in data.split("\n"):
            for word in line.split(" "):
                if word[:3].lower() == "the":
                    counter += 1
    print("Number of words containing starting with 'the' is:", counter)

count_words()