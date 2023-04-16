import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')
# Выведи информацию о всем DataFrame, чтобы узнать какие столбцы нуждаются в очистке
# Сколько в датасете приложений, у которых не указан ('NaN') рейтинг ('Rating')?
#print(df.info())
# Замени пустое значение ('NaN') рейтинга ('Rating') для таких приложений на -1.
#print(df[pd.isnull(df["Rating"])])
# Определи, какое ещё значение размера ('Size') хранится в датасете помимо Килобайтов и Мегабайтов, замени его на -1.
# Преобразуй размеры приложений ('Size') в числовой формат (float). Размер всех приложений должен измеряться в Мегабайтах.
# Чему равен максимальный размер ('Size') приложений из категории ('Category') 'TOOLS'?
#print(df[df['Category'] == 'TOOLS']['Size'].max())
#pd.set_option('display.max_rows', 10840)
#pd.set_option('display.max_colwidth', 10840)
#pd.set_option('display.max_columns', None)
#print(a)
#tp = (df[(df["Category"] == "TOOLS")])["Size"].max()

#sm3 = df[(df["Category"] == "TOOLS") & (df["Category"] != "Varies with device")]["Size"].max()

#print(sm3)

#print(df["Size"].value_counts())
#print(tp)

#def set_size(size):
#    if size[-1] == "M":
#       return float(size[:-1])
#    if size[-1] == "k":
#        return float(size[:-1]) / 1024
#    return -1

#df["Size"] = df["Size"].apply(set_size).max()
#print(df["Size"].value_counts())
#print(df[df['Category'] == 'TOOLS']['Size'].max())
# Бонусные задания
# Замени тип данных на целочисленный (int) для количества установок ('Installs').
# В записи количества установок ('Installs') знак "+" необходимо игнорировать.
# Т.е. если в датасете количество установок равно 1,000,000+, то необходимо изменить значение на 1000000
#def set_installs():
#    if installs == "0":
#        return 0
#    return int(installs[:-1].replace(',', ','))

#df["Installs"] = df['Installs'].apply(set_installs())
#print(df["Installs"])

# int64   10840   Installs
#
#
# 10839 10000000
# Сгруппируй данные по категории ('Category') и целевой аудитории ('Content Rating') любым удобным для тебя способом,
# посчитай среднее количество установок ('Installs') в каждой группе. Результат округли до десятых.
# В полученной таблице найди ячейку с самым большим значением.
# К какой возрастной группе и типу приложений относятся данные из этой ячейки?
#result = df.pivot_table(index='Content Rating', columns='Type', values='Installs', aggfunc='mean')
#print(round(result, 1))
# У какого приложения не указан тип ('Type')? Какой тип там необходимо записать в зависимости от цены?
#df["Type"].fillna("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS", inplace=True)
#print(df.info)
sm = (df[(df["Type"] != "Free") & (df["Type"] != "Paid")]["App"])
sm2 = (df[(df["Type"] != "Free") & (df["Type"] != "Paid")]["Price"])
print(sm)
print(sm2)

# Выведи информацию о всем DataFrame, чтобы убедиться, что очистка прошла успешно