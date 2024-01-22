def add_hero_to_category(category, heroes_set):
    hero_name = input(f"Введите имя героя для категории {category}: ")
    heroes_set.add(hero_name)


def input_hero(category):
    hero_name = input(f"Введите выбранного героя для категории {category}: ")
    return hero_name.strip()


def main():
    # Добавление героев пользователя в каждую категорию
    add_hero_to_category('Мид', mid_heroes)
    add_hero_to_category('Керри', carry_heroes)
    add_hero_to_category('Оффлэйн', offlane_heroes)
    add_hero_to_category('Саппорт', support_heroes)
    add_hero_to_category('Фул саппорт', full_support_heroes)

    # Ввод героев пользователя для каждой категории
    selected_mid_hero = input_hero('Мид')
    selected_carry_hero = input_hero('Керри')
    selected_offlane_hero = input_hero('Оффлэйн')
    selected_support_hero = input_hero('Саппорт')
    selected_full_support_hero = input_hero('Фул саппорт')

    # Ввод типа героя пользователя
    selected_hero_type = input("Введите тип героя (Сила, Гибкость, Интеллект, Универсал): ")

    # Вывод результата
    get_best_hero('Мид', mid_heroes, selected_mid_hero)
    get_best_hero('Керри', carry_heroes, selected_carry_hero)
    get_best_hero('Оффлэйн', offlane_heroes, selected_offlane_hero)
    get_best_hero('Саппорт', support_heroes, selected_support_hero)
    get_best_hero('Фул саппорт', full_support_heroes, selected_full_support_hero)

    get_best_hero_type(selected_hero_type.capitalize())


def get_best_hero(category, heroes, selected_hero):
    common_picks = mid_heroes.union(carry_heroes, offlane_heroes, support_heroes, full_support_heroes)
    available_heroes = heroes.intersection(common_picks)

    if selected_hero in available_heroes:
        available_heroes.remove(selected_hero)

    if available_heroes:
        print(f"Лучший герой в категории {category}: {available_heroes.pop()}")
    else:
        print(f"Нет доступных героев в категории {category}")


def get_best_hero_type(hero_type):
    if hero_type in hero_types:
        print(f"Лучший герой типа {hero_type}: {hero_types[hero_type][0]}")
    else:
        print(f"Нет информации о героях типа {hero_type}")


if __name__ == "__main__":
    mid_heroes = set()
    carry_heroes = set()
    offlane_heroes = set()
    support_heroes = set()
    full_support_heroes = set()

    hero_types = {'Strength': ['Wraith King', 'Pudge', 'Axe'],
                  'Agility': ['Phantom Lancer', 'Riki', 'Morphling'],
                  'Intelligence': ['Invoker', 'Crystal Maiden', 'Pugna'],
                  'Universal': ['Mirana', 'Juggernaut', 'Rubick']}

    main()
