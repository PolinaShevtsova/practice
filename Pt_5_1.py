import csv

books = [("Book", "Author", "Year of release"),
         ["If she knew", "Blake Pierce", "2019"],
         ["Watching", "Blake Pierce", "2019"],
         ["Here and Now", "Guillaume Musso", "2018"],
         ["The Notebook", "Nicholas Sparks", "1996"],
         ["A Bend in the Road", "Nicholas Sparks", "2011"]]

with open("books.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(books)
