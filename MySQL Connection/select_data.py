import mysql.connector as mc

con=mc.connect(host="localhost",username="root",password="root",database="collage")

db=con.cursor()

db.execute("select * from collage")

res=db.fetchall()

for i in res:
    print(i)