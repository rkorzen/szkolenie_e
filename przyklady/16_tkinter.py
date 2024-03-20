import tkinter as tk
from tkinter import ttk
import requests

def get_currency_rate(currency_code):
    url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
    try:
        response = requests.get(url)
        dane = response.json()
        rates = dane[0]["rates"]
        for waluta in rates:
            if waluta["code"] == currency_code:
                return waluta["mid"]
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
