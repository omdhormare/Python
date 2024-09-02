import mysql.connector as mc
con=mc.connect(host="localhost",password="root",username="root",database="collage")

db=con.cursor()

db.execute("create table collage(cno int,cname varchar(20),address varchar(20))")
print("Succefully Create Table...")