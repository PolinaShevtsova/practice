n = int(input("Введите число n: "))
copy = n
lisst = []
while copy > 0:
    lisst.append(copy % 10)
    copy //= 10
print("Индекс максимального элемента с конца списка: ", lisst.index(max(lisst)) + 1)
print("Индекс максимального элемента с начала списка:", len(lisst) - lisst.index(max(lisst)))
