import requests
import json
from config import keys


class APIException(Exception):
    pass

class MoneyConvertor:
    @staticmethod
    def get_price(quote : str, base: str, amount : str):
        if quote == base:
            raise APIException(f'Нельзя перевести одинаковые валюты {base}')

        quote_ticker, base_ticker = keys[quote], keys[base]
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(
            f'https://v6.exchangerate-api.com/v6/b25574281b9ee601feab2af1/pair/{quote_ticker}/{base_ticker}')
        total_base = json.loads(r.content)['conversion_rate'] * amount

        return total_base

