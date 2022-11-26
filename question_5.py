words = []
def display_words():
    with open("DATA.txt", "r") as file:
        data = file.read()
        print("Contents of the file:")
        print("="*25)
        print(data)
        print("="*25)
        for line in data.split("\n"):
            for word in line.split(" "):
                if len(word) < 4:
                    words.append(word)
    distinct_words = []
    for word in words:
        if word not in distinct_words and word != "":
            distinct_words.append(word)
    print("Words less than 4 characters long are:", distinct_words)

display_words()