lista_napisow = ["1", "2", "3", "11", "43"]



# lista_liczb = []
# for napis in lista_napisow:
#     lista_liczb.append(int(napis))

lista_liczb = [int(napis) for napis in lista_napisow]
# lista_liczb = map(int, lista_napisow)

print(lista_liczb)


liczby = [1, 2, 3, 4, 5, 6, 7, 8]

szczesciany_parzystych = []
for liczba in liczby:
    if liczba % 2 == 0:
        szczesciany_parzystych.append(liczba ** 3 )


szczesciany_parzystych = [i ** 3 for i in liczby if i % 2 == 0]

print({i: i**3 for i in liczby  if i % 2 == 0})


from pprint import pprint
pprint(tuple([i*j for j in range(10)] for i in range(10)))