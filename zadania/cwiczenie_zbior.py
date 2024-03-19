"""
input, set
znak = input("Podaj znak: ")

if znak == "":

el. 1. jak dodać do zbioru jakiś element?
el. 2. spróbuj napisać skrypt, który będzie pozwala na wprowadzanie
przez użytkownika znaków. Jeśli użytkownik nacisnie enter bez podania
znaku to konczymy program i wypisujemy ile bylo unikalnych znakow 


uruchamiamy...

Podaj znak: a
Podaj znak: 

Unikalnych znaków: 1

"""

znaki = set()
liczby = []
# print(dir(x))
# print(help(x.add))
# x.add(10)
# jak do x dodać jakaś wartość?

while True:
    znak = input("Podaj znak: ")
    # print(znak, type(znak))
    if znak.isnumeric():
        liczby.append(int(znak))
    znaki.add(znak)
    if znak == "":
        break

# if len(liczby) > 0:
#     srednia = sum(liczby)/len(liczby)

try:
    srednia = sum(liczby)/len(liczby)
except ZeroDivisionError:
    srednia = "Użytkownik nie podał liczb"

print(f"Unikalnych znaków: {len(znaki)}")
print(f"Średnia z podanych liczb: {srednia}" )
print("KONIEC")