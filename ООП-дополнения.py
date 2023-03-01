"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Data:
    @classmethod
    def meth_1(cls, data_1):
        new_str = data_1.split("-")
        day = int(new_str[0])
        month = int(new_str[1])
        year = int(new_str[2])
        print(year)
        print(type(day))

    @staticmethod
    def data_check(data_1):
        new_str = data_1.split("-")
        if int(new_str[0]) in range(1, 31):
            print("Day is correct")
        else:
            print("Day is incorrect")
        if int(new_str[1]) in range(1, 12):
            print("Month is correct")
        else:
            print("Month is incorrect")
        if int(new_str[2]) in range(1900, 2023) and len(new_str[2]) == 4:
            print("Year is correct")
        else:
            if len(new_str[2]) == 2:
                print("Year is incorrect, please enter the full year in range 1900-2022")


Data.meth_1("12-10-2021")
Data.data_check("12-10-87")


"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем. 
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data = input("Введите знаменатель: ")
first_number=input("Введите числитель: ")

try:
    inp_data = int(inp_data)
    first_number=int(first_number)
    if first_number== 0:
        while True: 
            first_number=input("На ноль делить нельзя, введите другой числитель: ")
            first_number=int(first_number)
            if first_number!= 0:
                print(f"Ваш результат: {inp_data//first_number}")
                break
    else:
        print(f"Ваш результат: {inp_data//first_number}")
                
                    
            
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)

""" Начать работу над классом Оргтехника
Создать класс, описывающий склад
Созадть класс оргтехника с описанием общих параметров
Создать 3 класса-наследника
Методы, отвечающие за прием оргтехники и передачу в определенное
подразделение (для хранения данных можно использовать словарь)
"""
# Основной класс склада
class Warehouse:
    def __init__(self, square, type_of_good):
        self.square = square
        self.type_of_good = type_of_good
        print(
            f"Наш склад площадью {self.square} кв.м. используется для хранения таких товаров как: {self.type_of_good}")

a = Warehouse(15, "оргтехника, столы, канцелярия")

# класс Оргтехника
class OrgTechnics:
    def __init__(self, interfase, power, types_of_paper):
        self.interfase = interfase
        self.power = power
        self.types_of_paper = types_of_paper

orgtech = OrgTechnics('usb', 'power', 'types_of_paper')

# Подкласс принтеры
class Printer(OrgTechnics):
    def __init__(self, interfase, power, types_of_paper):
        super().__init__(interfase, power, types_of_paper)

    def loading(self):
        self.printer = []
        Pr = {}
        ss = int(input("Начать ввод параметров принтера? 1- да, 2-нет: "))
        self.printer_number = 0
        while ss != 2:
            self.name = input("Введите марку принтера: ")
            self.model = input("Введите модель: ")
            self.printing_type = input("Введите тип принтера (струйный, лазерный и т.п.: ")
            self.speed = input("Введите скорость печати: ")
            self.speed.isdigit()
            try:
                check = self.speed.isdigit()
                if check == False:
                    while True:
                        print("Значение должно быть цифровым, попробуйте еще раз")
                        self.speed = input("Введите скорость печати: ")
                        if self.speed.isdigit() == True:
                            print("Значение в порядке")
                            break
            except ValueError:
                print("Вы ввели не число")
            self.color = input("Цветной/ЧБ: ")
            self.printer.append({'Производитель/Producer': self.name, 'Модель/Model': self.model,
                                 'Тип принтера': self.printing_type, 'Cкорость печати, лист/мин': self.speed,
                                 'Тип печати': self.color, "Тип бумаги": self.types_of_paper})
            self.printer_number = self.printer_number + 1
            ss = int(input("Продолжить ввод? 1- да, 2-нет: "))

    def PrinterStorage(self):
        print(self.printer)

    def Accepting(self):
        print(f"Количество принятых принтеров={self.printer_number}")

    def CurrentPosition(self):
        self.printer_transition = []
        self.new_place = 0
        self.choice_m = input("Выберите производителя принтера из списка: ")
        self.choice_n = input("Выберите модель: ")
        for i in self.printer:
            if i['Производитель/Producer'] == self.choice_m and i['Модель/Model'] == self.choice_m:
                self.new_place = input("Модель найдена, в какой отдел перемещаем:")
                self.printer_transition.append({'Производитель/Producer': self.choice_m, 'Модель/Model': self.choice_n,
                                                'Перемещено в отдел': self.new_place})
                print(self.printer_transition)
            else:
                print("Модель не найдена")


Pr = Printer("usb", '220V', 'A4')
Pr.loading()
Pr.PrinterStorage()
Pr.Accepting()
Pr.CurrentPosition()


# Класс сканеры
class Scaner(OrgTechnics):
    def __init__(self, interfase, power, types_of_paper):
        super().__init__(interfase, power, types_of_paper)

    def sc_loading(self):
        self.scaner = []
        Sc = {}
        ss = int(input("Начать ввод параметров сканера? 1- да, 2-нет: "))
        self.scaner_number = 0
        while ss != 2:
            self.scname = input("Введите производителя сканера: ")
            self.scmodel = input("Введите модель: ")
            self.resolution = input("Введите разрешающую способность: ")
            self.scspeed = input("Введите скорость сканирования: ")
            self.scspeed.isdigit()
            try:
                check = self.scspeed.isdigit()
                print(check)
                if check == False:
                    while True:
                        print("Значение должно быть цифровым, попробуйте еще раз")
                        self.scspeed = input("Введите скорость печати: ")
                        if self.scspeed.isdigit() == True:
                            print("Значение в порядке")
                            break
            except ValueError:
                print("Вы ввели не число")
            self.scaner.append({'Производитель': self.scname, 'Модель': self.scmodel,
                                'Разрешающая способность': self.resolution,
                                'Cкорость сканирования, лист/мин': self.scspeed,'Формат листов':self.types_of_paper })
            self.scaner_number = self.scaner_number + 1
            ss = int(input("Продолжить ввод? 1- да, 2-нет: "))

    def scaner_storage(self):
        print(self.scaner)

    def acceptingsc(self):
        print(f"Количество принятых сканеров={self.scaner_number}")

    def sc_currentposition(self):
        pos = 0
        self.scaner_transition = []
        self.new_place = 0
        self.choice_m = input("Выберите производителя сканера из списка: ")
        self.choice_n = input("Выберите модель: ")
        for i in self.scaner:
            if i['Производитель'] == self.choice_m and i['Модель'] == self.choice_m:
                self.new_place = input("Модель найдена, в какой отдел перемещаем:")
                self.scaner_transition.append({'Производитель': self.choice_m, 'Модель': self.choice_n,
                                               'Перемещено в отдел': self.new_place})
                print(self.scaner_transition)
            else:
                    print("Модель не найдена")



sc = Scaner("usb", '220V', 'A4')
sc.sc_loading()
sc.scaner_storage()
sc.acceptingsc()
sc.sc_currentposition()


# Подкласс ксерокс
class Xerox(OrgTechnics):
    def __init__(self, interfase, power, types_of_paper):
        super().__init__(interfase, power, types_of_paper)

    def xr_loading(self):
        self.xerox = []
        Xx = {}
        ss = int(input("Начать ввод параметров ксерокса? 1- да, 2-нет: "))
        self.xerox_number = 0
        while ss != 2:
            self.xrname = input("Введите производителя ксерокса: ")
            self.xrmodel = input("Введите модель: ")
            self.xrresolution = input("Введите разрешающую способность: ")
            self.xrspeed = input("Введите скорость копирования: ")
            self.xrspeed.isdigit()
            try:
                check = self.xrspeed.isdigit()
                print(check)
                if check == False:
                    while True:
                        print("Значение должно быть цифровым, попробуйте еще раз")
                        self.xrspeed = input("Введите скорость печати: ")
                        if self.xrspeed.isdigit() == True:
                            print("Значение в порядке")
                            break
            except ValueError:
                print("Вы ввели не число")
            self.incr = input("Масштабирование")
            self.xerox.append({'Производитель': self.xrname, 'Модель': self.xrmodel,
                               'Разрешающая способность': self.xrresolution,
                               'Cкорость копирования, лист/мин': self.xrspeed, 'Формат листов':self.types_of_paper, 'Масштабирование': self.incr})
            self.xerox_number = self.xerox_number + 1
            ss = int(input("продолжить ввод? 1- да, 2-нет: "))

    def xerox_storage(self):
        print(self.xerox)

    def acceptingxr(self):
        print(f"Количество принятых сканеров={self.xerox_number}")

    def xr_currentposition(self):
        pos = 0
        self.xerox_transition = []
        self.new_place = 0
        self.choice_m = input("Выберите производителя ксерокса из списка: ")
        self.choice_n = input("Выберите модель: ")
        for i in self.xerox:
            if i['Производитель'] == self.choice_m and i['Модель'] == self.choice_m:
                self.new_place = input("Модель найдена, в какой отдел перемещаем:")
                self.xerox_transition.append({'Производитель': self.choice_m, 'Модель': self.choice_n,
                                              'Перемещено в отдел': self.new_place})
                print(self.xerox_transition)
            else:
                print("Модель не найдена, продолжаем поиск....")
"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата."""

xx = Xerox("usb", '220V', 'A4')
xx.xr_loading()
xx.xerox_storage()
xx.acceptingxr()
xx.xr_currentposition()

class Complex_Number:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def output(self):
        print(complex(self.x, self.y))

    def __add__(self, other):
        return Complex_Number(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Complex_Number((self.x * other.x - self.y * other.y), (self.x * other.y + self.y * other.x))

    def __str__(self):
        return f"{complex(self.x, self.y)}"


a = Complex_Number(3, 2)
b = Complex_Number(4, 5)

print(a + b)

print(a * b)
