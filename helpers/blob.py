import pandas as pd

csv_path = "C:/Users/Computer Arena/Desktop/Qandeel_NKU/Qandeel_ML/training_ppanda/csv_tables/from_queries/340_var_id_data.csv"
df = pd.read_csv(csv_path)

# Extract Var_Id and Result column data from the given data/df   
Var_Id = df['Var_Id']
Result = df['Result']

# Using pandas.concat() to concat two DataFrames
df2 = pd.concat([Result, Var_Id], axis=1)
df2 = df2.reset_index(drop=True)
print(df2)
