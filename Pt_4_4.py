from functools import reduce
from itertools import combinations

number = int(input("Введите число: "))
numbers = [x for x in range(1, 11)]
unique_combinations = []

for r in range(1, len(numbers) + 1):
    combinations_r = combinations(numbers, r)
    unique_combinations.extend(combinations_r)
sum_comb = []
for i in unique_combinations:
    summa = reduce(lambda x, y: x + y, i)
    if summa == number:
        sum_comb.append(i)

print(f"Комбинации равные введенному числу: {sum_comb} из списка: {numbers}")
