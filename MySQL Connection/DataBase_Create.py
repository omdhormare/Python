import mysql.connector as mc
con=mc.connect(host="localhost",password="root",username="root")

db=con.cursor()
db.execute("create database collage")
print("Create Database..")

