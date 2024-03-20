structura = [
    {
        "dane": [1, 2, 3]
    },

    {
        "dane": [5, 2, 3]
    }
]
print(type(structura))
import json

print(dir(json))

result_json = json.dumps(structura)

print(result_json)
print(type(result_json))


text_json = '[{"dane": [1, 2, 3]}, {"dane": [5, 2, 3]}]'

obiekt = json.loads(text_json)

print(type(obiekt))



with open("waluty.json") as f:
    dane = json.load(f)

for waluta in dane[0]["rates"]:
    print(waluta["currency"], waluta["mid"])
