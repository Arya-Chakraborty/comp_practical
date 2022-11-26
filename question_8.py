import pickle


def add_record():
    with open("Student.dat", "wb") as file:
        L = []
        turns = 0
        while turns < 3:
            rollNo = int(input("Roll: "))
            name = (input("name: "))
            marks = int(input("marks: "))
            pickle.dump([rollNo, name, marks], file)
            turns += 1

# add_record()

def update_record(rollNo):
    with open("Student.dat", "rb") as file:
        lisOfRows = []
        while True:
            try:
                row = pickle.load(file)
                lisOfRows.append(row)
            except EOFError:
                break
    with open("Student.dat", "wb") as file:
        for row in lisOfRows:
            if int(row[0]) == rollNo:
                new_marks = int(input("New marks:"))
            else:
                new_marks = row[2]
            pickle.dump([row[0], row[1], new_marks], file)
add_record()
update_record(2)
with open("Student.dat", "rb") as file:
    while True:
        try:
            print(pickle.load(file))
        except EOFError:
            break