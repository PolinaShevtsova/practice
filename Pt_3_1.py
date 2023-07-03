from functools import reduce

lisst = [21, 23, 45, 56, 3, 43]
average = reduce(lambda x, y: x + y, list) / len(lisst)
print(average)
