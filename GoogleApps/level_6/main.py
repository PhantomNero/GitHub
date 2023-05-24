# Здесь должен быть твой код
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("cleaned_titanic.csv")
#print(df["Embarked"].fillna("S", inplace=True))
#print(df["Embarked"].value_counts())
age_1 = df[df["Pclass"] == 1]["Age"].median()
age_2 = df[df["Pclass"] == 2]["Age"].median()
age_3 = df[df["Pclass"] == 3]["Age"].median()


# print(age_1)
# print(age_2)
# print(age_3)


def fill_age(row):
    if pd.isnull(row["Age"]):
        if row["Pclass"] == 1:
            return age_1
        if row["Pclass"] == 2:
            return age_2
        if row["Pclass"] == 3:
            return age_3
    return row["Age"]


df["Age"] = df.apply(fill_age, axis=1)


def fill_sex(sex):
    if sex == "male":
        return 1
    return 0


df["Sex"] = df["Sex"].apply(fill_sex)


def is_alone(row):
    if row["SibSp"] + row["Parch"] == 0:
        return 1
    return 0


df["Alone"] = df.apply(is_alone, axis=1)
surv_table = df.pivot_table(values="Age", columns="Alone", index="Survived", aggfunc="count")
print(surv_table)

print("#" * 100)

x = df.drop("Survived", axis=1)
y = df["Survived"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

print(y_test[:-5])
print(y_pred[:-5])

print('Процент правильности: ', accuracy_score(y_test, y_pred) * 100)
print("Confusion matrix: ")
print(confusion_matrix(y_test, y_pred))
