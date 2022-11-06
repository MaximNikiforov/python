# Вычислить число Пи c заданной точностью d


from math import pi


def input_d():
    a = True
    while a:
        try:
            d = float(input(f'Введите точность вычисления числа Пи (например 0.00001):\n'))
            if (10 ** -1) >= d >= (10 ** -10):
                a = False
                return d
            else:
                print('Неверное число')
        except ValueError:
            print('Неверное число!')


def round_pi(d):
    try:
        str_d = str(d)
        c = len(str_d[str_d.index('.') + 1:])
    except ValueError:
        c = str(d)[3:]
    return f'Пи с точностью {d} = {round(pi, int(c))}'


num = input_d()
print(round_pi(num))
