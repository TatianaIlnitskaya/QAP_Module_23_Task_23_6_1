import json
import requests
from config import keys

class ConvertionException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Вы ввели одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Такая валюта не поддерживается {quote}.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Такая валюта не поддерживается {base}.')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не верно введено количество валюты {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base = total_base * amount
        return total_base
