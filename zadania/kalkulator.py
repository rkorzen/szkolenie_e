"""
Napisz skrypt, który będzie oferował proste obliczenia na zadanych danych wejsciowych:

Witaj w kalkulatorze!
Jaką operację chcesz wykonać (+-/*)? *
Podaj arg a: 10
Podaj arg b: 12
Wynik: 120

if warunek:
   cos tam

input("prompt")

def nazwa(arg,...)
   cialo funkcji

"""

def add(a, b, *args):
    wynik = a + b
    wynik += sum(args)  # wynik = wynik + sum(args)
    return wynik

def sub(a, b, *args):
    wynik = a - b
    wynik = wynik - sum(args)
    return wynik

def mul(a, b, *args):
    wynik = a * b
    for el in args:
        wynik = wynik * el

    return wynik

def div(a, b, *args):
    """wypadałoby by sprawdzić czy nie ma dzielenia przez 0"""
    wynik = a / b
    for el in args:
        wynik = wynik / el
    return wynik

def get_data():
    operacja = input("Jaką operację chcesz wykonać (+-/*)? ")
    a = int(input("Podaj arg a: "))
    b = int(input("Podaj arg b: "))
    args = []
    while True:
        el = input("Podaj kolejny element: ")
        if el == "":
            break
        el = int(el)
        args.append(el)

    return operacja, a, b, args

operacje = {
    "+": add, 
    "-": sub,
    "*": mul,
    "/": div
}
lista_operacji=[add, sub, mul, div]
print("przestrzen nazw:", dir())
print("wartosc w __name__", __name__)
if __name__ == "__main__":

    print("Witaj w kalkulatorze!")
    operacja, a, b, args = get_data()
    # a = int(a)
    # funkcja = operacje[operacja]
    # wynik = funkcja(a, b)

    wynik = operacje[operacja](a, b, *args)
    print(f"Wynik: {wynik}")

