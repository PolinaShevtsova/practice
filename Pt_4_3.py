def simple_check(digit):
    for num in range(2, digit):
        if digit % num == 0:
            return False
    return True


border1 = int(input("Нижняя граница диапазона: "))
border2 = int(input("Верхняя граница диапазона: "))

for number in range(border1, border2 + 1):
    if simple_check(number):
        print(number)
