import tkinter as tk
import mysql.connector

# Establishing the connection to the MySQL database
con = mysql.connector.connect(host="localhost", user="root", password="Acro@12")
cur = con.cursor(buffered=True)

# Create database if it does not exist
try:
    cur.execute("CREATE DATABASE IF NOT EXISTS registration")
    cur.execute("USE registration")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Create table if it does not exist
try:
    cur.execute("CREATE TABLE IF NOT EXISTS persons ("
                "id INT PRIMARY KEY AUTO_INCREMENT, "
                "name VARCHAR(99), "
                "age INT, "
                "gender VARCHAR(5), "
                "email VARCHAR(30), "
                "mobile VARCHAR(10))")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Function to handle the registration process
def Registration():
    try:
        cur.execute("INSERT INTO persons (name, age, gender, email, mobile) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (e1.get(), e2.get(), e3.get(), e4.get(), e5.get()))
        con.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()

# Creating the GUI
win = tk.Tk()
win.geometry("500x500")
win.title("Person Registration Portal")

l1 = tk.Label(win, text="Person details")
l2 = tk.Label(win, text="Name")
l3 = tk.Label(win, text="Age")
l4 = tk.Label(win, text="Gender")
l5 = tk.Label(win, text="Email")
l6 = tk.Label(win, text="Mobile Number")

l1.grid(row=0, column=1)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
l4.grid(row=3, column=0)
l5.grid(row=4, column=0)
l6.grid(row=5, column=0)

e1 = tk.Entry(win)
e2 = tk.Entry(win)
e3 = tk.Entry(win)
e4 = tk.Entry(win)
e5 = tk.Entry(win)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)

b = tk.Button(win, text="Submit Here", command=Registration)
b.grid(row=7, column=1)

win.mainloop()

# Closing the connection to the database
cur.close()
con.close()
