import pandas as pd


df = pd.read_csv('investments_VC.csv', sep=',', quotechar='"')
# Clean the DataFrame by removing commas and quotes
df.replace(',', '', regex=True, inplace=True)
df.replace('"', '', regex=True, inplace=True)

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_filename.csv', sep=',', quotechar='"', index=False)


