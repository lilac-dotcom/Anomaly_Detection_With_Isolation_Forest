import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/Computer Arena/Desktop/training_ppanda/csv_tables/var_id__result_on__result_1_299.csv')

# Count the occurrences of each value in the "Result" column
result_counts = df['Result'].value_counts().reset_index()

# Assign the column headers
result_counts.columns = ['Result', 'Count']

# Print the counts for each value
print(result_counts)


