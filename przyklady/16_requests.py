# pip install requests
import requests
import csv

url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"

response = requests.get(url)

print(response.status_code)

dane = response.json()

print(dane[0]["rates"][0]["mid"])
for waluta in dane[0]["rates"]:
    if waluta["code"] == "EUR":
        print(waluta["code"], waluta["mid"])



with open("kursy.csv", "w") as plik:
    writer = csv.DictWriter(plik, fieldnames=["currency", "code", "mid"])
    writer.writeheader()
    writer.writerows(dane[0]["rates"])