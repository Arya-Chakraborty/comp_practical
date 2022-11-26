import csv
with open("patient.csv", "r") as file:
    data = list(csv.reader(file))
    print(*data[0])
    for row in data[1:]:
        if int(row[4]) > 250 and int(row[3]) < 125:
            print(*row)
