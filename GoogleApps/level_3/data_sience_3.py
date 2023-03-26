import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
min_size = (df[(df["Category"] == "BUSINESS")])
a = len(min_size)
print(a)
print('#' * 100, '\n')
# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых.
teen = (df[(df["Content Rating"] == "Teen")])
kids = (df[(df["Content Rating"] == "Everyone 10+")])
b = len(teen)
c = len(kids)
d = b/c
d = round(d, 2)
print(b)
print(c)
print(d)
print('#' * 100, '\n')
# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений?
# Ответ запиши с точностью до сотых.
finance = (df[(df["Type"] == "Paid")]["Rating"]).mean()
finance2 = round(finance, 2)
print(finance2)
# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.
tp = (df[(df["Type"] == "Free")]["Rating"]).mean()
print(tp)
l = finance - tp
l = round(l, 2)
print(l)
print('*' * 100, '\n')
# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.
mins = (df[(df["Category"] == "COMICS")]["Size"]).min()
maxs = (df[(df["Category"] == "COMICS")]["Size"]).max()
mins = round(mins, 2)
maxs = round(maxs, 2)
print(mins)
print(maxs)
print('/' * 100, '\n')
# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?
am = (df[(df["Rating"] > 4.5) & (df["Category"] == "FINANCE")])
am = len(am)
print(am)
print('/' * 100, '\n')
# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?
sm = (df[(df["Rating"] > 4.9) & (df["Type"] == "Free") & (df["Category"] == "GAME")])
sm = len(sm)
print(sm)

fm = (df[(df["Rating"] > 4.9) & (df["Type"] == "Paid") & (df["Category"] == "GAME")])
fm = len(fm)
print(fm)

g = sm/fm

print(g)
