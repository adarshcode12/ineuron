#!/usr/bin/env python
# coding: utf-8

# In[12]:


import mysql.connector as connection
import pandas as pd

mydb = connection.connect(host="localhost",database = "Students",user="root", passwd="mysql",use_pure=True)
a=pd.read_sql_query("select * from Students.Studentdetails",mydb)
a.to_csv('mydata.csv')


# In[13]:


cursor = mydb.cursor()
data=pd.read_sql('mydata.csv')
data.to_sql('Studentdetails',con='mydb')


# In[ ]:





# In[ ]:




