n = int(input("Введите число n: "))
for i in range(int(n ** 0.5) - 1, n):
    if i ** 2 > n:
        print(i)
        break
