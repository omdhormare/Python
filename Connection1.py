import mysql.connector 

mc=mysql.connector

con = mc.connect(host="localhost", user="root", password="root",database="student")
if con.is_connected():
    print("Successfully Connected...")

db=con.cursor()
db.execute("insert into student values(1,'om',90)")
#db.execute("insert into student values(2,'omkar',85)")

db.execute("delete from student where rno=1")
db.execute("UPDATE student SET name='om' WHERE rno=2 ")

con.commit()
#con.commit()
print("Table create Succesfully...")