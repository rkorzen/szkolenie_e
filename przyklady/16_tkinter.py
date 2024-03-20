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


def on_submit():
    currency_code = currency_combobox.get()
    currency_rate = get_currency_rate(currency_code)
    result_label.config(text=f"Kurs {currency_code} to {currency_rate}")

app = tk.Tk()
app.geometry("400x400")
app.title("Kursy walut")

tk.Label(app, text="Wybierz walutę", font=("Arial", 20)).pack()
currency_combobox = ttk.Combobox(app, values=["USD", "EUR",])
currency_combobox.pack()

submit_button = tk.Button(
    app,
    text="Pobierz kurs",
    font=("Arial", 20),
    command=on_submit
)
submit_button.pack()
result_label = tk.Label(app, text="tutaj będą kursy", font=("Arial", 20))
result_label.pack()

app.mainloop()
