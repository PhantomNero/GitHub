# Открываем файл на чтение
with open('my_file.txt', 'r') as file:
    # Инициализируем переменную для суммы максимальных чисел
    sum_of_max_numbers = 0

    # Итерируемся по строкам файла
    for line in file:
        # Разбиваем строку на числа и преобразуем их в список целых чисел
        numbers = [int(num) for num in line.split()]

        # Находим максимальное число в текущей строке и добавляем его к сумме
        max_number = max(numbers)
        sum_of_max_numbers += max_number

# Выводим результат
print(f"Сумма максимальных чисел в каждой строке: {sum_of_max_numbers}")
