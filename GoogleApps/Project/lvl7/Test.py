import pandas as pd
df = pd.read_csv('cleaned_filename.csv')
# Number of companies that have invested more than $100,000
num_more_than_100k = len(df[df['funding_total_usd'] > 100000]['name'].unique())
print("Number of companies that have invested more than $100,000:", num_more_than_100k)

# Number of companies that have invested less than $100,000
num_less_than_100k = len(df[df['funding_total_usd'] < 100000]['name'].unique())
print("Number of companies that have invested less than $100,000:", num_less_than_100k)

# Number of successful companies that have invested more than $100,000
#num_successful_more_than_100k = len(df[(df['funding_total_usd'] > 100000) & (df['status'] == 'successful')]['name'].unique())
#print("Number of successful companies that have invested more than $100,000:", num_successful_more_than_100k)

# Number of successful companies that have invested less than $100,000
#num_successful_less_than_100k = len(df[(df['funding_total_usd'] < 100000) & (df['status'] == 'successful')]['name'].unique())
#print("Number of successful companies that have invested less than $100,000:", num_successful_less_than_100k)
