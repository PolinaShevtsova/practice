from functools import reduce

n = int(input("Введите число: "))
lisst = [1, 1]
while lisst[1] <= n:
    print(lisst[1])
    x = reduce(lambda z, y: z + y, lisst)
    lisst[0] = lisst[1]
    lisst[1] = x
    print(lisst)
