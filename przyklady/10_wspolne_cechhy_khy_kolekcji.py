# podobieństwa
a = [1, 2, 3, 1] # lista 
b = (4, 5 ,6)  # tupla
c = {"a": 1}   # slownik
d = {1, 2, 3}  # zbior
e = "12345"    # napis

print(len(a), len(b), len(c), len(d), len(e))

print(1 in a)
print(1 in b)
print(1 in c)
print("a" in c)
print(1 in d)
print("1" in e)

for i in a:
    print(i)

for key in c:
    print(key)
    print(c[key])

a, b = 1, 2

for k, v in c.items():
    print(k, v)

# różnice

print([1, print, [1, 2], (1, 2), {1, 2}])

# slownik i zbior - ograniczenia na klucze (slowniku) i el zbioru - tylko
# hashowalne

# napis - zawiera tylko napisy
# zbior nie ma porzadku

# zbior, lista, slownik - mutowalne obiekty

