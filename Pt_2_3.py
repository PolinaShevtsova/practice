print("Введите число: ")
numder = int(input())
copy_numder = numder
summ = 0
while copy_numder > 0:
    summ += (copy_numder % 10) ** 3
    copy_numder //= 10
if numder == summ:
    print("Это число Армстронга")
else:
    print("Это не число Армстронга")
