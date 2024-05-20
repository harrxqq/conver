class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency != 'USD':
            amount = amount / self.rates[from_currency]['rate']
        amount = round(amount * self.rates[to_currency]['rate'], 2)
        return amount

rates = {
    'USD': {'name': 'Доллар США', 'rate': 1},
    'EUR': {'name': 'Евро', 'rate': 0.92827},
    'JPY': {'name': 'Японская йена', 'rate': 153.79},
    'GBP': {'name': 'Фунт стерлингов', 'rate': 0.79523},
    'KZT': {'name': 'Казахстанский тенге', 'rate': 439.50},
    'UAH': {'name': 'Украинская гривна', 'rate': 39.29},
    'AUD': {'name': 'Австралийский доллар', 'rate': 1.51},
    'CAD': {'name': 'Канадский доллар', 'rate': 1.37},
    'CHF': {'name': 'Швейцарский франк', 'rate': 0.9053},
    'CNY': {'name': 'Китайский юань', 'rate': 7.21},
    'HKD': {'name': 'Гонконгский доллар', 'rate': 7.82},
    'NZD': {'name': 'Новозеландский доллар', 'rate': 1.66},
    'RUB': {'name': 'Русский рубль', 'rate': 91.31},
    'TRY': {'name': 'Турецкая лира', 'rate': 8.50},
    'BRL': {'name': 'Бразильский реал', 'rate': 5.07},
    'SGD': {'name': 'Сингапурский доллар', 'rate': 1.35},
    'RON': {'name': 'Румынский лей', 'rate': 4.62}
}
