import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# 1 Выведи на экран минимальный, средний и максимальный рейтинг ('Rating') платных и бесплатных приложений ('Type') с точностью до десятых.
# temp = df.pivot_table(columns="Category", index="Type", values="Rating", aggfunc=[min, max])
#mins1 = (df[(df["Type"] != "Paid")]["Content Rating"])
#means1 = (df[(df["Type"] != "Paid")]["Content Rating"])
#maxs1 = (df[(df["Type"] != "Paid")]["Content Rating"])
# mins1 = round(mins1, 1)
# means1 = round(means1, 1)
# maxs1 = round(maxs1, 1)
#print(mins1)
#print(means1)
#print(maxs1)

#print("Т" * 100)
#mins = (df[(df["Type"] == "Paid")]["Content Rating"])
#means = (df[(df["Type"] == "Paid")]["Content Rating"])
#maxs = (df[(df["Type"] == "Paid")]["Content Rating"])
## mins = round(mins, 1)
# maxs = round(maxs, 1)
# means = round(means, 1)
#print(mins)
#print(means)
#print(maxs)

#tempw = df.pivot_table(columns="Content Rating", index="Category", values="Price", aggfunc=[min])
#print(tempw)
# 2 Выведи на экран минимальную, медианную (median) и максимальную цену ('Price') платных приложений (Type == 'Paid') для
# разных целевых аудиторий ('Content Rating')

# 3 Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом
# посчитай максимальное количество отзывов ('Reviews') в каждой группе.
# Сравни результаты для категорий 'EDUCATION', 'FAMILY' и 'GAME':
# В какой возрастной группе больше всего отзывов получило приложение из категории 'EDUCATION'? 'FAMILY'? 'GAME'?
# Подсказка: ты можешь выбрать из DataFrame несколько столбцов одновременно с помощью такого синтаксиса:
# df[[<столбец 1>, <столбец 2>, <столбец 3>]]


# 4 Сгруппируй платные (Type == 'Paid') приложения по категории ('Category') и целевой аудитории ('Content Rating')
# Посчитай среднее количество отзывов ('Reviews') в каждой группе
# Обрати внимание, что в некоторых ячейках полученной таблицы отражается не число, а значение "NaN" - Not a Number
# Эта запись означает, что в данной группе нет ни одного приложения.
# Выбери названия категорий, в которых есть платные приложения для всех возрастных групп и расположи их в алфавитном порядке.

# Бонусная задача. Найди категории бесплатных (Type == 'Free') приложений, 
tempw = df.pivot_table(columns="Content Rating", index="Category", values="Price", aggfunc=[min])
print(tempw)