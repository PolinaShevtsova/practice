lisst = [int(input("Введите число списка: ")) for n in range(5)]
print(f"Исходный список: {lisst}")
list1 = [n ** 2 for n in lisst]
print(f"Новый список: {list1}")
