import csv
with open("patient.csv", "r") as file:
    data = list(csv.reader(file))
    print(*data[0])
    for row in data[1:]:
        if (row[0][0].lower() == "o" or row[0][-1].lower() == "r") and int(row[1]) > 70:
            print(*row)