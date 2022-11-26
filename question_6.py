import pickle
def add_record():
    with open("EMPLOYEE.dat", "ab") as file:
        empno = input("Enter Employee number:")
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        salary = int(input("Enter Salary: "))
        rec = [empno, name, address, salary]
        pickle.dump(rec, file)
    with open("EMPLOYEE.dat", "rb") as file:
        print("Contents of the File:")
        while True:
            try:
                print(pickle.load(file))
            except EOFError:
                break

add_record()