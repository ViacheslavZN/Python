"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр."""

class Matrix:
    def __init__(self, in_list):
        self.in_list = in_list
        self.list_1 = self.in_list[0]
        self.list_2 = self.in_list[1]

    def __str__(self):
        return f"{' '.join(self.list_1)} \n{' '.join(self.list_2)}"

    def __add__(self, other):
        a_1 = self.list_1
        a_2 = other[0]
        b_1 = self.list_2
        b_2 = other[1]
        index = 0
        while index < len(a_1):
            a_1[index] = str(int(a_1[index]) + int(a_2[index]))
            b_2[index] = str(int(b_1[index]) + int(b_2[index]))
            index += 1
        in_list = [a_1] + [b_2]
        return Matrix(in_list)


a = Matrix([['3', '2', '3'], ['3', '3', '3']])
print(a)
b = [['3', '2', '3'], ['3', '8', '3']]
print(a + b)

"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани.
Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

"""


class Clothes:
    def __init__(self):
        self.sizes = []
        self.size = input("Введите размер: ")
        self.sizes.append(self.size)
        while self.size != "0":
            self.size = input("Введите размер: ")
            self.sizes.append(self.size)
        # print(f"Размерный ряд для производства пальто: {self.sizes[0:int(len(self.sizes))-1]}")
        self.heights = []
        self.height = input("Введите рост: ")
        self.heights.append(self.height)
        while self.height != "0":
            self.height = input("Введите рост: ")
            self.heights.append(self.height)
        print(f"Размерный ряд для производства костюмов: {self.heights[0:(int(len(self.heights)) - 1)]}")


class Coats(Clothes):
    def __init__(self):
        super().__init__()

    @property
    def text_cons_coats(self):
        v = []
        for el in self.sizes[0:(int(len(self.heights)) - 1)]:
            v_1 = int(el) // 6.5 + 0.5
            v.append(v_1)
        print(f"Расход ткани по заказу: {v}")
        summ_cons = 0
        i = 0
        while i < len(v):
            summ_cons = summ_cons + float(v[i])
            i += 1
        print(f"Суммарный расход ткани на пальто: {summ_cons} м")


class Suits(Clothes):
    def __init__(self):
        super().__init__()

    @property
    def text_cons_suits(self):
        h = []
        for el in self.heights[0:(int(len(self.heights)) - 1)]:
            h_1 = 2 * int(el) + 0.3
            h.append(h_1)
        print(f"Расход ткани по заказу: {h}")
        summ_cons = 0
        i = 0
        while i < int(len(h)) - 1:
            summ_cons = summ_cons + float(h[i])
            i += 1
        print(f"Суммарный расход ткани на костюмы: {summ_cons} м")


"""расчет для пальто
b = Coats()
b.text_cons_coats"""

# расчет для костюма
el = Suits()
el.text_cons_suits

