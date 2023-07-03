import random

red = "Красный"
blue = "Синий"
yellow = "Желтый"
green = "Зеленый"
orange = "Оранжевый"
colours = [red, blue, yellow, green, orange]
system_colour = random.choice(colours)
print(f"Введите цвет из списка: {red, blue, yellow, green, orange}")
while True:
    user_colour = input()
    if system_colour != user_colour:
        if system_colour == red:
            print("Огненый цвет")
        elif system_colour == blue:
            print("Цвет неба")
        elif system_colour == yellow:
            print("Цвет лимона")
        elif system_colour == green:
            print("Цвет травы")
        elif system_colour == orange:
            print("Цвет заката")
        print("Повторите попытку!")
    else:
        print("Отлично!")
        break
