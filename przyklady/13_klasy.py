import datetime
# from datetime import datetime
now = datetime.datetime.now()
print(now)

print(dir(datetime))
print(dir(datetime.datetime))
# print(help(datetime.datetime.now))
class Person:
    """docstring"""

    def __init__(self, imie, wzrost, rok_ur):
        self.imie = imie
        self.wzrost = wzrost
        self.rok_ur = rok_ur

    def __repr__(self):
        return f"{self.imie} ({self.rok_ur})"

    def przedstaw_sie(self):
        print(f"Cześć jestem {self.imie}")

    @property
    def wiek(self):
        now = datetime.datetime.now()
        return now.year - self.rok_ur

franek = Person("Franek", 181, 1980)
gosia = Person("Gosia", 165, 1997)


print(franek)

print([franek])
print(franek.imie)
print(gosia.wzrost)
print(franek.wiek)


gosia.przedstaw_sie()
franek.przedstaw_sie()
print(franek.wiek)



class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    @property
    def obwod(self):
        return self.bok * 4
        
    @obwod.setter
    def obwod(self, value):
        self.bok = value / 4
    
    @property
    def pole(self):
        return self.bok ** 2
    

    def __add__(self, other):
        suma_pol = self.pole + other.pole+
        nowy_kwadrat = Kwadrat(suma_pol**0.5)
        return nowy_kwadrat

    def __gt__(self, other):
        return self.bok > other.bok

kw = Kwadrat(10)
kw2 = Kwadrat(20)

print(kw.obwod)

kw.obwod = 120
print(kw.bok)

print(kw > kw2)


print(kw + kw2)