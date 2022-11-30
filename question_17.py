import mysql.connector as mycon

db = mycon.connect(host="localhost", user="root", password="arya")
cur = db.cursor()
cur.execute("use 12k")
empno = input("enter empno to search for records: ")
cur.execute("select * from employee where empno = '{}'".format((empno)))
recs = cur.fetchall()
if cur.rowcount == 0:
    print("No records Found")
else:
    for record in recs:
        print(*record)
