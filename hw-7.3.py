# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого)
# деление клеток, соответственно.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество
# ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд
# записываются все оставшиеся.

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'({self.quantity}): {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return Cell(self.quantity - other.quantity)
        else:
            return f"({self.quantity - other.quantity}): Разность клеток не положительная"

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, c_max):
        c_str = ''
        for i in range(int(self.quantity / c_max)):
            c_str += f'{"*" * c_max} \n'
        c_str += f'{"*" * (self.quantity % c_max)}'
        return f'({self.quantity}) по {c_max}: \n{c_str}'


c_1 = Cell(5)
c_2 = Cell(7)
print(c_1)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_2 - c_1)
print(c_2 / c_1)
print((c_1 * c_2).make_order(10))
