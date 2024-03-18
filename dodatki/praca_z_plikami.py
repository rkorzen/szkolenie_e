with open("dane.csv", "w", encoding="CP1251") as f:
    dane = """
nazwa,wartosc
tekst,zażółć gęślą jaźń  
""".encode("CP1251")
    
    f.write(dane)