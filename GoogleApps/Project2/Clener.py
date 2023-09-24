import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("train.csv")

# List of labels to drop
labels_to_drop = ["id", "bdate", "has_photo", "last_seen", "career_end", "occupation_name", "followers_count",
                  "relation", "education_status", "city", "has_mobile"]

# Drop the specified columns and assign the result back to the DataFrame
df = df.drop(labels_to_drop, axis=1)  # Use axis=1 to drop columns

# Save the modified DataFrame back to the CSV file
df.to_csv('train.csv', index=False)  # Use index=False to avoid writing row numbers as a column
