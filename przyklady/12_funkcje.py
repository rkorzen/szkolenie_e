
def hello():
    print("Hello World")
    return "1"


hello()
hello()


print(hello)
to_co_zwraca_hello = hello()
print(to_co_zwraca_hello)

to_co_zwraca_print = print("to co drukuje print")
print(to_co_zwraca_print)



def hello_name(name="World"):
    print(f"Hello {name}")
    return "1"

hello_name("Rafał")
hello_name("Gosia")
hello_name()


def sumator(a, b):
    """To jest docstring, czyli dokumentacja tej funkcji
    
    a: liczba
    b: liczba

    funkcja zwraca sume a i b
    """
    return a + b

wynik = sumator(1, 2)
print(wynik)

print(help(sumator))