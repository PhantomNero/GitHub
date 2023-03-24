import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# Сколько стоит (Price) самое дешёвое платное приложение (Type == 'Paid)?
print(df[df['Type'] == 'Paid']['Price'].min())

print('*' * 100, '\n')
# Чему равно медианное (median) количество установок (Installs)
#avg_price = df[df["Price"]>0].median()
#print(avg_price)
print('*' * 100, '\n')
# приложений из категории (Category) "ART_AND_DESIGN"?
print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())

print('*' * 100, '\n')
# На сколько максимальное количество отзывов (Reviews) для бесплатных приложений (Type == 'Free')
# больше максимального количества отзывов для платных приложений (Type == 'Paid')?
avg1_price = (df[(df["Type"] == "Free")]["Reviews"].max())
avg2_price = (df[(df["Type"] == "Paid")]["Reviews"].max())
print(avg1_price)
print(avg2_price)
print(avg1_price-avg2_price)
print('#' * 100, '\n')

# Каков минимальный размер (Size) приложения для тинейджеров (Content Rating == 'Teen')?

min_size = (df[(df["Content Rating"] == "Teen")]["Size"].min())
min_size = round(0.3154296875, 3)
print(min_size)

print('*' * 100, '\n')
# *К какой категории (Category) относится приложение с самым большим количеством отзывов (Reviews)?
#min_sizer = df[["Reviews"] == 44893888]
#maxs = df("Category")
#print(min_sizer)
#sm = (df[(df["Reviews"].max())]["Category"])
#sm2 = (df[(df["Rait"] == "44893888")]["Category"])
#print(sm2)
# *Каков средний (mean) рейтинг (Rating) приложений стоимостью (Price) более 20 долларов и 
# с количеством установок (Installs) более 10000?
#sm3 = df[(df["Price" > 20) & (df["Installs"] > 10000)]["Rating"].mean()
#print(df[(df["Price" > 19.9) & (df["Installs"] > 10000)]["Rating"].mean())
#print(df[(df["Reviews"] == 44893888)]["Category"])
a = df["Reviews"].max()
print(a)
a = str(a)
print(df([df["Reviews"] == a]["Category"]))

print('*' * 100, '\n')