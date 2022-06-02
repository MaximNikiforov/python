# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, mtrx):
        self.mtrx = mtrx

    def __str__(self):
        return '\n'.join([''.join([str(cell).ljust(7) for cell in row]) for row in self.mtrx])

    def __add__(self, other):
        if len(self.mtrx) == len(other.mtrx) and len(self.mtrx[0]) == len(other.mtrx[0]):
            return Matrix([list(map(sum, zip(*i))) for i in zip(self.mtrx, other.mtrx)])
        else:
            return f'Размер матриц не совпадает!'


m_1 = Matrix([[1, 3, 5, 7], [2, 4, 6, 8], [3, 5, 7, 9]])
m_2 = Matrix([[12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]])
print(f'Первая матрица: \n{m_1}')
print(f'Вторая матрица: \n{m_2}')
print(f'Сумма матриц: \n{m_1+m_2}')
