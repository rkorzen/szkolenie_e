# pip install requests

import requests

response = requests.get("https://api.nbp.pl")

print(response.content)