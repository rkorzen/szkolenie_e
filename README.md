# Szkolenie z podstaw Pythona dla księgowych - 18.03.2024

## Materiały Szkoleniowe

- **Zdalne Repozytorium:** [GitHub - szkolenie_e](https://github.com/rkorzen/szkolenie_e)


## Rys historyczny

Python, jeden z najbardziej uniwersalnych i popularnych języków programowania, został stworzony przez Guido van Rossuma na początku lat 90. XX wieku. Pierwsza wersja języka, Python 0.9.0, została opublikowana w lutym 1991 roku. Van Rossum rozpoczął pracę nad Pythonem pod koniec lat 80. jako projekt hobbystyczny, mający na celu stworzenie następcy języka ABC, który byłby zarówno łatwy do nauczenia, jak i potężny w użyciu.

Python zyskał na popularności dzięki swojej prostej składni, co sprawia, że jest łatwy do nauki dla początkujących, jak również dzięki swojej wszechstronności, która pozwala na jego użycie w różnorodnych zastosowaniach, od rozwoju stron internetowych po naukę o danych i sztuczną inteligencję. Język ten zaprojektowano z myślą o czytelności kodu oraz możliwości jego wielokrotnego wykorzystania, co ułatwia zarządzanie dużymi projektami programistycznymi.

W ciągu lat Python przeszedł wiele zmian. Najważniejsze kamienie milowe to wydanie Pythona 2.0 w 2000 roku, które wprowadziło wiele nowych funkcji i usprawnień, oraz Pythona 3.0 w 2008 roku, z jeszcze większymi zmianami, mającymi na celu usunięcie niejasności i redundancji w języku. Migracja z Pythona 2 do Pythona 3 była znacznym wyzwaniem dla wielu projektów, ale ostatecznie przyniosła wiele korzyści, takich jak lepsza obsługa Unicode i bardziej spójna składnia.

Guido van Rossum, często nazywany "Benevolent Dictator For Life" (BDFL) Pythona, zrezygnował ze swojej roli w 2018 roku, przekazując odpowiedzialność za rozwój języka Pythonowej Społeczności. Python jest obecnie zarządzany przez Python Software Foundation (PSF) i rozwijany przez aktywną społeczność programistów.

Dzięki swojej ciągłej ewolucji i aktywnej społeczności użytkowników, Python utrzymuje swoją pozycję jako jeden z czołowych języków programowania, przyciągając zarówno początkujących, jak i doświadczonych programistów.


## Podstawy Pythona

### Zmienne

#### Zasady Nazewnictwa Zmiennych
- Zmienne mogą składać się z liter, cyfr i znaków podkreślenia (np. `ser_1`, `ser1`, `_ser`).
- Nazwy zmiennych nie mogą zaczynać się od cyfr (np. `1_ser` jest niepoprawne).
- Nie mogą być słowami kluczowymi w Pythonie (np. `def = 1` jest niepoprawne). Lista słów kluczowych dostępna jest poprzez wywołanie `help("keywords")` w interpreterze Pythona.

#### Konwencje Nazewnictwa
- Używamy małych liter i rozdzielamy słowa znakami podkreślenia (snake_case), np. `super_dluga_zmienna`.
- Unikamy notacji camelCase (`superDlugaZmienna`) i PascalCase (`SuperDlugaZmienna`).

#### Stałe
- Stałe oznaczamy wielkimi literami, np. `LICZBA_PI = 3.1415`.

### Używanie Zmiennych
- Tworzenie zmiennej: `x = 1`.
- Użycie zmiennej: `print(x)` (jako argument funkcji), `x + 10` (element wyrażenia).

## Typy Zmiennych w Pythonie

Python jako język programowania wysokiego poziomu oferuje różnorodność wbudowanych typów danych, które ułatwiają pracę z różnego rodzaju danymi. Oto krótki opis podstawowych typów zmiennych:

### `int`
Typ `int` (integer, liczba całkowita) reprezentuje liczby całkowite, zarówno dodatnie, jak i ujemne, bez części dziesiętnej. Jest to jeden z najczęściej używanych typów danych w Pythonie, przydatny w różnych operacjach matematycznych i logicznych. Na przykład: `42`, `-23`.

### `float`
Typ `float` odnosi się do liczb zmiennoprzecinkowych, czyli takich, które posiadają część dziesiętną. Umożliwia reprezentację liczb rzeczywistych, co jest niezbędne w obliczeniach naukowych, finansowych czy inżynieryjnych. Przykłady wartości typu `float` to `3.14`, `-0.001`.

### `complex`
Liczby zespolone w Pythonie są reprezentowane przez typ `complex`, który zawiera część rzeczywistą i część urojoną (oznaczaną jako `j`). Liczby te są używane głównie w zaawansowanych obliczeniach matematycznych i inżynieryjnych. Przykładem liczby zespolonej może być `2 + 3j`.

### `str`
Typ `str` reprezentuje ciągi znaków, czyli tekst. Może to być pojedynczy znak, słowo, zdanie lub nawet dłuższy tekst. Ciągi znaków są niezwykle ważne w wielu aspektach programowania, od interakcji z użytkownikiem, przez przetwarzanie danych, po prace z plikami. Python oferuje bogaty zestaw operacji i metod do manipulacji ciągami znaków. Przykład: `"Hello, World!"`.

Każdy z tych typów danych ma swoje zastosowania i jest ważny w różnych kontekstach programistycznych. Python, jako język dynamicznie typowany, automatycznie rozpoznaje typ zmiennej podczas przypisywania jej wartości, co jeszcze bardziej ułatwia pracę z danymi.

### `bool`

Typ `bool` (boolean) reprezentuje wartość logiczną, która może być albo `True` (prawda), albo `False` (fałsz). Jest to podstawowy typ danych używany w operacjach logicznych i warunkowych, umożliwiający kontrolę przepływu programu i podejmowanie decyzji.

W Pythonie wartości logiczne mogą być również traktowane jako liczby w kontekście matematycznym, gdzie `True` jest równoważne `1`, a `False` jest równoważne `0`. Dzięki temu możliwe jest bezpośrednie używanie wartości boolowskich w obliczeniach matematycznych i logicznych.

Typ `bool` jest szczególnie przydatny w instrukcjach warunkowych (`if`, `elif`, `else`), pętlach (`while`, `for`) oraz w wyrażeniach logicznych łączących warunki za pomocą operatorów logicznych takich jak `and`, `or`, `not`. 

## Formatowanie Napisów

Formatowanie napisów w Pythonie jest ważnym aspektem programowania, szczególnie gdy potrzebujemy dynamicznie wstawiać wartości do ciągów tekstowych. Python oferuje kilka metod formatowania napisów, które mogą być używane w różnych sytuacjach:

### Stary styl formatowania (`%` operator)
Styl ten, znany również jako operator procentowy, pochodzi z języka C. Umożliwia wstawianie wartości do ciągu znaków za pomocą specjalnych znaczników formatujących. Na przykład:
```python
imie = 'Jan'
wiek = 30
print("Witaj, %s. Masz %d lat." % (imie, wiek))
```
Jest to najstarsza metoda formatowania w Pythonie i choć jest nadal wspierana, to zaleca się korzystanie z nowszych metod.

### Metoda `str.format()`
Ta metoda została wprowadzona w Pythonie 2.6 i jest bardziej elastyczna oraz czytelna niż stary styl formatowania. Pozwala na wstawianie wartości w miejsce nawiasów klamrowych `{}` w ciągu znaków:
```python
imie = 'Jan'
wiek = 30
print("Witaj, {}. Masz {} lat.".format(imie, wiek))
```
Metoda `format` oferuje również zaawansowane możliwości formatowania, takie jak określanie precyzji liczb zmiennoprzecinkowych, wyrównywanie tekstu czy formatowanie dat.

### Literały napisów sformatowanych (f-stringi)

Wprowadzone w Pythonie 3.6, f-stringi stanowią szybką i czytelną metodę formatowania napisów. Aby użyć tej metody, przed ciągiem znaków stawiamy literę `f`, a wewnątrz nawiasów klamrowych `{}` umieszczamy zmienne lub wyrażenia, które mają zostać wstawione:
```python
imie = 'Jan'
wiek = 30
print(f"Witaj, {imie}. Masz {wiek} lat.")
```
F-stringi są obecnie zalecaną metodą formatowania napisów w Pythonie, ze względu na ich wydajność i łatwość w użyciu.

### Template strings
Klasa `Template` z modułu `string` oferuje jeszcze jedną metodę formatowania, która jest mniej elastyczna, ale może być bezpieczniejsza przy obróbce napisów pochodzących od użytkowników. Używa specjalnej składni z placeholderami w postaci `$zmienna`:
```python
from string import Template
imie = 'Jan'
wiek = 30
szablon = Template("Witaj, $imie. Masz $wiek lat.")
print(szablon.substitute(imie=imie, wiek=wiek))
```
Ta metoda jest mniej popularna w codziennym użyciu, ale znajduje swoje zastosowanie w specyficznych przypadkach.

Każda z tych metod ma swoje miejsce i może być użyteczna w zależności od konkretnego przypadku użycia i preferencji programisty.

Więcej informacji o formatowaniu napisów można znaleźć na [pyformat.info](https://pyformat.info/).

## Sterowanie Przepływem

### Wyrażenia Warunkowe

#### Najprostszy Przypadek
```python
if warunek:
    blok_instrukcji
# Kolejne instrukcje
```

#### if else
Po dwukropku nowa linia i kod przesunięty o 4 spacje w prawo.
```python
if warunek:
    blok_instrukcji
else:
    inny_blok_instrukcji
# Kolejne instrukcje
```

#### if elif else
```python
if warunek_1:
    blok_instrukcji
elif warunek_2:
    blok_instrukcji
else:
    inny_blok_instrukcji
# Kolejne instrukcje
```

### Pętle

#### while
W pętli `while` blok kodu jest wykonywany tak długo, jak spełniony jest dany warunek. Opcjonalnie można użyć instrukcji `break` do natychmiastowego przerwania działania pętli lub `continue` do przerywania aktualnego obrotu pętli i przejścia do kolejnego sprawdzenia warunku. Po zakończeniu pętli, jeśli zdefiniowano blok `else`, jest on wykonany.
```python
while warunek:
    blok_kodu
    # Opcjonalnie: break (przerywa działanie pętli), continue (przerywa obrot pętli)
else:
    # Blok kodu po pętli (opcjonalnie)
# Kolejne instrukcje
```

#### for
Pętla `for` służy do iterowania po elementach sekwencji (takich jak listy, krotki, słowniki, zbiory, ciągi znaków) lub innych obiektów iterowalnych. W każdej iteracji pętli zmienna iteracyjna przyjmuje wartość kolejnego elementu z sekwencji, a blok kodu jest wykonany. Podobnie jak w przypadku pętli `while`, `break` i `continue` mogą być użyte do kontrolowania przepływu pętli, a opcjonalny blok `else` jest wykonany po wyczerpaniu sekwencji, chyba że pętla została przerwana instrukcją `break`.

```python
for zmienna in sekwencja:
    blok_kodu
    # Opcjonalnie: break (przerywa działanie pętli), continue (przerywa obrot pętli)
else:
    # Blok kodu po pętli (opcjonalnie)
# Kolejne instrukcje
```

W pętli `for` można również używać funkcji `range()` do generowania sekwencji liczb, co jest szczególnie przydatne w przypadkach, gdy potrzebujemy wykonać blok kodu określoną liczbę razy. Na przykład, `for i in range(5):` pozwoli na pięciokrotne wykonanie bloku kodu, przy czym zmienna `i` przyjmie wartości od 0 do 4.


# Kolekcje w Pythonie: Przewodnik po Podstawowych Typach

Python oferuje potężny zestaw wbudowanych typów kolekcji, które umożliwiają przechowywanie, dostęp i manipulację zbiorami danych w różnorodny i efektywny sposób. Każdy typ kolekcji ma swoje unikalne właściwości i zastosowania, co czyni Pythona niezwykle elastycznym językiem programowania. W tym artykule przyjrzymy się bliżej czterem podstawowym typom kolekcji w Pythonie: listom, krotkom, słownikom oraz zbiorom.

## Listy

Listy są jednym z najczęściej używanych typów kolekcji w Pythonie. Są one uporządkowane, zmienne i mogą zawierać elementy różnych typów. Listy są idealne do przechowywania kolekcji elementów, które mogą się zmieniać podczas wykonywania programu. Można je łatwo modyfikować, dodając nowe elementy, usuwając istniejące lub zmieniając wartość elementów.

```python
moja_lista = [1, "Python", 3.14]
moja_lista.append("nowy element")
print(moja_lista)
```

## Krotki

Krotki są podobne do list, ale są niemutowalne, co oznacza, że nie można ich zmieniać po utworzeniu. Krotki są idealne do przechowywania zestawów wartości, które nie powinny się zmieniać przez cały czas działania programu. Ich niemutowalność sprawia, że są one szybsze niż listy i mogą być używane jako klucze w słownikach.

```python
moja_krotka = (1, "Python", 3.14)
print(moja_krotka)
```

## Słowniki

Słowniki w Pythonie to struktury danych, które przechowują pary klucz-wartość. Są one nieuporządkowane, co oznacza, że elementy nie są przechowywane w żadnej konkretnej kolejności. Słowniki są niezwykle użyteczne, gdy potrzebujemy szybkiego dostępu do elementów na podstawie unikalnego klucza. Słowniki pozwalają na efektywne dodawanie, usuwanie i modyfikację par klucz-wartość.

```python
moj_slownik = {"klucz1": "wartość1", "klucz2": 2, "klucz3": 3.14}
print(moj_slownik["klucz1"])
```

## Zbiory

Zbiory są nieuporządkowaną kolekcją unikalnych elementów. Są one podobne do matematycznych zbiorów i mogą być używane do operacji takich jak unia, przecięcie, różnica. Zbiory są idealne do usuwania duplikatów z kolekcji danych oraz do sprawdzania przynależności elementów.

```python
moj_zbior = {1, 2, 3, 4, 5}
print(moj_zbior)
```

# mutowalność na przykładzie list

Mutowalność list w Pythonie oznacza, że obiekty list mogą być zmieniane po ich utworzeniu. Ta cecha wpływa na sposób pracy z listami oraz na zachowanie programu w wielu kontekstach. Oto kilka kluczowych konsekwencji mutowalności list:

### Modyfikacja w Miejscu
Możemy zmieniać, dodawać lub usuwać elementy listy bez potrzeby tworzenia nowej listy. Działa to efektywnie, ponieważ nie wymaga dodatkowej pamięci do przechowywania zmodyfikowanej listy.

```python
lista = [1, 2, 3]
lista.append(4)  # Dodanie elementu
lista[0] = "zmieniony"  # Zmiana elementu
del lista[2]  # Usunięcie elementu
```

### Dzielenie Referencji
Dwie lub więcej zmiennych mogą odnosić się do tej samej listy. Oznacza to, że zmiana dokonana przez jedną zmienną będzie widoczna dla innych zmiennych odnoszących się do tej listy.

```python
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print(lista1)  # [1, 2, 3, 4]
```

### Niezamierzone Efekty Uboczne
Ze względu na dzielenie referencji, modyfikacja listy przez jedną część programu może nieoczekiwanie wpłynąć na inne części programu, które używają tej samej listy. Może to prowadzić do trudnych do zidentyfikowania błędów.

### Kwestie Wątkowości
W wielowątkowych aplikacjach mutowalne struktury danych, takie jak listy, mogą wymagać dodatkowych mechanizmów synchronizacji, aby zapewnić spójność danych podczas jednoczesnego dostępu z różnych wątków.

### Użycie jako Kluczy Słownikowych
Listy nie mogą być używane jako klucze w słownikach z powodu ich mutowalności. Python wymaga, by klucze słowników były niemutowalne (takie jak krotki, liczby, czy ciągi znaków), aby zapewnić ich unikalność i niezmienność przez cały czas życia słownika.

### Optymalizacja Pamięci i Wydajności
Chociaż mutowalność list pozwala na efektywne modyfikacje, może też prowadzić do nieoptymalnego zużycia pamięci w niektórych przypadkach. Python próbuje zarządzać tym poprzez alokację dodatkowego miejsca przy rozszerzaniu listy, ale to z kolei może czasami wpłynąć na wydajność.

Zrozumienie mutowalności i jej konsekwencji jest kluczowe przy projektowaniu efektywnych i bezbłędnych programów w Pythonie. Należy zwracać uwagę na sposób, w jaki zmiany w listach mogą wpływać na program, oraz stosować odpowiednie praktyki programistyczne, aby unikać niezamierzonych efektów ubocznych.

### inne mutowalne typy wbudowane:

Zbiór i słownik. 

## Wybieranie i slicing w kolekcjach

Wybieranie elementów i operacja slicing (krojenie) to dwie podstawowe techniki pracy z kolekcjami w Pythonie, pozwalające na dostęp do elementów lub ich podzbiorów. Sposób ich użycia różni się w zależności od typu kolekcji, takich jak listy, słowniki i zbiory.

### Listy

**Wybieranie elementów:** Możemy wybrać pojedynczy element z listy, używając indeksu elementu w nawiasach kwadratowych. Indeksy w Pythonie zaczynają się od 0 dla pierwszego elementu. Możemy również użyć indeksów ujemnych, aby odwołać się do elementów od końca listy, gdzie `-1` jest ostatnim elementem.

```python
lista = ['a', 'b', 'c', 'd']
print(lista[1])  # Wybiera drugi element: 'b'
print(lista[-1])  # Wybiera ostatni element: 'd'
```

**Slicing:** Slicing pozwala na wybieranie zakresu elementów z listy. Używa się do tego składni `[start:stop:step]`, gdzie `start` jest indeksem początkowym zakresu (włącznie), `stop` jest indeksem końcowym (wyłącznie), a `step` określa krok przeskoku między elementami.

```python
print(lista[1:3])  # Wynik: ['b', 'c']
print(lista[::2])  # Wynik: ['a', 'c'] - wybiera co drugi element
```

### Słowniki

**Wybieranie elementów:** W słownikach dostęp do wartości odbywa się poprzez klucz, a nie indeks. Używa się klucza w nawiasach kwadratowych do wybrania wartości powiązanej z tym kluczem.

```python
slownik = {'klucz1': 'wartosc1', 'klucz2': 'wartosc2'}
print(slownik['klucz1'])  # Wynik: 'wartosc1'
```

**Slicing:** Operacje slicingu nie są bezpośrednio dostępne w słownikach, ponieważ są one nieuporządkowane do Pythona 3.7. Od Pythona 3.7, słowniki zachowują kolejność wstawienia elementów, jednak nadal nie można używać slicingu tak jak w listach. Można jednak iterować po kluczach, wartościach lub parach klucz-wartość za pomocą metod takich jak `.keys()`, `.values()`, i `.items()`.

### Zbiory

**Wybieranie elementów:** Zbiory w Pythonie są nieuporządkowane, co oznacza, że nie można wybrać pojedynczego elementu za pomocą indeksu ani przeprowadzić operacji slicingu.

```python
zbior = {1, 2, 3, 4}
# Nie można zrobić: zbior[0] - to zwróci błąd
```

**Operacje na zbiorach:** Mimo że bezpośredni dostęp do elementów jest niemożliwy, zbiory oferują bogaty zestaw operacji matematycznych takich jak unia, przecięcie, różnica symetryczna i różnica, które pozwalają na efektywną manipulację zbiorami.

W zależności od typu kolekcji, Python oferuje różne mechanizmy dostępu i manipulacji danymi, co pozwala na elastyczne i efektywne programowanie.


## wyrażenia listowe, słownikowe (comprehensions)





# PRACA Z PLIKAMI

Praca z plikami w Pythonie jest kluczowym aspektem wielu programów, pozwalającym na odczyt, zapis i manipulację danymi przechowywanymi w plikach na dysku. Poniżej przedstawiam podstawowe operacje związane z pracą z plikami w Pythonie:

1. **Otwieranie pliku**: Aby pracować z plikiem, najpierw musimy go otworzyć. Służy do tego wbudowana funkcja `open()`. Przyjmuje ona ścieżkę do pliku oraz tryb otwarcia. Na przykład:

```python
file = open("example.txt", "r")  # Otwarcie pliku do odczytu
```

2. **Tryby otwarcia pliku**: Python obsługuje różne tryby otwarcia pliku, takie jak:
   - `"r"`: Odczyt - domyślny tryb, otwiera plik do odczytu.
   - `"w"`: Zapis - otwiera plik do zapisu. Jeśli plik już istnieje, jego zawartość zostanie usunięta. Jeśli plik nie istnieje, zostanie utworzony.
   - `"a"`: Dopisywanie - otwiera plik do dopisywania. Nowa zawartość jest dodawana na końcu pliku.
   - `"r+"`: Odczyt i zapis - otwiera plik do odczytu i zapisu.
   - `"b"`: Tryb binarny - otwiera plik w trybie binarnym, który jest używany do plików nie-tekstowych (np. obrazy, pliki dźwiękowe).

3. **Odczyt i zapis danych**: Po otwarciu pliku możemy odczytywać jego zawartość lub zapisywać dane do niego. Do tego celu używamy metod takich jak `read()`, `readline()`, `readlines()` do odczytu, oraz `write()` do zapisu danych. Na przykład:

```python
# Odczyt całej zawartości pliku
content = file.read()

# Odczyt pojedynczej linii
line = file.readline()

# Odczyt wszystkich linii do listy
lines = file.readlines()

# Zapis danych do pliku
file.write("Nowa zawartość.")
```

4. **Zamykanie pliku**: Po zakończeniu pracy z plikiem ważne jest jego zamknięcie, aby zwolnić zasoby systemowe. Służy do tego metoda `close()`:

```python
file.close()
```

5. **Blok `with`**: Blok `with` jest często używany w Pythonie do otwierania plików. Zapewnia on automatyczne zamknięcie pliku po opuszczeniu bloku, nawet jeśli wystąpi błąd podczas działania w bloku `with`. Jest to zalecana praktyka:

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# Tutaj plik zostanie automatycznie zamknięty
```

6. **Obsługa błędów**: Podczas pracy z plikami istnieje wiele czynników, które mogą spowodować błędy, takie jak brak pliku, brak dostępu do pliku itp. Dobrą praktyką jest obsługa tych błędów za pomocą instrukcji `try` i `except`.

To podstawowe informacje dotyczące pracy z plikami w Pythonie. Praca z plikami jest niezbędna w wielu aplikacjach, szczególnie w operacjach na danych, jak czytanie plików z danymi wejściowymi, zapisywanie wyników, itp.


# Funkcje

def nazwa():
   cialo funkcji


def nazwa(param, param2):
   cialo funkcji


def nazwa(param, param2="wartosc domyslna"):
   cialo funkcji

nazwa() 


def sumator(a, b, *args):
   args - tupla

   pass

sumator(1, 2)
sumator(1, 2, 1, 2, 3)


def foo(*argumenty):
    ...


foo()
foo(1, 2)


## OOP

class <nazwa>:
   ...

class Person:  # klasa
    pass

person = Person()  # instancja, obiekt

int("10")


## wersja wykonywalna pliku
python -m venv venv
venv\Scripts\activate

pip install pyinstaller

pyinstaller --onefile <nazwa pliku>

py -3.12 -m pip install pyinstaller 


## PEP 8

https://peps.python.org/pep-0008/

flake8 - sprawdzanie
black - formatowanie

pip install flake8
pip install black

flake8 <nazwa pliku>
flake8 