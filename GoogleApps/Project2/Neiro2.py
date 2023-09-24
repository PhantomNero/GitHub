import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier

df = pd.read_csv("train.csv")

features = ['sex', 'graduation', 'occupation_type']
X = df[features]

le_result = LabelEncoder()
y = le_result.fit_transform(df['result'])

label_encoders = {}
for feature in features:
    le = LabelEncoder()
    X[feature] = le.fit_transform(X[feature])
    label_encoders[feature] = le

clf = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
clf.fit(X, y)

print("Please provide information:")
sex = input("Sex (Male - 1, Woman - 2): ")
graduation_year = int(input("Graduation Year (**** - 2023): "))
occupation_type = input("Occupation Type (university, work): ")

sex_encoded = label_encoders['sex'].transform([sex])[0]
occupation_type_encoded = label_encoders['occupation_type'].transform([occupation_type])[0]

user_input = [[sex_encoded, graduation_year, occupation_type_encoded]]

prediction = clf.predict(user_input)

predicted_result = le_result.inverse_transform(prediction)[0]

print(f"Predicted Result: {predicted_result}")
