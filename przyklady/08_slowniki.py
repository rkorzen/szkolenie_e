slownik = {
    "a": 1,
    "b": 2,
}

slownik["c"] = 3

print(slownik["a"])

# print(slownik["d"])
print(slownik.get("d"))

# print(dir(slownik))
print(slownik)
print(slownik.keys())
print(slownik.values())
print(slownik.items())

print(dict(a=10, b=20))

{  "a b":10 }
# {[1, 2]: 10}

print(hash("ala ma kota"))

# hash([1, 2,3 ]) - to daje błąd