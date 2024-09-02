import mysql.connector as mc

con=mc.connect(host="localhost",password="root",username="root")
if con.is_connected():
    print("Connected")
else:
    print("Not Connected")