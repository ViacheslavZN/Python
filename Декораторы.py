"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError. Пример:
>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
"""
import re

dic={}

def email_parse(email):
    re_email = re.compile(r'\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}')
    # username=re.compile(r'^[a-zA-Z0-9_*!][^@]{0,25}')
    username = re.compile(r'^[a-zA-Z0-9_*!.][^@]{0,56}')
    domain = re.compile(r'\@[a-zA-Z_]+?\.[a-zA-Z]{2,4}')
    if re_email.match(email):
        u_name=username.findall(email)
        d_name=str(domain.findall(email)).replace('@','')
        def f (**kwargs):
            print (kwargs)
        f (username=u_name, domain=d_name)
    else:
        raise ValueError (f'ValueError: wrong email {email}')



email_parse('zyrinviacheslav@gmail.com')

"""3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3
#>>> a = calc_cube(5)
5: <class 'int'>"""


def type_logger(calc_cube):
    def wrapper(x):
        print(f'{x}:{type(x)}')
        calc_cube(x)

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)

