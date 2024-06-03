""" insert data in table for MYSQL"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Acro@12",
  database="LearnCode"
)

mycursor = mydb.cursor()

sql = "INSERT INTO demo (FastName , LastName ,address ) VALUES (%s, %s,%s)"
val = ("Ashish","pal","341 vijay nagar indore")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")