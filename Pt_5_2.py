import csv


def add_books():
    k = int(input("Введите количество строк, которые будут добавлены: "))
    new_books = []
    for i in range(k):
        book, author, year = input("Введите название книги, автора и год издания через пробел: ").split()
        new_books.append([book, author, year])
    with open("books.csv", "a", newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(new_books)


def find_books():
    found_books = []
    author = input("Введите автора книги: ")
    print(f"Книги автора - {author}: ")
    with open("books.csv", newline='') as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            if author == row["Author"]:
                found_books.append(row)
    if not found_books:
        print("В списке нет книг данного автора")
    else:
        for row in found_books:
            print(row["Book"], "|", row["Author"], "|", row["Year of release"])


while True:
    choose = int(input("Выберите номер опреации:\n"
                       "1. Добавление новых книг\n"
                       "2. Поиск книг по автору\n"
                       "3. Завершение работы\n"))
    if choose == 1:
        add_books()
    elif choose == 2:
        find_books()
    elif choose == 3:
        break
