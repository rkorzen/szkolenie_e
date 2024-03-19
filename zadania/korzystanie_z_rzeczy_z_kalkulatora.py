from kalkulator import lista_operacji

dane = [[1, 2], [3, 4]]



for para in dane:
    for funkcja in lista_operacji:
        a = para[0]
        b = para[1]
        print(funkcja.__name__, funkcja(a, b))
    print("-"* 40)