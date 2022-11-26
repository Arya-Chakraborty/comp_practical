import csv
with open("patient.csv", "r") as file:
    data = list(csv.reader(file))
    print(data[0])
    for i in data[1:][::-1]:
        print(*i)