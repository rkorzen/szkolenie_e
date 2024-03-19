"""
Mamy zadaną listę liczb:

[1, 2, 16, 17, 21, 13, 37]

napisz skrypt, któr z tej listy wybierze tylko te liczby, które sa 
liczbami pierwszymi
!=
"""

liczby = [1, 2, 16, 17, 21, 13, 37]
liczby_pierwsze = []

for liczba in liczby:
    if liczba < 2:
        continue

    for potencjalny_dzielnik in range(2, liczba):
        if liczba % potencjalny_dzielnik == 0:
            break
    else:
        liczby_pierwsze.append(liczba)

print(liczby_pierwsze)