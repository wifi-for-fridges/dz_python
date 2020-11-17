# дз 6

"""
1) Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
— на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
"""

import time


class TrafficLight:
    __colour = None

    def running(self):
        print('Светофор включен')

        self.__colour = 'red'
        print(f'Включен {self.__colour} свет')
        time.sleep(7)

        self.__colour = 'yellow'
        print(f'Включен {self.__colour} свет')
        time.sleep(2)

        self.__colour = 'green'
        print(f'Включен {self.__colour} свет')
        time.sleep(5)

        print('Выключение светофора')

    def running_with_check(self):
        self.__colour = 0
        traf_colors = {'red': 7, 'yellow': 2, 'green': 5}
        tr_keys = tuple(traf_colors.keys())

        while True:
            if self.__colour == 3:
                self.__colour = 0

            color = input('введите цвет: ')

            if color != tr_keys[self.__colour]:
                print('ошибка в работе светофора')
                break

            print(f'Включен {color} свет')
            time.sleep(traf_colors[color])
            self.__colour += 1


tf = TrafficLight()
tf.running()
tf.running_with_check()
print()

"""
2) Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
(ширина). Значения данных атрибутов должны передаваться при создании экземпляра
класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна. Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
1 см*число см толщины полотна. Проверить работу метода.
"""


class Road:
    __length = 0
    __width = 0

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate(self, weight, depth):
        return self.__length * self.__width * weight * depth


road = Road(15, 10)
print(f'{road.calculate(25, 5)} т')
print()

"""
3) Реализовать базовый класс Worker (работник), в котором определить атрибуты: name ,
surname , position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker .
В классе Position реализовать методы получения полного имени сотрудника ( get_full_name ) и
дохода с учетом премии ( get_total_income ). Проверить работу примера на реальных данных
(создать экземпляры класса Position , передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:
    name = None
    surname = None
    _position = {'wage': None, 'bonus': None}

    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._position['wage'] = wage
        self._position['bonus'] = bonus


class Position(Worker):

    def __init__(self, name, surname, wage, bonus):
        super(Position, self).__init__(name, surname, wage, bonus)

    def get_full_name(self):
        print(f'имя сотрудника: {self.name}')
        print(f'фамилия сотрудника: {self.surname}')

    def get_total_income(self):
        print(f'доход сотрудника: {self._position["wage"] + self._position["bonus"]}')


wk = Position('Вася', 'Пупкин', 20500, 1000)
wk.get_full_name()
wk.get_total_income()
print()

"""
4) Реализуйте базовый класс Car . У данного класса должны быть следующие атрибуты: speed ,
color , name , is_police (булево). А также методы: go , stop , turn(direction) , которые должны
сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar , SportCar , WorkCar , PoliceCar . Добавьте в базовый класс метод
show_speed , который должен показывать текущую скорость автомобиля. Для классов
TownCar и WorkCar переопределите метод show_speed . При значении скорости свыше 60
( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print('газззззуем!!')

    def stop(self):
        print('выжимаем тормозззззззззз')

    def turn(self, direction):
        print(f'машина двигается {direction}')

    def show_speed(self):
        print(f'текущая скорость: {self.speed}')


class TownCar(Car):
    def __init__(self, name, speed, color, is_police=False):
        super(TownCar, self).__init__(name, speed, color, is_police)

    def show_speed(self):
        print(f'текущая скорость: {self.speed}')
        if self.speed > 60:
            print('превышение скоростного режима!')


class WorkCar(Car):
    def __init__(self, name, speed, color, is_police=False):
        super(WorkCar, self).__init__(name, speed, color, is_police)

    def show_speed(self):
        print(f'текущая скорость: {self.speed}')
        if self.speed > 40:
            print('превышение скоростного режима!')


class SportCar(Car):
    def __init__(self, name, speed, color, is_police=False):
        super(SportCar, self).__init__(name, speed, color, is_police)
        print('содержать ее - дорогое удовольствие')


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True):
        super(PoliceCar, self).__init__(name, speed, color, is_police)

    def turn_on(self):
        print('сирена включена')

    def turn_off(self):
        print('сирена выключена')


tc = TownCar('hyndai solaris', 45, 'blue')
tc.go()
tc.turn('направо')
tc.show_speed()
tc.stop()
print()

wc = WorkCar('toyota alpald', 50, 'black')
wc.go()
wc.turn('обратно')
wc.show_speed()
wc.stop()
print()

sc = SportCar('aston martin', 350, 'red')
sc.go()
sc.turn('налево')
sc.show_speed()
sc.stop()
print()

pc = PoliceCar('bmw x5', 300, 'white-blue')
pc.go()
pc.turn_on()
pc.turn('обратно')
pc.turn_off()
pc.stop()
print()

"""
5) Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
(название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовать переопределение метода draw . Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
метод для каждого экземпляра.
"""


class Stationery:
    title = None

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('запуск отрисвоки')


class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)

    def draw(self):
        print(f'запуск отрисовки {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)

    def draw(self):
        print(f'запуск отрисовки {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)

    def draw(self):
        print(f'запуск отрисовки {self.title}')


pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')

pen.draw()
pencil.draw()
handle.draw()