# Szkolenie z podstaw Pythona dla księgowych - 18.03.2024

## Materiały Szkoleniowe

- **Zdalne Repozytorium:** [GitHub - szkolenie_e](https://github.com/rkorzen/szkolenie_e)

Aby pobrać materiały wejdź na powyższy link, kliknij zielony przycisk Code i wybierz opcję Download ZIP. Po pobraniu plików, rozpakuj archiwum i otwórz folder w dowolnym edytorze kodu.

Możesz też użyć gita do sklonowania repozytorium na swój komputer. 
By to zrobić musisz mieć zainstalowanego gita na swoim komputerze. 

W terminalu wpisz:

```bash
git clone https://github.com/rkorzen/szkolenie_e.git 
```

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


**Funkcje w Pythonie: Klucz do Efektywnego Kodowania**

W świecie programowania, funkcje stanowią fundament tworzenia czytelnego, modułowego i efektywnego kodu. W języku Python, funkcje są wszechobecne i stanowią nieodłączny element programowania zarówno dla początkujących, jak i doświadczonych programistów. W tym artykule przyjrzymy się roli funkcji w Pythonie oraz ich istotnym cechom.

**Czym są funkcje w Pythonie?**

W Pythonie, funkcje są blokami kodu, które wykonują określone zadanie po wywołaniu. Mogą przyjmować argumenty, przetwarzać dane oraz zwracać wyniki. Definiowanie funkcji rozpoczyna się od słowa kluczowego `def`, po którym podaje się nazwę funkcji i ewentualne parametry.

**Podstawowe cechy funkcji w Pythonie:**

1. **Modularyzacja kodu:** Funkcje pozwalają na podział programu na mniejsze, bardziej zrozumiałe części. Dzięki temu kod staje się bardziej czytelny i łatwiejszy w utrzymaniu.

2. **Parametry:** Funkcje mogą przyjmować zero lub więcej parametrów. Parametry mogą być obowiązkowe lub opcjonalne, a nawet mogą posiadać wartości domyślne.

3. **Zasięg zmiennych:** Zmienne zdefiniowane wewnątrz funkcji mają zasięg lokalny i nie są dostępne poza nią, chyba że zostaną zadeklarowane jako globalne.

4. **Zwracanie wartości:** Funkcje mogą zwracać wartość za pomocą słowa kluczowego `return`. W Pythonie funkcja może zwrócić jedną lub więcej wartości.

5. **Rekurencja:** Python obsługuje rekurencyjne wywoływanie funkcji, co pozwala na eleganckie rozwiązanie wielu problemów, takich jak obliczanie silni czy przeszukiwanie drzew.

**Przykład: Funkcja obliczająca silnię:**

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print("Factorial of 5 is:", result)
```

W powyższym przykładzie funkcja `factorial` oblicza silnię liczby `n` za pomocą rekurencji.


**1. Funkcja przyjmująca parametry pozycyjne:**

Parametry pozycyjne są najbardziej podstawowym rodzajem parametrów funkcji. Ich wartości są przypisywane na podstawie kolejności, w jakiej są przekazywane podczas wywoływania funkcji.

```python
def greet(name, age):
    print(f"Hello {name}! You are {age} years old.")

greet("Alice", 30)
```

W tym przykładzie `name` i `age` są parametrami pozycyjnymi. Przekazując wartości `"Alice"` i `30` podczas wywoływania funkcji `greet`, przypisywane są one odpowiednio do parametrów `name` i `age`.

**2. Funkcja przyjmująca parametry nazwane:**

Parametry nazwane (keyword arguments) są przypisywane na podstawie ich nazw podanych podczas wywoływania funkcji.

```python
def greet(name, age):
    print(f"Hello {name}! You are {age} years old.")

greet(age=30, name="Bob")
```

W tym przykładzie argumenty są przekazywane z nazwami `age` i `name`, co pozwala na dowolną kolejność podawania argumentów.

**3. Funkcja przyjmująca *args:**

`*args` pozwala funkcji przyjmować dowolną liczbę pozycyjnych argumentów. Argumenty te są przekazywane do funkcji jako krotka (tuple).

```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_all(1, 2, 3, 4, 5)
print("Sum:", result)
```

W tym przykładzie funkcja `sum_all` może przyjąć dowolną liczbę argumentów pozycyjnych. Przekazane argumenty są zsumowane, niezależnie od ich liczby.

**4. Funkcja przyjmująca **kwargs:**

`**kwargs` pozwala funkcji przyjmować dowolną liczbę nazwanych argumentów. Argumenty te są przekazywane do funkcji jako słownik (dict).

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
```

W tym przykładzie funkcja `print_info` przyjmuje nazwane argumenty i wypisuje je w formie klucz-wartość. Dzięki temu możemy przekazać funkcji różne parametry w postaci nazwanych argumentów.

## OOP

**Klasy w Pythonie: Budowanie Struktur i Hierarchii Obiektów**

W świecie programowania obiektowego, klasy są kluczowym elementem, który umożliwia tworzenie struktur danych oraz hierarchii obiektów. W języku Python, koncepcja klas jest niezwykle ważna i elastyczna, pozwalając programistom na tworzenie zarówno prostych, jak i złożonych systemów.

**Definiowanie Klas:**

Klasy w Pythonie definiuje się przy użyciu słowa kluczowego `class`, po którym podaje się nazwę klasy. Klasa może zawierać atrybuty klasowe oraz metody.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car: {self.make} {self.model}")
```

W powyższym przykładzie definiujemy klasę `Car`, która ma atrybuty `make` i `model`, oraz metodę `display_info`, która wyświetla informacje o samochodzie.

**Atrybuty Klasowe i Atrybuty Instancji:**

Atrybuty klasy są wspólne dla wszystkich instancji danej klasy, podczas gdy atrybuty instancji są unikatowe dla każdej instancji.

```python
class Car:
    wheels = 4  # Atrybut klasowy

    def __init__(self, make, model):
        self.make = make  # Atrybut instancji
        self.model = model  # Atrybut instancji
```

W tym przykładzie `wheels` jest atrybutem klasowym, który jest wspólny dla wszystkich samochodów, natomiast `make` i `model` są atrybutami instancji, które mogą się różnić dla każdego samochodu.

**Proste Dziedziczenie:**

Dziedziczenie umożliwia tworzenie nowych klas na podstawie istniejących klas. Klasa dziedzicząca (potomna) dziedziczy atrybuty i metody klasy nadrzędnej (bazowej).

```python
class ElectricCar(Car):  # Dziedziczenie
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def display_info(self):  # Przeciążanie metody
        print(f"Electric Car: {self.make} {self.model}, Battery: {self.battery_capacity} kWh")
```

W tym przykładzie klasa `ElectricCar` dziedziczy po klasie `Car`, a metoda `display_info` została przeciążona, aby uwzględnić informacje o pojemności baterii dla samochodu elektrycznego.

**Proste Przeciążanie Operatorów:**

Przeciążanie operatorów umożliwia definiowanie własnych zachowań dla operatorów Pythona w ramach naszych klas.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Przeciążanie operatora dodawania
        return Point(self.x + other.x, self.y + other.y)

point1 = Point(1, 2)
point2 = Point(3, 4)
result = point1 + point2
print("Result:", result.x, result.y)
```

W powyższym przykładzie operator dodawania `+` został przeciążony dla klasy `Point`, co pozwala na dodawanie dwóch punktów, zwracając nowy punkt o współrzędnych będących sumą współrzędnych punktów dodawanych.


## Wersja wykonywalna pliku

```bash
python -m venv venv
venv\Scripts\activate

pip install pyinstaller

pyinstaller --onefile <nazwa pliku>

py -3.12 -m pip install pyinstaller 
```

## PEP 8

PEP 8 to oficjalny zbiór zaleceń dotyczących stylu kodowania w języku Python. Można go znaleźć pod adresem [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/).

**PEP 8: Podstawowe Zasady Stylu Kodowania w Pythonie**

PEP 8 to oficjalny dokument zawierający zalecenia dotyczące stylu kodowania w języku Python. Opracowany przez autora samego Pythona, Guido van Rossuma, oraz Barry'ego Warsaw, PEP 8 jest podstawowym punktem odniesienia dla programistów Pythona w kwestii tworzenia czytelnego, konsekwentnego i łatwego w utrzymaniu kodu.

**Dlaczego PEP 8 jest ważny?**

Konsekwentne stosowanie zasad PEP 8 przynosi wiele korzyści dla projektów Pythonowych:

1. **Czytelność kodu:** Stosowanie spójnego stylu kodowania ułatwia czytanie i zrozumienie kodu, zarówno dla programistów, którzy go piszą, jak i dla osób pracujących nad nim w przyszłości.

2. **Łatwiejsze utrzymanie:** Konsekwentny styl kodowania ułatwia debugowanie, testowanie i wprowadzanie zmian w kodzie, co przyczynia się do jego długoterminowej trwałości.

3. **Łatwiejsza współpraca:** Przestrzeganie zasad PEP 8 ułatwia współpracę z innymi programistami, ponieważ wszyscy stosują te same zasady formatowania.

**Podstawowe Zasady PEP 8:**

1. **Wcięcia:** Używaj wcięć o długości czterech spacji, unikaj tabulatorów.

2. **Spacje vs. Tabulatory:** Unikaj mieszania spacji i tabulatorów do tworzenia wcięć. Stosuj spacje jako preferowany sposób wcięcia.

3. **Długość linii:** Linie kodu nie powinny być dłuższe niż 79 znaków. Długie instrukcje można podzielić za pomocą linii kontynuacji lub podziału logicznego.

4. **Nazewnictwo:** Używaj zrozumiałego i konsekwentnego nazewnictwa dla zmiennych, funkcji, klas i modułów. Stosuj snake_case dla nazw zmiennych i funkcji, oraz CamelCase dla nazw klas.

5. **Importy:** Importy powinny być grupowane w następującej kolejności: standardowe moduły biblioteki Pythona, moduły zainstalowane przez użytkownika, lokalne moduły. Importy powinny być umieszczone na początku pliku.

6. **Puste linie:** Dodawaj puste linie w celu rozdzielenia logicznych bloków kodu wewnątrz funkcji, metod oraz na końcu plików.

7. **Komentarze:** Dodawaj komentarze, które wyjaśniają skomplikowane fragmenty kodu lub jego intencje. Komentarze powinny być jasne i zwięzłe.

PEP 8 to więcej niż zbiór zasad formatowania kodu. Jest to wyraz dojrzałości społeczności Pythona, która docenia czytelność, klarowność i współpracę. Stosowanie zasad PEP 8 to nie tylko dobry nawyk, ale także sposób na tworzenie lepszego oprogramowania w środowisku Pythona.

### Narzędzia

```bash
pip install flake8
pip install black

flake8 <nazwa pliku>
flake8 

black <nazwa pliku>
black .
```

**Flake8 i Black: Narzędzia do Wspierania Zgodności z PEP 8**

Flake8 i Black są dwoma popularnymi narzędziami w świecie Pythona, które pomagają programistom utrzymywać zgodność z zasadami PEP 8 oraz poprawiają jakość kodu poprzez automatyczne sprawdzanie i formatowanie.

**Flake8:**

Flake8 jest narzędziem do statycznego sprawdzania kodu w języku Python. Integruje kilka narzędzi sprawdzających, w tym pyflakes, pycodestyle (wcześniej znany jako pep8) oraz McCabe, umożliwiając kompleksowe analizowanie kodu pod kątem zgodności z PEP 8 oraz znajdowanie potencjalnych błędów i problemów w kodzie.

Korzyści z korzystania z Flake8 obejmują:

- Automatyczne sprawdzanie kodu pod kątem zgodności z PEP 8.
- Wykrywanie potencjalnych błędów i problemów w kodzie.
- Integracja z wieloma edytorami kodu i narzędziami do zarządzania kodem źródłowym.

**Black:**

Black to narzędzie do automatycznego formatowania kodu w języku Python. Jego celem jest zapewnienie spójnego i zgodnego z zasadami PEP 8 formatowania kodu poprzez automatyczne stosowanie odpowiednich wcięć, odstępów, linii pustych itp. Black działa jako narzędzie wiersza poleceń oraz jako wtyczka dla wielu popularnych edytorów kodu.

Korzyści z korzystania z Black obejmują:

- Automatyczne formatowanie kodu, co eliminuje potrzebę ręcznego dbania o jego spójność i zgodność z PEP 8.
- Umożliwia skupienie się na samej logice i funkcjonalności kodu, zamiast martwienia się o jego formatowanie.
- Zapewnia spójny styl kodowania w całym projekcie, niezależnie od liczby autorów i edytorów.

W skrócie, zarówno Flake8, jak i Black są potężnymi narzędziami, które pomagają programistom utrzymywać wysoką jakość kodu oraz zgodność z zasadami PEP 8. Flake8 pomaga w statycznym sprawdzaniu kodu, podczas gdy Black automatycznie formatuje kod, co pozwala programistom skupić się na samej logice i funkcjonalności kodu. Dzięki nim utrzymanie czystego, czytelnego i zgodnego z zasadami PEP 8 kodu staje się prostsze i bardziej efektywne.

## Dokumentacja SQLAlchemy

Dokumentacja SQLAlchemy dostępna jest pod adresem [https://docs.sqlalchemy.org/en/20/](https://docs.sqlalchemy.org/en/20/).

## Materiały dodatkowe:

[tutaj](materiały dodatkowe)