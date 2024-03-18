
# 100x100
"""
and, or

if warunek:
    ...
elif innywarunek:
    ...
elif innywarunek:
   ...
else:
   ...

"""

x = 50
y = 50

if x < 0 or x > 100 or y < 0 or y > 100:
    print("Jestem poza planszą")
elif x <= 10 and y >= 90:
    print("GLR")
elif x >= 90 and y >= 90:
    print("GPR")
elif x >= 90 and y <= 10:
    print("DPR")
elif x <= 10 and y <= 10:
    print("DLR")
elif x <= 10:
    print("LK")
elif y >= 90:
    print("GK")
elif x >= 90:
    print("PK")
elif y <= 10:
    print("DK")
else:
    print("C")

