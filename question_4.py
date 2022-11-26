def transfer_lines():
    new_lines = []
    with open("ORIGIN.txt", "r") as file:
        data = file.read()
        print("Contents of ORIGIN.txt are:")
        print(data)
        print("="*25)
        for line in data.split("\n"):
            if line[0].lower() in "aeiou":
                new_lines.append(line)
    with open("NEW.txt", "w+") as file:
        file.writelines(new_lines)
    with open("NEW.txt", "r") as file:
        data = file.read()
        print("Contents of NEW.txt are:")
        print(data)
        print("="*25)

transfer_lines()