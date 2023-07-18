import pandas as pd
import pyodbc

# database connection
con = pyodbc.connect(driver='{ODBC Driver 18 for SQL Server}',
                     server='dev-o3.public.090962170979.database.windows.net,3342',
                     database='UATO3UtilityDB',
                     uid='NKU_USER', pwd='*NKU_USER1278*')

print('starting')

cursor = con.cursor()
con.autocommit = True

# the SQL query from where we get the data. Modify Var_Id to get the count of decimals in required Var_Id.
query = "SELECT Result, Result_On, Var_Id FROM Execution WHERE Var_Id = 341"

# Read query data from DB into a pandas dataframe
df = pd.read_sql_query(query, con)

# commit changes made within transaction to DB.
con.commit()

# Calculate the number of decimal points in each number
decimal_counts = df['Result'].apply(lambda x: len(str(x).split('.')[-1]))

# Count the number of rows for each distinct decimal count
count_per_decimal = decimal_counts.value_counts()

print(count_per_decimal)
