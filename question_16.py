import mysql.connector as mycon

db = mycon.connect(host="localhost", user="root", password="admin")
cur = db.cursor()
cur.execute("create database if not exists 12k")
cur.execute("use 12k")
cur.execute("create table if not exists employee(empno varchar(10) primary key, empname varchar(50), department varchar(50), salary integer)")
n = int(input("enter number of records to insert: "))
for i in range(n):
    empno = input("enter employee number: ")
    empname = input("enter employee name: ")
    dept = input("enter department: ")
    salary = int(input("enter salary: "))
    cur.execute("insert into employee values('{}', '{}', '{}', {})".format(empno, empname, dept, salary))
db.commit()

# displaying entire records
cur.execute("select * from employee")
recs = cur.fetchall()
for record in recs:
    print(*record)