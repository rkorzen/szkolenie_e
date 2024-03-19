"""
5! = 5 * 4! = 5 * 4 * 3! ... = 5 * 4 * 3 * 2 * 1 * 1

0! = 1

"""

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)
    

def licznik(start):
    print(start)
    licznik(start + 1)

licznik(1)
