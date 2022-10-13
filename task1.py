# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет


def weekend():
    try:
        day = int(input('Введите цифру, обозначающую день недели: '))
        if 1 <= day <= 5:
            return print('Не выходной')
        elif 6 <= day <= 7:
            return print('Выходной')
        else:
            print('Введите цифру от 1 до 7!')
            return weekend()
    except ValueError:
        print('Введите цифру от 1 до 7!')
        return weekend()


weekend()
