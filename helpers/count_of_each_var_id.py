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

# the SQL query from where we get the data
query = "SELECT Var_Id, COUNT(*) as count FROM Execution GROUP BY Var_Id"

cursor.execute(query)
con.commit()

# fetchall() retrieves all the rows returned by the SQL query 
# The executionData variable stores the result returned by cursor.fetchall().
executionData = cursor.fetchall()

# printing executionData
print(executionData)