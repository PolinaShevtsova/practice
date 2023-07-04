import itertools

s = input("Введите строку: ")
permutations = itertools.permutations(s)
kol = 0
for perm in permutations:
    kol += 1
print("Количество перестановок: ", kol)
