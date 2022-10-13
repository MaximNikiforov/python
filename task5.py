# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


def distance():
    import math
    try:
        a = list(map(float, input('Введите координаты точки A(x,y) через запятую: ').split(',')))
        b = list(map(float, input('Введите координаты точки B(x,y) через запятую: ').split(',')))
        if len(a) == 2 and len(b) == 2:
            dist = math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))
            return print(f'{dist:.2f}')
        else:
            print('Неверные координаты')
            return distance()
    except ValueError:
        print('Неверные координаты!')
        return distance()


distance()
