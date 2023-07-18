import numpy as np
from sklearn.ensemble import IsolationForest
import pyodbc
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import warnings
import os

num_epochs = 20

# path to where the model will be saved
saved_model_path = "C:/Users/Computer Arena/Desktop/Qandeel_NKU/Qandeel_ML/training_ppanda/saved_model/one_solution/isolation_forest_model.pkl"

warnings.filterwarnings('ignore')

# variables for paths to epoch counters used in both training and validation. 
# delete these counter files if wanting to start the process from scratch
epoch_train_count_path = "C:/Users/Computer Arena/Desktop/Qandeel_NKU/Qandeel_ML/training_ppanda/helpers/epoch_train_count.txt"
epoch_validate_count_path = "C:/Users/Computer Arena/Desktop/Qandeel_NKU/Qandeel_ML/training_ppanda/helpers/epoch_validate_count.txt"

# to keep track of epochs during training/validation. 𝗖𝗛𝗔𝗡𝗚𝗘 𝗧𝗛𝗘 𝗘𝗣𝗢𝗖𝗛 𝗣𝗔𝗧𝗛 𝗩𝗔𝗥𝗜𝗔𝗕𝗟𝗘 according to which stage you are in
# Check if count file exists
if os.path.exists(epoch_validate_count_path): # 𝗰𝗵𝗮𝗻𝗴𝗲 𝗽𝗮𝘁𝗵 𝘃𝗮𝗿𝗶𝗮𝗯𝗹𝗲 𝗶𝗳 𝗻𝗲𝗲𝗱𝗲𝗱
    # Read the current count from the file
    with open(epoch_validate_count_path, "r") as f: # 𝗰𝗵𝗮𝗻𝗴𝗲 𝗽𝗮𝘁𝗵 𝘃𝗮𝗿𝗶𝗮𝗯𝗹𝗲 𝗶𝗳 𝗻𝗲𝗲𝗱𝗲𝗱
        epoch_count = int(f.read())
else:
    # Initialize count if the file doesn't exist
    epoch_count = 0

# Training/Validation loop
for epoch in range(num_epochs):
    # Perform training steps
    def detect_anomalies(data): # 𝗤: 𝗽𝗿𝗲𝘃𝗶𝗼𝘂𝘀_𝗮𝗻𝗼𝗺𝗮𝗹𝘆_𝘀𝗰𝗼𝗿𝗲𝘀 is 
    # an 𝗼𝗽𝘁𝗶𝗼𝗻𝗮𝗹 𝗽𝗮𝗿𝗮𝗺𝗲𝘁𝗲𝗿 with a 𝗱𝗲𝗳𝗮𝘂𝗹𝘁 𝘃𝗮𝗹𝘂𝗲 of 𝗡𝗼𝗻𝗲.
    
        # model = IsolationForest(contamination=0.1) # 𝗨𝗦𝗘𝗗 𝗪𝗛𝗘𝗡 𝗧𝗥𝗔𝗜𝗡𝗜𝗡𝗚. COMMENT IF NOT TRAINING
        
        # Load the saved model using joblib. 
        model = joblib.load(saved_model_path) # 𝗨𝗦𝗘𝗗 𝗙𝗢𝗥 𝗩𝗔𝗟𝗜𝗗𝗔𝗧𝗜𝗢𝗡. COMMENT IF NOT VALIDATING
        
        anomaly_scores_list = []
    
        # Extract Var_Id and Result column data from the given data/df   
        Var_Id = df['Var_Id']
        
        # extracting their values to send to training
        result = df['Result'].values
        var_id = df['Var_Id'].values
    
        # convert Var_Id series to python list
        Var_Id_list = Var_Id.to_list()
        
        # Combine the columns into a 2D NumPy array
        data = np.column_stack((result, var_id))

        # # Fit the model to the Result data. 𝗨𝗦𝗘𝗗 𝗪𝗛𝗘𝗡 𝗧𝗥𝗔𝗜𝗡𝗜𝗡𝗚. 𝗖𝗢𝗠𝗠𝗘𝗡𝗧 𝗧𝗛𝗜𝗦 𝗜𝗙 𝗡𝗢𝗧 𝗧𝗥𝗔𝗜𝗡𝗜𝗡𝗚
        # model.fit(data)
        
        # # save the model to path. 𝗨𝗦𝗘𝗗 𝗪𝗛𝗘𝗡 𝗧𝗥𝗔𝗜𝗡𝗜𝗡𝗚. 𝗖𝗢𝗠𝗠𝗘𝗡𝗧 𝗧𝗛𝗜𝗦 𝗜𝗙 𝗡𝗢𝗧 𝗧𝗥𝗔𝗜𝗡𝗜𝗡𝗚
        # joblib.dump(model, saved_model_path)
        # print(" \n -> model saved successfully. \n \n ")
        
        # Predict the anomaly scores for the data
        anomaly_scores = model.decision_function(data)
    
        # Store the anomaly scores in the dictionary with varId as key and its respective scores
        anomaly_scores_dict = {'Var_Id': Var_Id_list, 'scores': anomaly_scores.tolist()}
        
        # append the dict to the list
        anomaly_scores_list.append(anomaly_scores_dict)

        return anomaly_scores_list
    
    # Increment epoch count
    epoch_count += 1
    
    # Print epoch count
    print("Epoch:", epoch_count)

# Save the updated count to the file
with open(epoch_validate_count_path, "w") as f: # 𝗰𝗵𝗮𝗻𝗴𝗲 𝗽𝗮𝘁𝗵 𝘃𝗮𝗿𝗶𝗮𝗯𝗹𝗲 𝗶𝗳 𝗻𝗲𝗲𝗱𝗲𝗱
    f.write(str(epoch_count))

# database connection 
con = pyodbc.connect(driver='{ODBC Driver 18 for SQL Server}',
                     server='dev-o3.public.090962170979.database.windows.net,3342',
                     database='UATO3UtilityDB',
                     uid='NKU_USER', pwd='*NKU_USER1278*')

print('starting')

cursor = con.cursor()
con.autocommit = True


# # 𝗧𝗥𝗔𝗜𝗡𝗜𝗡𝗚 𝗗𝗔𝗧𝗔 𝗟𝗢𝗔𝗗𝗜𝗡𝗚. 𝗰𝗼𝗺𝗺𝗲𝗻𝘁 𝘁𝗵𝗶𝘀 𝘀𝗲𝗰𝘁𝗶𝗼𝗻 𝘄𝗵𝗲𝗻 𝗻𝗼𝘁 𝘁𝗿𝗮𝗶𝗻𝗶𝗻𝗴/𝗻𝗼𝘁 𝘂𝘀𝗶𝗻𝗴 𝗹𝗶𝘃𝗲 𝗱𝗮𝘁𝗮 𝘁𝗼 𝘁𝗿𝗮𝗶𝗻
# # the SQL query from where we get the live data. Modify Var_Id to get the required Var_Id data.
# training_query = "SELECT CAST(Result AS FLOAT) AS Result, Result_On, Var_Id FROM Execution WHERE Var_Id = 340"
# # Read training query data from DB into a pandas dataframe. 
# df = pd.read_sql_query(training_query, con)
# # END OF TRAINING DATA LOADING


# # 𝗩𝗔𝗟𝗜𝗗𝗔𝗧𝗜𝗢𝗡 𝗗𝗔𝗧𝗔 𝗟𝗢𝗔𝗗𝗜𝗡𝗚. 𝗰𝗼𝗺𝗺𝗲𝗻𝘁 𝘁𝗵𝗶𝘀 𝘀𝗲𝗰𝘁𝗶𝗼𝗻 𝗶𝗳 𝗻𝗼𝘁 𝘃𝗮𝗹𝗶𝗱𝗮𝘁𝗶𝗻𝗴, 𝗼𝗿 𝗻𝗼𝘁 𝘃𝗮𝗹𝗶𝗱𝗮𝘁𝗶𝗻𝗴 𝘂𝘀𝗶𝗻𝗴 𝗹𝗶𝘃𝗲 𝗱𝗮𝘁𝗮
# query_340_low_outliers = "select Var_Id, Result_On, CAST(Result AS FLOAT) AS Result from Execution where Var_Id = 340 and Result < 1000.00"
# # query_341_low_outliers = "select Var_Id, Result_On, CAST(Result AS FLOAT) AS Result from Execution where Var_Id = 341 and Result < 1000.00"
# query_340_high_outliers = "select Var_Id, Result_On, CAST(Result AS FLOAT) AS Result from Execution where Var_Id = 340 and Result > 1900.00"
# # query_341_high_outliers = "select Var_Id, Result_On, CAST(Result AS FLOAT) AS Result from Execution where Var_Id = 341 and Result > 1900.00"

# df_340_low_outliers = pd.read_sql_query(query_340_low_outliers, con)
# # df_341_low_outliers = pd.read_sql_query(query_341_low_outliers, con)
# df_340_high_outliers = pd.read_sql_query(query_340_high_outliers, con)
# # df_341_high_outliers = pd.read_sql_query(query_341_high_outliers, con)

# # Using pandas.concat() to concat the two dataFrames of high and low outliers
# outliers_340 = [df_340_low_outliers, df_340_high_outliers]
# outliers_340_df = pd.concat(outliers_340)

# # outliers_341 = [df_341_low_outliers, df_341_high_outliers]
# # outliers_341_df = pd.concat(outliers_341)

# # # create dataframe for all outliers in variables no. 340 and 341
# # outliers = [outliers_340_df, outliers_341_df]
# # outliers_df = pd.concat(outliers)

# # Shuffle the outlier dataframe to create final dataframe for validation
# df = outliers_340_df.sample(frac=1, random_state=1)
# # END OF VALIDATION DATA LOADING


# # 𝗖𝗨𝗦𝗧𝗢𝗠 𝗧𝗥𝗔𝗜𝗡𝗜𝗡𝗚 𝗗𝗔𝗧𝗔 𝗟𝗢𝗔𝗗𝗜𝗡𝗚. 𝗰𝗼𝗺𝗺𝗲𝗻𝘁 𝘁𝗵𝗶𝘀 𝘀𝗲𝗰𝘁𝗶𝗼𝗻 𝘄𝗵𝗲𝗻 𝗻𝗼𝘁 𝘁𝗿𝗮𝗶𝗻𝗶𝗻𝗴/𝘂𝘀𝗶𝗻𝗴 𝗹𝗶𝘃𝗲 𝗱𝗮𝘁𝗮 𝘁𝗼 𝘁𝗿𝗮𝗶𝗻
# training_data_path = "C:/Users/Computer Arena/Desktop/Qandeel_NKU/Qandeel_ML/training_ppanda/csv_tables/from_helpers/training_data.csv"
# df = pd.read_csv(training_data_path) 
# # END OF CUSTOM TRAINING DATA LOADING


# 𝗖𝗨𝗦𝗧𝗢𝗠 𝗩𝗔𝗟𝗜𝗗𝗔𝗧𝗜𝗢𝗡 𝗗𝗔𝗧𝗔 𝗟𝗢𝗔𝗗𝗜𝗡𝗚. 𝗰𝗼𝗺𝗺𝗲𝗻𝘁 𝘁𝗵𝗶𝘀 𝘀𝗲𝗰𝘁𝗶𝗼𝗻 𝘄𝗵𝗲𝗻 𝗻𝗼𝘁 𝘃𝗮𝗹𝗶𝗱𝗮𝘁𝗶𝗻𝗴/𝘂𝘀𝗶𝗻𝗴 𝗹𝗶𝘃𝗲 𝗱𝗮𝘁𝗮 𝘁𝗼 𝘃𝗮𝗹𝗶𝗱𝗮𝘁𝗲
validation_data = {
  "Var_Id": [340, 340, 340, 340, 340],
  "Result": [1100.00, 1250.00, 1500.00, 10.00, 1990.00],
  "Result_On": ['2023-07-09 5:42:00', '2023-07-09 5:42:00', '2023-07-09 5:42:00', '2023-07-09 5:42:00', '2023-07-09 5:42:00'] 
}

#load data into a DataFrame object:
df = pd.DataFrame(validation_data)
# END OF CUSTOM VALIDATION DATA LOADING


print(df)

# drop indexes
df = df.reset_index(drop=True)

# Detect anomalies for each sublist separately using the model
anomaly_scores_list = detect_anomalies(df)

# Retrieve Var_Id
Var_Id = df['Var_Id']

# Retrieve Result_On
Result_On = df['Result_On']

# Retrieve Result
Result = df['Result']

# anomaly_scores has data type of list
anomaly_scores = anomaly_scores_list[0]['scores']  # Access the 'scores' key and its value

# creating a dataframe to output the results
output_df = pd.DataFrame(list(zip(Var_Id, Result_On, Result, anomaly_scores)), columns=['Var_Id', 'Result_On', 'Result', 'Anomaly_Scores'])
print("The data points and their anomaly scores are: \n ")
print(output_df)

# sending the output_df to a csv file
output_df_csv_path = 'C:/Users/Computer Arena/Desktop/Qandeel_NKU/Qandeel_ML/training_ppanda/csv_tables/one_solution_csv/output_df.csv'
output_df.to_csv(output_df_csv_path, columns=['Var_Id', 'Result_On', 'Result', 'Anomaly_Scores'])

# separate dataframe for anomaly scores of variable no. 340 and 341
anomaly_score_340_df = output_df.query("Var_Id == 340")
anomaly_score_341_df = output_df.query("Var_Id == 341")

# separately performing stats on anomalies detected in variable no. 340 and 341's data 
agg_stats_340 = anomaly_score_340_df.agg({'Anomaly_Scores' : ['min', 'max']})
agg_stats_341 = anomaly_score_341_df.agg({'Anomaly_Scores' : ['min', 'max']})

print('\n \n The minimum and maximum anomaly scores for variable no. 340 are: \n \n', agg_stats_340)
print('\n The minimum and maximum anomaly scores for variable no. 341 are: \n \n', agg_stats_341)

# creating a separate variable for minimum and maximum anomaly score in variable no. 340 and 341
min_anomaly_score_340 = agg_stats_340.iloc[0, 0]
max_anomaly_score_340 = agg_stats_340.iloc[1, 0]

min_anomaly_score_341 = agg_stats_341.iloc[0, 0]
max_anomaly_score_341 = agg_stats_341.iloc[1, 0]

# querying to find the exact data point with minimum/maximum anomaly scores for variables no. 340 and 341
min_anomaly_score_340_df = output_df.query('Var_Id == 340 and Anomaly_Scores == @min_anomaly_score_340')
print('\n \n mininum anomaly score details for variable no. 340 is: \n \n', min_anomaly_score_340_df)

min_anomaly_score_341_df = output_df.query('Var_Id == 341 and Anomaly_Scores == @min_anomaly_score_341')
print('\n \n mininum anomaly score details for variable no. 341 is: \n \n', min_anomaly_score_341_df)

max_anomaly_score_340_df = output_df.query('Var_Id == 340 and Anomaly_Scores == @max_anomaly_score_340')
print('\n \n maximum anomaly score details for variable no. 340 is: \n \n', max_anomaly_score_340_df)

max_anomaly_score_341_df = output_df.query('Var_Id == 341 and Anomaly_Scores == @max_anomaly_score_341')
print('\n \n maximum anomaly score details for variable no. 341 is: \n \n', max_anomaly_score_341_df)

# visualizing the anomaly scores
plt.figure()
plt.scatter(anomaly_scores, range(len(anomaly_scores)))
plt.xlabel('Anomaly Score')
plt.ylabel('Data Point Index')
plt.title('Isolation Forest Anomaly Detection')
plt.show()



