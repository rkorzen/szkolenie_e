
# Napisy (str)

# Demonstracja różnych sposobów definiowania napisów
print(
    "to jest napis",
    'to też jest napis',
    "to jest \"wartosc\"",  # Użycie sekwencji ucieczki
    'to jest "wartosc"',    # Alternatywny sposób wstawiania cudzysłowów
    "1",
    sep="\n"  # Separator elementów to nowa linia
)

# Funkcja print jako obiekt
print(print)  # Wydrukuje informację o funkcji print

# Liczby całkowite (int)
# Demonstracja zapisu liczb
1
1000
# Ładniejszy zapis dużych liczb za pomocą podkreślenia
print(1_000_000)  # 1000000
print(1000000)

## Operatory arytmetyczne
# Podstawowe operacje matematyczne
1 + 1
1 - 2
3 * 2
# Różne rodzaje dzielenia
print(3 / 4)   # Dzielenie z wynikiem zmiennoprzecinkowym
print(3 // 4)  # Dzielenie całkowite (zaokrąglanie w dół)
print(3 % 2)   # Reszta z dzielenia (modulo)

# Potęgowanie
print(3 ** 2)  # 9
print(9 ** 0.5)  # Pierwiastek kwadratowy

# Liczby zmiennoprzecinkowe (float) i problem precyzji
print(0.1 + 0.1 + 0.1 == 0.3)
print(0.1 + 0.1 + 0.1)
# Porównanie z "prawie równym"
print(0.1 + 0.1 + 0.1 == 0.30000000000000004)

# Zaokrąglenie do określonej liczby miejsc po przecinku
print(round(0.1 + 0.1 + 0.1, 2))

# Notacja naukowa
print(10e2)
# Maksymalna wartość float
print(1.89e308)
# Nieskończoność i jej zastosowanie
print(float("inf"))
print(float("-inf") < 10 < float("inf"))
# NaN (Not a Number)
print(float("nan"))
# Porównania z NaN zawsze zwracają False
print(float("-inf") < float("nan") < float("inf"))
print(1.2 == 1.2)
print(float("nan") == float("nan"))  # False

# Liczby zespolone (complex)
print(1 + 2j)

## Operatory porównania
# Demonstracja operatorów porównania
1 < 2
2 > 100
2 > 1
3 == 1
2 > 2
2 >= 2

# Typ logiczny (bool)
# Demonstracja wartości logicznych i operatorów logicznych
True, False

True and True
True and False
False and True
False and False

True or True
True or False
False or True
False or False

not False

wynik = 1 > 2
# Porównanie z True za pomocą ==
wynik == True
# Sprawdzenie tożsamości za pomocą is
wynik is True

# Konwersje typów
## Konwersja między int, float, complex, str

# Z liczby na napis:
print(10 + 10)
print(str(10) + str(10))

# Z napisu na liczbę:
print(int("10") + 1)
# Konwersja szesnastkowa
print(int("c0ffee", base=16))

# Konwersja binarna
print(int("101", 2))

# Notacje specjalne dla liczby całkowite:
0b101010    # binarna
0o1234123   # ósemkowa
0x123ff     # szesnast