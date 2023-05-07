import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('investments_VC.csv')

# Convert the funding_total_usd column to a numeric data type
df['funding_total_usd'] = pd.to_numeric(df['funding_total_usd'], errors='coerce')

# 'errors=coerce' will set invalid parsing to NaN

# Print the data types of each column in the DataFrame to confirm the change
print(df.dtypes)
