lisst = int(input("Введите число: "))
f = lambda x: x % 2 == 0
if f(lisst):
    print("Число четное")
else:
    print("Число нечетное")
