import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Acro@12",
    database="LearnCode"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE demo (User_ID INT NOT NULL AUTO_INCREMENT, FastName VARCHAR(255), LastName VARCHAR(99), address VARCHAR(255), PRIMARY KEY (User_ID))")

print("Table created successfully!")
