a = int(input("Введите число: "))
b = 0
while a != 0 and b < 1000 and a < 30000 and a%8 == 0:
    if a > 9 and a < 100:
        b = b + 1
        a = int(input("Введите число: "))
    else:
        break
print(b)