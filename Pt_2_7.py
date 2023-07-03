summ = 0
while True:
    n = int(input("Введите число: "))
    if n < 0:
        summ += n
    else:
        break
print(summ)
