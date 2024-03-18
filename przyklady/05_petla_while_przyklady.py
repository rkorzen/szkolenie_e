# 1. Liczenie w dół od 10 do 1
print("Przykład 1: Liczenie w dół od 10 do 1")
countdown = 10
while countdown >= 1:
    print(countdown)
    countdown -= 1

# 2. Sumowanie liczb od 1 do 100
print("\nPrzykład 2: Sumowanie liczb od 1 do 100")
total = 0
number = 1
while number <= 100:
    total += number
    number += 1
print("Suma liczb od 1 do 100 wynosi:", total)

# 3. Wykonywanie pętli, dopóki użytkownik nie poda poprawnej odpowiedzi
print("\nPrzykład 3: Wykonywanie pętli, dopóki użytkownik nie poda poprawnej odpowiedzi")
correct_answer = 7
guess = int(input("Podaj liczbę od 1 do 10: "))

while guess != correct_answer:
    print("Nieprawidłowa odpowiedź.")
    guess = int(input("Spróbuj ponownie: "))

print("Gratulacje! Podałeś prawidłową liczbę.")

# 4. Iterowanie po liście, dopóki nie zostanie znaleziony określony element
print("\nPrzykład 4: Iterowanie po liście, dopóki nie zostanie znaleziony określony element")
fruits = ["jabłko", "banan", "gruszka", "śliwka"]
search_item = "gruszka"
index = 0

while index < len(fruits) and fruits[index] != search_item:
    index += 1

if index < len(fruits):
    print(f"{search_item} została znaleziona na pozycji {index}.")
else:
    print(f"{search_item} nie została znaleziona.")

# 5. Wykonywanie pętli, dopóki użytkownik nie wpisze "quit"
print("\nPrzykład 5: Wykonywanie pętli, dopóki użytkownik nie wpisze 'quit'")
user_input = ""
while user_input != "quit":
    user_input = input("Wpisz coś (wpisz 'quit' aby zakończyć): ")
    print("Wpisano:", user_input)
