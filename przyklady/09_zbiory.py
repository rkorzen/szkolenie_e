# set

print({1, 2, 3, 1, 2, 3})

print({"c", 1, "3", "a", "cd"})


A = {1, 2, 3}
B = {2, 3, 4}

print(A & B)
print(A | B)
print(A - B)
print(B - A)
print(A ^ B)  # roznica symetrycza - elemty ktore sa albo w A albo w B 
              # ale nie w A i B jednocześnie


C = {1, 2, 3, 4, 5, 6}

print(A.issubset(C))
print(C.issuperset(B))