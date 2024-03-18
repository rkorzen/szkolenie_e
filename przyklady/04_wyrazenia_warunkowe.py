# Przykłady użycia instrukcji warunkowych if / elif / else

# 1. Prosty przykład sprawdzenia, czy liczba jest większa od zera
number = 5

if number > 0:
    print("Liczba jest większa od zera.")

# 2. Dodanie instrukcji else do obsługi przypadku, gdy warunek nie jest spełniony
number = -3

if number > 0:
    print("Liczba jest większa od zera.")
else:
    print("Liczba nie jest większa od zera.")

# 3. Dodanie instrukcji elif do przetestowania dodatkowego warunku
number = -3

if number > 0:
    print("Liczba jest większa od zera.")
elif number == 0:
    print("Liczba jest równa zero.")
else:
    print("Liczba jest mniejsza od zera.")

# 4. Zagnieżdżone instrukcje warunkowe
number = 10

if number > 0:
    if number % 2 == 0:
        print("Liczba dodatnia i parzysta.")
    else:
        print("Liczba dodatnia i nieparzysta.")
else:
    print("Liczba nie jest dodatnia.")

# 5. Użycie skróconej formy z warunkowym wyrażeniem
age = 25
status = "pełnoletni" if age >= 18 else "niepełnoletni"
print(f"Osoba jest {status}.")
