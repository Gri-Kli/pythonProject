# Привет. Проверять скрипт не стоит, переписал твой скрипт который разбирали на уроке. во всем разобрался. Очень здорово, что разобрали домашку. Спасибо.



from datetime import date
from decimal import Decimal
from sys import argv

import requests


def get_currency_rate(currency_code='USD'):
    currency_code = currency_code.upper()
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'

    response_text = requests.get(url).text
    currency_starts_at_index = response_text.find(currency_code)

    if currency_starts_at_index == -1:
        return

    date_index = response_text.find('Date')
    currency_date = response_text[date_index + 6:date_index + 16]
    day, month, year = currency_date.split('.')
    refined_currency_date = date(int(year), int(month), int(day))

    nominal = get_field('<Nominal>', response_text, currency_starts_at_index)
    currency_price = get_field('<Value>', response_text, currency_starts_at_index)
    currency_price = currency_price.replace(',', '.')

    return f'На {refined_currency_date} {nominal} {currency_code} == {Decimal(currency_price)} RUR'


def get_field(field_name, response_text, currency_starts_at_idex):
    value_start_index = response_text.find(field_name, currency_starts_at_idex) + len(field_name)
    value_end_index = response_text.find('</', value_start_index)

    return response_text[value_start_index: value_end_index]


if __name__ == '__main__':
    _module_name, currency_code_arg = argv
    print(get_currency_rate(currency_code_arg))
