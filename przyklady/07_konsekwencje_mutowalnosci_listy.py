# Importowanie modułu deepcopy z biblioteki copy
from copy import deepcopy

# Tworzenie listy a
a = [1, 2, 3]

# Tworzenie kopii listy a za pomocą metody copy()
b = a.copy()

# Tworzenie listy c, która zawiera listę a jako jeden z jej elementów
c = [5, 6, a]

# Tworzenie głębokiej kopii listy c za pomocą deepcopy()
d = deepcopy(c)

# Modyfikacja oryginalnej listy a poprzez dodanie nowego elementu
a.append(10)

# Wyświetlenie zawartości listy b i d
print("Zawartość listy b:", b)  # Wynik: [1, 2, 3]
print("Zawartość listy d:", d)  # Wynik: [5, 6, [1, 2, 3]]
