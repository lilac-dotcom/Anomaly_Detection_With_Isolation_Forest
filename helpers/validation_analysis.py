import pandas as pd

# specify path to validation results' csv file
csv_path = "C:/Users/Computer Arena/Desktop/Qandeel_NKU/Qandeel_ML/training_ppanda/csv_tables/one_solution_csv/output_df.csv"

# Load the CSV file into a dataframe
df = pd.read_csv(csv_path)

# drop indexes
df = df.reset_index(drop=True)

df['Validation_Accuracy'] = df['Anomaly_Scores'] < 0

print('\n', df)

# some additional stats
# getting total rows/values
total_value_count = df['Anomaly_Scores'].count()
print('\n Total values in validation dataset: ', total_value_count)

# getting total outliers detected in validation dataset
true_detection_count = (df['Validation_Accuracy'] == True).sum()
print('\n Total outliers detected in validation dataset: ', true_detection_count)

# getting accuracy of model
accuracy = true_detection_count / total_value_count
print('\n Accuracy of model after validation is: ', accuracy)

# sending the output_df to a csv file
validation_analysis_csv_path = 'C:/Users/Computer Arena/Desktop/Qandeel_NKU/Qandeel_ML/training_ppanda/csv_tables/from_helpers/validation_analysis.csv'
df.to_csv(validation_analysis_csv_path, columns=['Var_Id', 'Result_On', 'Result', 'Anomaly_Scores', 'Validation_Accuracy'])