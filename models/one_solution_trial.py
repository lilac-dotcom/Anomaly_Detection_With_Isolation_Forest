# importing pandas and Isolation forest algorithm from scikit-learn
import json
import pandas as pd
from sklearn.ensemble import IsolationForest
import pyodbc

# creating a python list and naming it dataArr
dataArr = [1,2,3,4,105,6]

#dbConnection
con = pyodbc.connect(driver='{ODBC Driver 18 for SQL Server}',
                     server='dev-o3.public.090962170979.database.windows.net,3342',
                     database='UATO3UtilityDB',
                     uid='NKU_USER', pwd='*NKU_USER1278*')

print('starting')

cursor = con.cursor()
con.autocommit = True
sp = "SET NOCOUNT ON; exec sp_Execution_GetDailyExecutionDataTEST"
cursor.execute(sp)
con.commit()

executionData = cursor.fetchall()

# data is column
for data in executionData:
    data[2] = json.loads(data[2])
    break

#iterate over first dimension to traverse between rows, second dimension is for result column (col with index 2) 
firstRowResult = executionData[2][2]

resArr = []

for data in firstRowResult:
    resArr.append(data['Result'])
    
print(resArr)

# loading data into dataframe object called data. "dataArr" as the data parameter. columns takes an array-like of column label(s) 
# to use for resulting frame when data does not have them. in this case we have one column label called numbers.
# for indexing on resulting frame: Will default to RangeIndex if no indexing information part of input data and no index provided.
data = pd.DataFrame(dataArr, columns=['numbers'])

# (not sure): we pass columns to a variable called features
features = ['numbers'] # TODO: try replacing 'numbers' with "numbers" in this line to see if code still works (UPDATE: it works)

# selecting the numbers column (using features to refer to it), which produces a Series (One-dimensional ndarray with axis labels) 
# and passing it to variable called x.
# x now contains the numbers column label + data
# (maybe): data already contains the data + column label. 
x = data[features]

# using isolation forest algorithm, with contamination at 0.01. 
# storing it in model variable for reference
# contamination is the amount of contamination of the data set, i.e. the proportion of outliers in the data set. data is in dataArr
# If float, the contamination should be in the range (0, 0.5).
# (not sure): why is contamination set at 0.01 when 1/6 is 0.1666666666666667?
model = IsolationForest(contamination=0.01)

# "In a nutshell: fitting is equal to training." - stack overflow
# fit() method takes the [training] data as arguments, which can be one array in the case of unsupervised learning, 
# or two arrays in the case of supervised learning. 
# our case is unsupervised learning
# (probably): we are training the model
model.fit(x)

# decision_function(X): Average anomaly score of X of the base classifiers. - https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html
# we are finding Average anomaly score of x, and storing it in scores variable
# (not sure): what is base classifier?
scores = model.decision_function(x)

# we store 0.1 in a variable called threshold
threshold = 0.1

# (property) DataFrame.iloc[source]: Purely integer-location based indexing for selection by position. - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc
# Dataframe.iloc[] method is used when the index label of a data frame is something other than numeric series of 0, 1, 2, 3….n 
# or in case the user doesn’t know the index label.
# The syntax of the iloc function in Python is as follows: df.iloc[row_start:row_end, column_start:column_end] - https://www.prepbytes.com/blog/python/iloc-function-in-python/
# in the iloc method, we are comparing scores vs threshold. when scores (Average anomaly score) is less than threshold, we select those rows
# and store it in a variable called anomalies. These rows are considered anomalies based on the given threshold.
anomalies = data.iloc[scores < threshold]

# if the length of anomalies variable is 0, it means no rows were selected and there are hence no anomalies.
if len(anomalies) == 0:
    print("No Anomaly") # we give print statement with msg

# in the other case (length of anomalies variable is not 0), it means atleast 1 row was selected. hence there was atleast 1 anomaly.
else:
    print(anomalies) # we print the anomalies (the rows that were selected)
    
# eg: if the output is:
# numbers
# 4      105
# it means that it is showing us a numbers column containing the row that was the anomaly. 4 is its index and 105 is the value