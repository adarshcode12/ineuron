import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost",database = "Students",user="root", passwd="mysql",use_pure=True)

    query = "INSERT INTO Studentdetails VALUES (019,'abh','2022-03-26')"

    cursor = mydb.cursor()
    cursor.execute(query)
    print("Insert into Table;")
    mydb.commit()

except Exception as e:
    mydb.close()
    print(str(e))