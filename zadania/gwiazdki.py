"""1:
*
**
***
****
*****
2:
******
*****
****
***
**
*
3:
* * * * * * 
 * * * * * *
* * * * * * 
 * * * * * *

"""

print("1:")

for i in range(1, 6):
    # for j in range(i):
    #     print("*", end="")
    # print()

    print("*" * i)

print("2:")
for i in range(1, 7):
    print("*" * (7 - i))
# "*" * 5

wzor = "* * * * * * "

for i in range(1, 5):
    if i % 2 == 0:
        print(f" {wzor}")
    else:
        print(wzor)
