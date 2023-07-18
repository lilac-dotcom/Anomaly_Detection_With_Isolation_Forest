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
sp = "SET NOCOUNT ON; exec sp_execution_detail_0_299"
cursor.execute(sp)
con.commit()

# fetchall() retrieves all the rows returned by the stored procedure execution in the "sp_execution_detail"
# stored procedure. 
# The executionData variable stores the result returned by cursor.fetchall().
# executionData is a list of tuples.
executionData = cursor.fetchall()

# create empty lists to store the extracted rows into respective columns
var_id = []
result_on = []
result = []

# # printing the first tuple/row
# print(executionData[0])

# iterate over each tuple/row in the executionData list
for row in executionData:
    # for every row, append the value for each required column into its respective column variable
    var_id.append(row[0])
    result_on.append(row[1].timestamp())  # Convert datetime to timestamp
    result.append(int(row[2]))  # Convert the value to integer using int()
    
print(result)

# # Combine the variables into a dictionary
# executionDict = {
#     'Var_Id': var_id,
#     'Result_On': result_on,
#     'Result': result
# }

# # Convert the dictionary to a pandas DataFrame
# df = pd.DataFrame(executionDict)

# # print the dataset just to check the data
# print(" \n \n the dataset is: \n \n", df)

# # declare model TODO: explore contamination value
# model = IsolationForest(contamination=0.1)

# # train it on the data
# model.fit(df)
# print("\n \n -> model trained successfully.")

# # # save the model
# # joblib.dump(model, 'saved_model\model0\isolation_forest_model.pkl')
# # print(" \n -> model saved successfully.")

# # finding the average anomaly score of X of the base classifiers.
# # The anomaly score of an input sample is computed as the mean anomaly score of the trees in the forest.
# anomaly_score = model.decision_function(df)

# # set a threshold TODO: explore threshold value
# threshold = 0.1

# # select rows that fit anomaly criteria
# anomalies = df.iloc[anomaly_score < threshold]

# # if anomalies is empty, no anomaly
# if len(anomalies) == 0:
#     print("no anomaly")

# # otherwise print anomaly
# else:
#     print(" \n \n anomaly/anomalies detected are: \n \n", anomalies)

# print(len(anomalies))