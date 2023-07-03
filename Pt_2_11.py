a, b = map(int, input("Введите два числа через пробел: ").split())
summ = 0
for i in range(a, b + 1):
    summ += i
print(summ)
