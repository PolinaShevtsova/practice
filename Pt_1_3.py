a, b, c = map(int, input("введите три числа:").split())
liste = [a, b, c]
print(max(liste))
print(sorted(liste, reverse=True))
