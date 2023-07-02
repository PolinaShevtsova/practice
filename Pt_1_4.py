def check():
    print("Введите число в диапазоне от 10 до 20:")
    a = int(input())
    if a < 10:
        print("Число меньше требуемого диапазона")
        check()
    elif a > 20:
        print("Число больше требуемого диапазона")
        check()
    else:
        print("Спасибо")
        return


check()
