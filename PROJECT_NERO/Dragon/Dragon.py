import random
import time


def displayIntro():
    print("Вы бродили в пещере и вдруг вы осознали, что вы потерялись!")
    print("Перед вами есть два ответвления.")
    print("В первом ответвлении живет добрый дракон, который покажет где выход!")
    print("Во втором ответвлении живет злой дракон, который вас съест")


def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Вы должны решить, в какую пещеру вы войдете!")
        print("В первую или во-вторую?")
        cave = input()

    return cave


def checkCave(choosenCave):
    print("Вы приближаетесь к пещере...")
    time.sleep(2)
    print("Вы уже так рядом что слышите дыхание дракона...")
    time.sleep(2)
    print("Иииии...")
    time.sleep(4)

    friendlyCave = random.randint(1, 2)

    if choosenCave == str(friendlyCave):
        print("Дракон показал вам выход!!")

    else:
        print("Дракон съел вас заживо!!")


playAgain = "Да"
while playAgain == "Да" or playAgain == "Нет":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Хотите снова " "Да или нет")
    playAgain = input()