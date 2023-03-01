"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt

(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)"""


res=[]
file='nginx_logs.txt'
with open(file) as f:
    for line in f:
        line=line.split()
        ip=line[0]
        func=line[5].strip('"')
        action=line[6]
        res.append((ip,action,func))

print(res)


"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):

Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):

скалолазание,охота
горные лыжи
"""

import json
import sys

hobby_data = dict()
with open('hobby.csv', 'r', encoding='utf-8') as f1,\
    open('user.csv', 'r', encoding='utf-8') as f2:
    for line1 in f1:
        line2 = f2.readline().strip()
        if not line2:
            line2 = None
        if line1 not in hobby_data:
            hobby_data[line1.strip()] = line2
    content = f2.read()
  

with open('hobby_result.json','w', encoding='utf-8') as f3:
    data=json.dumps(hobby_data, ensure_ascii=False)
    f3.write(data)
with open('hobby_result.json','r', encoding='utf-8') as f4:
    content=f4.read()
    result=json.loads(content)

print(result)


"""
6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:

    просто запуск скрипта — выводить все записи;
    запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
    запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.

Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.

Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. """

import sys

param=sys.argv[1] if len(sys.argv) > 1 else '.'
with open ('sales_data.csv','a',encoding='utf-8') as f:
    param_1=''.join(param)
    f.write(param_1)

# Read file
import sys

param=len(sys.argv[1]) if len(sys.argv) > 1 else '.'
if param==1:
    with open ('sales_data.csv','a',encoding='utf-8') as f:
        content=f.read()
        print(content,end=' ')
elif param==2:
    with open('sales_data.csv', 'r', encoding='utf-8') as f:
        for line in f:
            content=f.readlines()[int(argv[1])-1:]
            print(content, end=' ')

