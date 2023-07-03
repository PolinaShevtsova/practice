def check_simple(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


lisst = [int(input("Введите число списка: ")) for n in range(5)]
print(f"Исходный список: {lisst}")
list1 = [n for n in lisst if check_simple(n)]
print(f"Новый список: {list1}")
