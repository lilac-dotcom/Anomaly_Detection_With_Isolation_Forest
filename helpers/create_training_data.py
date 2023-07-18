import pandas as pd
import pyodbc
import warnings

warnings.filterwarnings('ignore')

# database connection 
con = pyodbc.connect(driver='{ODBC Driver 18 for SQL Server}',
                     server='dev-o3.public.090962170979.database.windows.net,3342',
                     database='UATO3UtilityDB',
                     uid='NKU_USER', pwd='*NKU_USER1278*')

print('starting')

cursor = con.cursor()
con.autocommit = True

# TRAINING DATA LOADING.
# SQL queries which we use to fetch the live data, and creating their respective dataframes for every range we need in the training dataset.
# TODO: further split optimal range into parts and create training data accordingly
query_get_all_inliers = "SELECT Result, Result_On, Var_Id FROM Execution WHERE Var_Id = 340 and CAST( [Result] AS FLOAT) between 1000 and 1900"
inliers_df = pd.read_sql_query(query_get_all_inliers, con)

query_outliers_0_10 = "SELECT TOP 6 Result, Result_On, Var_Id FROM Execution WHERE Var_Id = 340 and CAST( [Result] AS FLOAT) between 0 and 10 ORDER BY NEWID()"
outliers_0_10_df = pd.read_sql_query(query_outliers_0_10, con)

query_outliers_10_20 = "SELECT TOP 9 Result, Result_On, Var_Id FROM Execution WHERE Var_Id = 340 and CAST( [Result] AS FLOAT) between 10 and 20 ORDER BY NEWID()"
outliers_10_20_df = pd.read_sql_query(query_outliers_10_20, con)

query_outliers_20_272 = "SELECT TOP 1 Result, Result_On, Var_Id FROM Execution WHERE Var_Id = 340 and CAST( [Result] AS FLOAT) between 20 and 272 ORDER BY NEWID()"
outliers_20_272_df = pd.read_sql_query(query_outliers_20_272, con)

query_outliers_272_500 = "SELECT TOP 5 Result, Result_On, Var_Id FROM Execution WHERE Var_Id = 340 and CAST( [Result] AS FLOAT) between 272 and 500 ORDER BY NEWID()"
outliers_272_500_df = pd.read_sql_query(query_outliers_272_500, con)

query_outliers_500_1000 = "SELECT TOP 3 Result, Result_On, Var_Id FROM Execution WHERE Var_Id = 340 and CAST( [Result] AS FLOAT) between 500 and 1000 ORDER BY NEWID()"
outliers_500_1000_df = pd.read_sql_query(query_outliers_500_1000, con)

query_outliers_1900_2000 = "SELECT TOP 3 Result, Result_On, Var_Id FROM Execution WHERE Var_Id = 340 and CAST( [Result] AS FLOAT) between 1900 and 2000 ORDER BY NEWID()"
outliers_1900_2000_df = pd.read_sql_query(query_outliers_1900_2000, con)

# concatenation of dataframes.
# List of dataframes
lst_of_df = [inliers_df, outliers_0_10_df, outliers_10_20_df, outliers_20_272_df, outliers_272_500_df, outliers_500_1000_df, outliers_1900_2000_df] 
training_data_df = pd.concat(lst_of_df, ignore_index=True)

# shuffle the df
training_data_df = training_data_df.sample(frac=1, random_state=1)

# convert Result column to float
training_data_df['Result'] = training_data_df['Result'].astype(float)

# print(training_data_df)

# sending the training data to a csv file
training_data_csv_path = 'C:/Users/Computer Arena/Desktop/Qandeel_NKU/Qandeel_ML/training_ppanda/csv_tables/from_helpers/training_data.csv'
training_data_df.to_csv(training_data_csv_path, columns=['Result', 'Result_On', 'Var_Id'])
print('training data sent to csv file.')