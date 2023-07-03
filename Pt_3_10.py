s = input("Введите строку:")
s = s.replace(" ", "")
diction = {k: s.count(k) for (k) in s}
print(diction)
