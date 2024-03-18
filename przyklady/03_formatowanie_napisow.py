imie = "Rafał"
wzrost = 181
stanowisko = "trener"

# Stary sposób formatowania za pomocą konkatenacji i konwersji typów
raport = "Imię: " + imie + ", wzrost: " + str(wzrost) + ", stanowisko: " + stanowisko
print(raport)

# Nowoczesny sposób za pomocą f-stringów
raport1 = f"Imię: {imie}, wzrost: {wzrost}, stanowisko: {stanowisko}"
print(raport1)

# Formatowanie za pomocą metody format()
raport1a = "Imię: {imie}, wzrost: {wzrost}, stanowisko: {stanowisko}"
raport1b = raport1a.format(imie="Wojtek", wzrost=wzrost, stanowisko=stanowisko)

# Składanie raportów z użyciem f-stringów i formatowania z zachowaniem czytelności
raport = f"{raport1}\n{raport1a}\n{raport1b}"
print(raport)

# Alternatywna, bardziej zwięzła forma łączenia ciągów w f-stringach
raport2 = f"{raport1}\n{raport1a}\n{raport1b}\n"
print(raport2)

# Formatowanie za pomocą ciągów wieloliniowych
raport3 = (f"{raport1}\n"
           f"{raport1a}\n"
           f"{raport1b}\n")
print(raport3)

# Uwaga: raport1a w powyższych przykładach jest tylko szablonem napisu i nie jest sformatowany przy pomocy metodą .format() lub jako f-string w kontekście zmiennych imie, wzrost, stanowisko zdefiniowanych na początku. Pokazuje to, jak można użyć tego samego szablonu z różnymi danymi.
