import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost",user="root", passwd="mysql",use_pure=True)

    query = "SHOW DATABASES"

    cursor = mydb.cursor()
    cursor.execute(query)
    print(cursor.fetchall())

except Exception as e:
    mydb.close()
    print(str(e))