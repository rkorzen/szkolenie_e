"""

Mamy tekst: Ala ma kota

napisz skrypt, który wypisze słownik zawierajacy zliczenia znaków

{
"A": 1,
"l": 1,
"a": 3,
...
}

klucz in slownik
slownik[klucz] = slownik[klucz] + innawartosc

for znak in tekst:
   ...

https://github.com/rkorzen/szkolenie_e   
"""

tekst = "Ala ma kota sds vw9i sldjfnbw 04ipf bs"

# tekst = input("Podaj tekst")
zliczenia = {}

for znak in tekst:
    # if znak in zliczenia:
    #     zliczenia[znak] = zliczenia[znak] + 1
    # else:
    #     zliczenia[znak] = 1
    zliczenia[znak] = zliczenia.get(znak, 0) + 1

print(zliczenia)