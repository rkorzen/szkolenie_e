
lista = [1, 2, 3, [4, 5, [1, 2, 3, [1, 2], 1]]]

def splaszcz_lista(kolekcja):
    wynik = []
    for el in kolekcja:
        if type(el) == int:  # isinstance(el, int)
            wynik.append(el)
        else:
            for el_ze_spl in splaszcz_lista(el):
                wynik.append(el_ze_spl)
    return wynik


def test_splaszcz_lista():
    assert splaszcz_lista(kolekcja=[]) == []
    assert splaszcz_lista(kolekcja=[1,2,3]) == [1, 2, 3]
    assert splaszcz_lista(kolekcja=(1, 2, 3)) == [1, 2, 3]
    assert splaszcz_lista(kolekcja=lista) == [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]