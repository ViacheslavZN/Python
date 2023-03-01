#Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, 

def odd_nums(n):
    for num in range (0,n+1):
        if num%2!=0:
            yield num

odd_to_5=odd_nums(15)
print(odd_to_5)
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))

"""3. Есть два списка:

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:

('Иван', '9А')
('Анастасия', '7В')
...

Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:

('Станислав', None)"""

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Лариса', 'Алла']

klasses = ['9А', '7B', '9Б', '9В', '8Б', '9f']


def function():
    t = len(tutors) - len(klasses)
    for tutor, klass in zip(tutors, klasses):
        yield (tutor, klass)
    while t > 0:
        k = (tutors[-t], 'None')
        t = t - 1
        yield k


z = function()
print(z)
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))

"""
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
"""

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
k = len(src) - 1
i = 0
N = len(src) - 1
majority = set()
while i < N:
    if src[i + 1] > src[i]:
        majority.add(src[i + 1])
    i = i + 1
print([number for number in src if number in majority])


"""
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_number = set()
repeated_number = set()

for number in src:
    if number in repeated_number:
        continue
    if number in unique_number:
        repeated_number.add(number)
        unique_number.discard(number)
        continue
    unique_number.add(number)

print([number for number in src if number in unique_number])



