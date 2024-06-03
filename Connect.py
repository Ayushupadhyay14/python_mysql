import mysql.connector as myconn

mydb=myconn.connect(host="localhost",user="root",password="Acro@12")

print(mydb,"Connection Etrablisted")

