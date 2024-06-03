import mysql.connector as myconn

mydb=myconn.connect(host="localhost",user="root",password="Acro@12")

db_cursor=mydb.cursor()

db_cursor.execute("create database LearnCode")
print("database created done...")