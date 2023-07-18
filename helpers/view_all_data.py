# import required libraries
import json
import pandas as pd
from sklearn.ensemble import IsolationForest
import pyodbc
import joblib

# database connection
con = pyodbc.connect(driver='{ODBC Driver 18 for SQL Server}',
                     server='dev-o3.public.090962170979.database.windows.net,3342',
                     database='UATO3UtilityDB',
                     uid='NKU_USER', pwd='*NKU_USER1278*')

print('starting')

cursor = con.cursor()
con.autocommit = True

# Replace the stored procedure with the SQL query
query = "SELECT * FROM Execution"

cursor.execute(query)
con.commit()

# fetchall() retrieves all the rows returned by the SQL query 
# The executionData variable stores the result returned by cursor.fetchall().
executionData = cursor.fetchall()

# printing the top 2 tuples/rows. [:2] denotes selection of rows from the first (0) 
# up to and excluding row 2 (the third row since indexing starts from 0)
# print(executionData[:2])

print(type(executionData[0][5]))
