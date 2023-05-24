import pandas as pd

df = pd.read_csv("titanic.csv")
df.drop(["PassengerId", "Name", "Ticket", "Cabin", "Embarked"], axis=1, inplace=True)
df.to_csv('cleaned_titanic.csv')
