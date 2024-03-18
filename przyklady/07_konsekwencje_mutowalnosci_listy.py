a = [1, 2, 3]
b = a.copy()
c = [5, 6, a]
from copy import deepcopy

d = deepcopy(c)
# b = [1, 2 ,3]

a.append(10)
print(b)
print(d)

