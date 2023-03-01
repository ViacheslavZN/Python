"""
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод."""
import time


class TrafficLight:

    def running(self):
        __color = "Red"
        print(__color)
        time.sleep(7)
        __color = "Yellow"
        print(__color)
        time.sleep(2)
        __color = "Green"
        print(__color)
        time.sleep(6)


light = TrafficLight()
light.running()

"""2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т."""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asph_load(self, a_m, thickness):
        self.a_m = int(a_m)
        self.thickness = int(thickness)
        mass = self._width * self._length * self.a_m * self.thickness // 1000
        print(mass)


asph_ex = Road(20, 5000)

"""3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров."""
income = {"wage": 56000, "bonus": 15000}


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        print(f"Полное имя: {self.name} {self.surname}, должность - {self.position}")

    def get_total_income(self):
        income = {"wage": 56000, "bonus": 15000}
        self._income = income
        summ = self._income['wage'] + self._income['bonus']
        print(f"Суммарный доход - {summ} руб.")


w_1 = Position('Иван', 'Сидоров', 'инженер')

w_1.get_full_name()
w_1.get_total_income()

asph_ex.asph_load(25, 5)

"""4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
 остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат."""


# Родительский класс
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Car {self.name} start moving")

    def stop(self):
        print(f"Car {self.name} stop moving")

    def turn(self, direction):
        self.direction = direction
        print(f"Car {self.name} is going {self.direction}")

    def show_speed(self):
        print(f"Current speed of {self.name} is {self.speed}")


# Дочерний класс TownCar

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def type(self):
        if self.is_police == False:
            print(f"Car {self.name} is Town Car")

    def show_speed(self):
        print(f"Current speed of {self.name} is {self.speed}")
        if self.speed > 60:
            print("Внимание, превышение скорости!!")


# Дочерний класс WorkCar
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def type(self):
        if self.is_police == False:
            print(f"Car {self.name} is Town Car")

    def show_speed(self):
        print(f"Current speed of {self.name} is {self.speed}")
        if self.speed > 40:
            print("Внимание, превышение скорости!!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def type(self):
        if self.is_police == False:
            print(f"Car {self.name} is Town Car")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def type(self):
        if self.is_police == True:
            print(f"Car {self.name} is Police Car")


car_1 = Car(70, 'Red', 'BMW', False)
car_1.go()
car_1.stop()
car_1.turn('Right')
car_1.show_speed()
print(
    '')
car_2 = TownCar(70, 'Red', 'BMW', False)
car_2.type()
car_2.show_speed()
print(
    '')
car_3 = WorkCar(30, 'Red', 'BMW', False)
car_3.type()
car_3.show_speed()
print(
    '')
car_4 = SportCar(70, 'Red', 'BMW', False)
car_4.type()
print(
    '')
car_5 = PoliceCar(70, 'Red', 'BMW', True)
car_5.type()

"""5.	Реализовать класс Stationery (канцелярская принадлежность):
●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки маркером")


a_1 = Pen(Pen)
a_1.draw()
a_2 = Pencil(Pencil)
a_2.draw()
a_2 = Handle(Handle)
a_2.draw()
