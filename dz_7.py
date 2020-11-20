# дз 7
"""
1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__() ), который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""


class Matrix:

    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        for row in self.matrix:
            for el in row:
                print(el, '\t', end='')
            print()

    def __add__(self, other):
        new_list_of_lists = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                             range(len(self.matrix))]
        return Matrix(new_list_of_lists)


m1 = Matrix([[1, 2], [3, 4]])
m1.__str__()
print()

m2 = Matrix([[5, 6], [7, 8]])
m2.__str__()
print()

m3 = m1 + m2
m3.__str__()
print()


"""
2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда , которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм . У этих типов одежды существуют
параметры: размер (для пальто ) и рост (для костюма ). Это могут быть обычные числа: V и
H , соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5) , для костюма (2*H + 0.3) . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property .
"""

from abc import ABC, abstractmethod


class Wear(ABC):

    @abstractmethod
    def costs(self):
        pass


class Coat(Wear):

    def __init__(self, v):
        self.v = v

    def costs(self):
        return self.v / 6.5 + 0.5


class Suit(Wear):

    def __init__(self, h):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = h

    def costs(self):
        return self.__h * 2 + 3


c = Coat(10)
s = Suit(10)

print(c.costs())
print(s.costs())
print()

"""
3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: 
сложение ( __add__() ), вычитание ( __sub__() ), умножение ( __mul__() ), деление ( __truediv__() ). 
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное 
(с округлением до целого) деление клеток, соответственно.
"""


class Mesh:

    def __init__(self, count):
        self.cell = count

    def __add__(self, other):
        return Mesh(self.cell + other.cell)

    def __sub__(self, other):
        count = self.cell - other.cell

        if count > 0:
            return Mesh(count)
        print(f'ошибка, значение count: {count}')

    def __mul__(self, other):
        return Mesh(self.cell * other.cell)

    def __truediv__(self, other):
        return Mesh(self.cell // other.cell)

    def make_order(self, count_in_row):
        columns = self.cell // count_in_row
        if self.cell % count_in_row == 0:
            for i in range(columns):
                print('*' * count_in_row)
        else:
            for i in range(columns):
                print('*' * count_in_row)

            print('*' * (self.cell % count_in_row))

        print()

m1 = Mesh(5)
m2 = Mesh(3)

m3 = m1 + m2
m4 = m1 - m2
m5 = m2 - m1
m6 = m1 * m2
m7 = m6 / m4

m1.make_order(3)
m2.make_order(4)

