import mysql.connector as mycon

db = mycon.connect(host="localhost", user="root", password="arya")
cur = db.cursor()
cur.execute("use 12k")
empno = input("enter employee number of employee who want to delete records of: ")
cur.execute("select * from employee where empno = '{}'".format(empno))
rec = cur.fetchall()[0]
if cur.rowcount == 0:
    print("No records found")
else:
    print(*rec)
    ch = input("Please confirm you want to delete this record (y/n): ")
    if ch.lower() == "n":
        print("record not deleted")
    elif ch.lower() == "y":
        cur.execute("delete from employee where empno = '{}'".format(empno))
        db.commit()
        print("record deleted successfully")
    