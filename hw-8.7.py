# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных
# экземпляров. Проверьте корректность полученного результата.


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b < 0:
            return f'{self.a} - {-self.b}i'
        elif self.b == 0:
            return f'{self.a}'
        else:
            return f'{self.a} + {self.b}i'

    def __add__(self, other):
        a_add = self.a + other.a
        b_add = self.b + other.b
        return Complex(a_add, b_add)

    def __mul__(self, other):
        a_mul = self.a * other.a - self.b * other.b
        b_mul = self.a * other.b + other.a * self.b
        return Complex(a_mul, b_mul)

    def __sub__(self, other):
        a_sub = self.a - other.a
        b_sub = self.b - other.b
        return Complex(a_sub, b_sub)

    def __truediv__(self, other):
        a_truediv = (self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2)
        b_truediv = (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)
        return Complex(a_truediv, b_truediv)


c_1 = Complex(2, -3)
c_2 = Complex(1, 3)
print(c_1)
print(c_2)
print(c_1 + c_2)
print(c_1 * c_2)
print(c_1 - c_2)
print(c_1 / c_2)
