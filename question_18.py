import mysql.connector as mycon

db = mycon.connect(host="localhost", user="root", password="arya")
cur = db.cursor()
cur.execute("use 12k")
empno = input("Enter employee number of employee you want to update records of: ")
cur.execute("select * from employee where empno = '{}'".format(empno))

recs = cur.fetchall()[0]
if cur.rowcount != 0:
    new_dept = input("Enter New Department (keep blank if no change): ")
    if new_dept == "":
        new_dept = recs[2]
    new_salary = int(input("enter new salary (keep blank if no change): "))
    if new_salary == "":
        new_salary = recs[3]
    cur.execute("update employee set department = '{}' where empno = '{}'".format(new_dept, empno))
    cur.execute("update employee set salary = {} where empno = '{}'".format(new_salary, empno))
    db.commit()
    # printing updated details
    cur.execute("select * from employee where empno = '{}'".format(empno))
    rec = cur.fetchall()[0]
    print(*rec)
