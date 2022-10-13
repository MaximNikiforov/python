# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


def coordinate():
    ans = ['Ошибка! Неверный номер четверти!', 'x > 0, y > 0', 'x < 0, y > 0', 'x < 0, y < 0', 'x < 0, y > 0']
    try:
        q = int(input('Введите номер четверти: '))
        if 0 < q < 5:
            return print(ans[q])
        else:
            print(ans[0])
            return coordinate()
    except ValueError:
        print(ans[0])
        return coordinate()


coordinate()
