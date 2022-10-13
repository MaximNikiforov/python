# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def quarter():
    try:
        x = float(input('Введите X: '))
        y = float(input('Введите Y: '))
        if x > 0:
            if y > 0:
                return print('1')
            elif y < 0:
                return print('4')
            else:
                return print('Y = 0 !')
        elif x < 0:
            if y > 0:
                return print('2')
            elif y < 0:
                return print('3')
            else:
                return print('Y = 0 !')
        else:
            return print('X = 0 !')
    except ValueError:
        print('Неверные координаты!')
        return quarter()


quarter()
