names = ["Клон", "Новости", "Друзья", "Гадалка"]
print("Список передач:")
k = 0
for show in names:
    print(k, ". ", show)
    k += 1
new = input("Введите название новой передачи: ")
position = int(input("Введите позицию, на которой она должна быть вставлена: "))
names.insert(position, new)
k = 0
print("Обновленный список передач:")
for show in names:
    print(k, ". ", show)
    k += 1
