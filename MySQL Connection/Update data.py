import mysql.connector as mc

con=mc.connect(host="localhost",username="root",password="root",database="collage")

db=con.cursor()
db.execute("update collage set address='Nagar' where cno=2 ")

con.commit()
print("Update Succefully")
