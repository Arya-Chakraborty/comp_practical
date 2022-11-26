import pickle

def add_record():
    with open("STUDENT.dat", "wb") as file:
        L = []
        turns = 0
        while turns < 2:
            rollNo = int(input("Roll: "))
            name = (input("name: "))
            clss = int(input("class: "))
            section = (input("section: "))
            mobile = (input("mobile: "))
            marks = int(input("marks: "))
            pickle.dump([rollNo, name, clss, section, mobile, marks], file)
            turns += 1
# add_record()

def delete_record(rollno):
    with open("STUDENT.dat", "rb") as file:
        lisOfRows = []
        while True:
            try:
                row = pickle.load(file)
                lisOfRows.append(row)
            except EOFError:
                break
    target, data = False, None
    for row in lisOfRows:
        if int(row[0]) == rollno:
            lisOfRows.remove(row)
            target, data = True, row
    with open("STUDENT.dat", "wb") as file:
        for row in lisOfRows:
            pickle.dump(row, file)
        if target == False:
            print("No data Found")
        else:
            print("Data Deleted: ", data)

delete_record(1)