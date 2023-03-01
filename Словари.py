"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. 
"""


def num_translate(number):
    dictionary = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    return dictionary.get(number)


number = input("Input a number:   ")

if num_translate(number) != None:
    print(f" '{number.title()}' in Russian is '{num_translate(number)}'")
else:
    print("Please input the number in range 0-10")
    
    
"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:

>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"], 
    "М": ["Мария"], "П": ["Петр"]
}
"""
# Словарь с сортировкой
def thesaurus(*args):
    args_rev = sorted(args, reverse=False)
    vocab = dict()
    for elements in args_rev:
        i = elements[0]
        if i not in vocab:
            vocab[i] = []
        vocab[i].append(elements)
    return vocab

""" 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

        Например:

>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

print(thesaurus("Жора", "Мария", "Петр", "Илья"))"""

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives =["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
joke = []
len_1 = len(nouns) - 1
len_2 = len(adverbs) - 1
len_3 = len(adjectives) - 1


def get_jokes(jokes_number):
    i = 0
    while i < jokes_number:
        n = random.randint(0, len_1)
        adv = random.randint(0, len_2)
        adj = random.randint(0, len_3)
        new_line = nouns[n] + ' ' + adverbs[adv] + ' ' + adjectives[adj]
        joke.append(new_line)
        i = i + 1
    return joke


number = int(input("Сколько шуток Вы хотите (до 4х)   "))
print(get_jokes(number))
