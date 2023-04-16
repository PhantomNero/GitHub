import pandas as pd

df = pd.read_csv('GooglePlayStore_wild.csv')


# Очистка данных из первого задания

# Замени тип данных на дробное число (float) для цен приложений ('Price')

# Вычисли, сколько долларов разработчики заработали на каждом платном приложении
# def split(genres):
#    return genres.split(",")
# df["Genres"] = df["Genres"].apply(split)
# df["Numbres of genres"]
# Чему равен максимальный доход ('Profit') среди платных приложений (Type == 'Paid')?
def set_season(date):
    month = date.sprit()[0]
    seasons = {
        "Зима": ["December", "January", "February"],
        "Лето": ["June", "July", "August"],
        "Весна": ["March", "April", "May"],
        "Осень": ["October", "November", "September"]}

    for season in seasons:
        if month in seasons[season]:
            return season
        return "Сезон не установлен"


df["Season"] = df["Last Updated"].apply(set_season)

print(df["Season"].value_counts())

# Создай новый столбец, в котором будет храниться количество жанров. Назови его 'Number of genres'

# Какое максимальное количество жанров ('Number of genres') хранится в датасете?

# Бонусное задание
# Создай новый столбец, хранящий сезон, в котором было произведено последнее обновление ('Last Updated') приложения. Назови его 'Season'

# Выведи на экран сезоны и их количество в датасете
