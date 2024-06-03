import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Acro@12",
  database="Learncode"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM demo")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


