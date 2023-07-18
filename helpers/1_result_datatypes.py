import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/Computer Arena/Desktop/training_ppanda/csv_tables/1__var_id__result_on__result.csv')

# Get the unique data types in the "Result" column
result_data_types = df['Result'].apply(type).unique()

# Print the unique data types
print(result_data_types)


