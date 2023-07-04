number = input("Введите число: ")
numbers = []
for x in number:
    numbers.append(int(x))
print("Максимальное число: ", *sorted(numbers, reverse=True))
