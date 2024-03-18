# komentarz - to jest ignorowane
x = 1             # x zmienna a 1 to wartość liczbowa typu int, = operator przypisania
y = "1"
text = "Hello"  # text to zmienna, Hello to wartość (tekst - str)

print(text)  # funkcja wbudowana print, () jakieś działąnie -  w tym przypadku wywołanie
print(end="-")
print(text)
print(text)
print(text, x, y, sep="::")



# nawiasy wpływają na kolejność operacji
(1 + 2) * 3
1 + 2 * 3

# funkcje wbudowane mogą byc nadpisane   
print = 1
print(text)