# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def fabric(self):
        return self.v / 6.5 + 0.5

    def __str__(self):
        return f'Ткань на пальто: {Coat(self.v).fabric:g}'


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def fabric(self):
        return 2 * self.h + 0.3

    def __str__(self):
        return f'Ткань на костюм: {Suit(self.h).fabric:g}'


class Total(Clothes):
    def __init__(self, h, v):
        self.h = h
        self.v = v

    @property
    def fabric(self):
        return Coat(self.v).fabric + Suit(self.h).fabric

    def __str__(self):
        return f'Ткани всего: {Total(self.h, self.v).fabric:g}'


coat = Coat(1255)
suit = Suit(174)
print(suit)
print(coat)
total = Total(174, 1255)
print(total)
