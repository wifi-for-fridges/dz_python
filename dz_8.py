# дз 8

"""
1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
 преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
 и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def parse_date(cls, str_date):
        dates = str_date.split('-')

        date = int(dates[0])
        month = Data.valid_month(dates[1])
        year = int(dates[2])

        print(f'введенная дата: {date}.{month}.{year}')

    @staticmethod
    def valid_month(str_month):
        months = {
                  'январь': 1,
                  'ферваль': 2,
                  'март': 3,
                  'апрель': 4,
                  'май': 5,
                  'июнь': 6,
                  'июль': 7,
                  'август': 8,
                  'сентябрь': 9,
                  'октябрь': 10,
                  'ноябрь': 11,
                  'декабрь': 12
                  }

        return months[str_month]


date = Data('29-октябрь-2015')
Data.parse_date(date.str_date)

"""
2) Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, 
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту 
ситуацию и не завершиться с ошибкой.
"""

class OwnDivByZero(Exception):
    def __init__(self):
        self.txt = 'Ошибка!! Делить на 0 нельзя!'


try:
    number1 = float(input('введите число 1: '))
    number2 = float(input('введите число 2: '))

    if number2 == 0:
        raise OwnDivByZero()

except OwnDivByZero as err:
    print(err.txt)
else:
    print(f'результат деления: {number1 / number2}\n')


"""
3) Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только
 числами. Класс-исключение должен контролировать типы данных элементов списка.
"""


class OwnException(Exception):
    def __init__(self):
        self.txt = 'в список можно добавлять только числа!'


number_list = []
while True:
    value = input('введите значение для добавления в свисок (q - выход): ')

    if value == 'q':
        break

    try:
        if value.isalpha():
            raise OwnException()
    except OwnException as err:
        print(err.txt)
    else:
        value = float(value)
        number_list.append(value)

print(f'введенный список: {number_list}\n')


"""
4) - 6) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
 уникальные для каждого типа оргтехники. 
"""


class OwnCountEx(Exception):
    def __init__(self):
        self.txt = 'На складе нет такого количества техники!'

class OwnTypeEx(Exception):
    def __init__(self):
        self.txt = 'Количество извлекаемой техники можно вводить только числом!'

class Storage:
    def __init__(self):
        self._euq = {}

    def add(self, equipment):
        name = f'{equipment.name}, {equipment.model}'
        if name in self._euq.keys():
            self._euq[name] += 1
        else:
            self._euq.update([(name, equipment.count)])

    def extract(self, name, count):
        if type(count) == str:
            raise OwnTypeEx()

        if name in self._euq.keys():
            if self._euq[name] > count:
                self._euq[name] -= count
                return self._euq[name]

            if self._euq[name] == count:
                return self._euq.pop(name)
            else:
                raise OwnCountEx()

    def __str__(self):
        return str(self._euq)


class OfficeEquipment:
    def __init__(self, name, year):
        self.name = name
        self.year = year


class Printer(OfficeEquipment):
    count = 0

    def __init__(self, name, year, model):
        super().__init__(name, year)
        self.model = model
        Printer.count += 1

    def action(self):
        print('печать...\n')


class Scaner(OfficeEquipment):
    count = 0

    def __init__(self, name, year, model):
        super().__init__(name, year)
        self.model = model
        Scaner.count += 1

    def action(self):
        print('сканирует..\n')


class Xerox(OfficeEquipment):
    count = 0

    def __init__(self, name, year, model):
        super().__init__(name, year)
        self.model = model
        Xerox.count += 1

    def action(self):
        print('ксерит...\n')


storage = Storage()
printer1 = Printer('hp', 1993, '12-93')
printer1.action()
scaner = Scaner('lg', 2015, 'xx647')
scaner.action()
xerox = Xerox('samsung', 2019, 'asdfqqwe')
xerox.action()

storage.add(printer1)
storage.add(scaner)
storage.add(xerox)

printer2 = Printer('hp', 1995, '12-93')
storage.add(printer2)
print(storage)

try:
    storage.extract('hp, 12-93', 1)
except OwnTypeEx as tp:
    print(tp.txt)
except OwnCountEx as ct:
    print(ct.txt)
finally:
    print(storage)

try:
    storage.extract('lg, xx647', 1)
except OwnTypeEx as tp:
    print(tp.txt)
except OwnCountEx as ct:
    print(ct.txt)
finally:
    print(storage)

try:
    storage.extract('hp, 12-93', 'десять')
except OwnTypeEx as tp:
    print(tp.txt)
except OwnCountEx as ct:
    print(ct.txt)
finally:
    print(storage)

try:
    storage.extract('hp, 12-93', 10)
except OwnTypeEx as tp:
    print(tp.txt)
except OwnCountEx as ct:
    print(ct.txt)
finally:
    print(storage)


"""
7) Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
 методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) 
 и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real, imagine):
        self.real = real
        self.im = imagine

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.im + other.im)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.im - other.im)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.im * other.im, self.im * other.real + self.real * other.im)

    def __str__(self):
        if self.im > 0:
            return f'{self.real} + {self.im}i'

        if self.im < 0:
            return f'{self.real} - {abs(self.im)}i'


cn1 = ComplexNumber(5, 9)
cn2 = ComplexNumber(3, 24)

cn3 = cn1 + cn2
print(cn3)

cn3 = cn1 - cn2
print(cn3)

cn1 = ComplexNumber(-4, 16)
cn2 = ComplexNumber(11, -8)

cn3 = cn1 + cn2
print(cn3)

cn3 = cn1 - cn2
print(cn3)

cn1 = ComplexNumber(2, 3)
cn2 = ComplexNumber(5, -7)

cn3 = cn1 * cn2
print(cn3)

cn1 = ComplexNumber(12, 0)
cn2 = ComplexNumber(6, 2)

cn3 = cn1 * cn2
print(cn3)