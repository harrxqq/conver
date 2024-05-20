import unittest
from ConverterApp import CurrencyConverter, rates

class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.converter = CurrencyConverter(rates)

    def test_usd_to_eur(self):
        result = self.converter.convert(100, 'USD', 'EUR')
        self.assertAlmostEqual(result, 92.83, places=2)

    def test_eur_to_usd(self):
        result = self.converter.convert(100, 'EUR', 'USD')
        self.assertAlmostEqual(result, 107.74, places=2)

    def test_jpy_to_gbp(self):
        result = self.converter.convert(1000, 'JPY', 'GBP')
        self.assertAlmostEqual(result, 5.17, places=2)

    def test_gbp_to_kzt(self):
        result = self.converter.convert(50, 'GBP', 'KZT')
        self.assertAlmostEqual(result, 27659.68, places=2)

    def test_invalid_currency(self):
        with self.assertRaises(KeyError):
            self.converter.convert(100, 'ABC', 'USD')

if __name__ == '__main__':
    unittest.main()
