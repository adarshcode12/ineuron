from django.db import DatabaseError
import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost",database = "Students",user="root", passwd="mysql",use_pure=True)

    query = "CREATE TABLE Studentdetails (Studentid INT(6) PRIMARY KEY ,Name VARCHAR(30), date DATE) "

    cursor = mydb.cursor()
    cursor.execute(query)
    print("table created;")

except Exception as e:
    mydb.close()
    print(str(e))