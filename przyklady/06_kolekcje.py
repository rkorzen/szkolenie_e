# Napis jako kolekcja - niemutowalny
napis = "ala ma kota"

# Dostęp do poszczególnych znaków w napisie
print(napis[8])   # Indeks 8, zwraca 't'
print(napis[-1])  # Ostatni znak, zwraca 'a'

# Iteracja po napisie za pomocą pętli while
i = 0
while i < len(napis):
    znak = napis[i]
    print(znak)
    i += 1

# Slicing - wybieranie fragmentów napisu
print(napis[1])       # Wartość z indeksu 1, zwraca 'l'
print(napis[1:5])     # Wartości z zakresu od 1 do 4, zwraca 'la m'
print(napis[1:10:2])  # Wartości z zakresu od 1 do 9 z krokiem 2, zwraca 'l ak'
print(napis[:])       # Cały napis, zwraca 'ala ma kota'
print(napis[3::-1])   # Odwrócenie fragmentu napisu, zwraca 'al a'

# Metody stringa
print(napis.title())       # Każde słowo zaczyna się z wielkiej litery
print(napis.upper())       # Wszystkie litery zamienione na wielkie
print(napis.capitalize())  # Pierwsza litera na wielką, reszta na małe

print(napis.isalnum())            # Sprawdza, czy wszystkie znaki w napisie są alfanumeryczne
print("alamakota".isalnum())      # Zwraca True, bo wszystkie znaki są alfanumeryczne
print("zążółćgęśłąjaźń".isascii())  # Zwraca False, zawiera znaki spoza ASCII

# Krotka, tuple, niemutowalne
zestaw0 = (1, 2, "1", "a")
print(zestaw0[2])  # Dostęp do elementu na indeksie 2, zwraca '1'

# Lista (list) - mutowalna
zestaw1 = [1, 2, "1", "a"]
print(zestaw1[2])  # Dostęp do elementu na indeksie 2, zwraca '1'

zestaw1[1] = "zmienione"  # Zmiana wartości elementu na indeksie 1
print(zestaw1)            # Wyświetlenie zmienionej listy

# Próba zmiany elementu krotki spowoduje błąd, ponieważ krotki są niemutowalne
# zestaw0[1] = "zmienione"  # TypeError: 'tuple' object does not support item assignment
