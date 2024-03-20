# na poczatku bez biblioteki


with open("plik.csv") as f:
    for row in f:
        print(row.split(";"))
print("-"*40)

import csv

with open("plik.csv") as f:
    reader = csv.DictReader(f, delimiter=";", quotechar="|")

    for row in reader:
        print(row)