from tkinter import *
from ConverterApp import CurrencyConverter, rates

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()

    converter = CurrencyConverter(rates)
    converted_amount = converter.convert(amount, from_currency, to_currency)

    result_label.config(
        text=f"{amount} {rates[from_currency]['name']} = {converted_amount} {rates[to_currency]['name']}")

root = Tk()
root.title("Конвертер валют")

amount_label = Label(root, text="Сумма:")
amount_label.grid(row=0, column=0)

amount_entry = Entry(root)
amount_entry.grid(row=0, column=1)

from_currency_label = Label(root, text="Из валюты:")
from_currency_label.grid(row=1, column=0)

from_currency_var = StringVar(root)
from_currency_var.set("USD")
from_currency_menu = OptionMenu(root, from_currency_var, *rates.keys())
from_currency_menu.grid(row=1, column=1)

to_currency_label = Label(root, text="К валюте:")
to_currency_label.grid(row=2, column=0)

to_currency_var = StringVar(root)
to_currency_var.set("EUR")
to_currency_menu = OptionMenu(root, to_currency_var, *rates.keys())
to_currency_menu.grid(row=2, column=1)

convert_button = Button(root, text="Перевести", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2)

result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
