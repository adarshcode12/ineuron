import mysql.connector as connection
import pandas as pd


mydb = connection.connect(host="localhost",database = "Students",user="root", passwd="mysql",use_pure=True)
pd.read_sql_query("select * from Students.Studentdetails",mydb)

