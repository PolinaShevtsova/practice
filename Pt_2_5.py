import random

lisst = [1, 0]
print("Орёл - 0"
      "Решка -1")
win_count = 0
lose_count = 0
check = 0
while True:
    system_choice = random.choice(lisst)
    user_choice = int(input("Введите значение: "))
    if system_choice == user_choice:
        win_count += 1
        check += 1
    else:
        lose_count += 1
        check = 0
    print(f"Количество побед: {win_count}"
          f"Количество проигрышей: {lose_count}")
    if check == 3:
        print("Вы выиграли!")
        break
