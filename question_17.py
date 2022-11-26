import mysql.connector as mycon

db = mycon.connect(host="localhost", user="root", password="admin")
cur = db.cursor()
cur.execute("use 12k")
empno = input("enter empno to search for records: ")
cur.execute("select * from employee where empno = '{}'".format(empno))
if cur.rowcount == 0:
    print("No records Found")
else:
    recs = cur.fetchall()
    for record in recs:
        print(*record)
