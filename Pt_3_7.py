diction = {}
s = input("Введите строку:")
for i in s:
    if i != " ":
        if i in "уеыаоэяию":
            diction[i] = True
        else:
            diction[i] = False
print(diction)
