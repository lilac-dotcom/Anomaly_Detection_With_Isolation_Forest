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
query = "SELECT DISTINCT Var_Id FROM Execution"

cursor.execute(query)
con.commit()

# fetchall() retrieves all the rows returned by the SQL query 
# The executionData variable stores the result returned by cursor.fetchall().
executionData = cursor.fetchall()

# printing executionData
print(executionData)

# Expected output should be something like the following format: starting
# [(306,), (340,), (341,), (509,), (510,), (519,), (308,), (355,), (422,), (372,), (444,), (494,), (529,), (301,), (421,), (522,)]
# The 𝗰𝗼𝗺𝗺𝗮𝘀 𝗶𝗻𝘀𝗶𝗱𝗲 𝘁𝗵𝗲 𝗽𝗮𝗿𝗲𝗻𝘁𝗵𝗲𝘀𝗲𝘀 𝗶𝗻𝗱𝗶𝗰𝗮𝘁𝗲 that 𝘁𝗵𝗲𝘀𝗲 𝘃𝗮𝗹𝘂𝗲𝘀 𝗮𝗿𝗲 𝘀𝘁𝗼𝗿𝗲𝗱 𝗮𝘀 𝘁𝘂𝗽𝗹𝗲𝘀.
