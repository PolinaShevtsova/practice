import csv


def find_books(fr_year, t_year):
    found_books = []
    with open("books.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            for year in range(fr_year, t_year + 1):
                year = str(year)
                if year == row["Year of release"]:
                    found_books.append(row)
    if not found_books:
        print("В списке нет книг этих годов")
    else:
        for row in found_books:
            print(row["Book"], "|", row["Author"], "|", row["Year of release"])


try:
    from_year = int(input("Введите нижнюю границу диапазона годов: "))
    to_year = int(input("Введите верхнюю границу диапазона годов: "))
    find_books(from_year, to_year)
except ValueError:
    print("Введено не число!")
