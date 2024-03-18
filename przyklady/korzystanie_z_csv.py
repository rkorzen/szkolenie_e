import csv

# Dane do zapisania
data = [['Numer', 'Nazwa'], [1, 'Ąęćłńóśźż'], [2, 'Produkt B']]

# Utworzenie pliku CSV w kodowaniu UTF-8 bez BOM
with open('przyklad_utf8.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print('Plik CSV w kodowaniu UTF-8 został utworzony.')


import csv

# Dane do zapisania
data = [['Numer', 'Nazwa'], [1, 'Ąęćłńóśźż'], [2, 'Produkt B']]

# Utworzenie pliku CSV w kodowaniu UTF-8 z BOM
with open('przyklad_utf8_bom.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print('Plik CSV w kodowaniu UTF-8 z BOM został utworzony.')
