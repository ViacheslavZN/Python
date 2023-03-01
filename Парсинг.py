"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро."""

# парсинг сайта ЦБ
import requests
from datetime import datetime

response = requests.get('http://cbr.ru/scripts/XML_daily.asp')
if response.status_code == 200:
    content = response.content.decode(encoding=response.encoding)
else:
    print("Проблема с получением информации")
# Дата обращения к сайту
for el in content.split('ValCurs Date="')[1:]:
    time = el.split('"')[0]
    time = time.split('.')
    date = datetime(year=int(time[2]), month=int(time[1]), day=int(time[0]), hour=0)
    date_format = (f'{time[0]}.{time[1]}.{time[2]}')


def currency_rate(name):
    currency = []
    rate = []
    for el in content.split('NumCode><CharCode>')[1:]:
        i = el.split('</')[0]
        currency.append(i)
    for z in content.split('Name><Value>')[1:]:
        k = z.split('</')[0]
        rate.append(k)
    if name in currency:
        pos = currency.index(name)
        value = float(rate[pos].replace(',', '.'))
        quantity = input('Введите количество валюты: ')
        sum = float(quantity) * value
        print(f'Ваша цена за {quantity} {name} (по курсу ЦБ {value}руб. на {date_format})  равна {round(sum, 3)} рублей')
    else:
        print("None")

name = input("Введите код валюты: ")

currency_rate(name)

"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего лишнего не происходит."""
import utils

utils.currency_rate('USD')


