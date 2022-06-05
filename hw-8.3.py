# Создайте собственный класс-исключение, который должен проверять содержимое списка
# на наличие только чисел. Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.


class NotNumber(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'Это не число!'


class ListCheck:
    def __init__(self):
        self.num_list = []

    def num_check(self):
        while True:
            try:
                n = input('Введите число: ')
                if n == '.':
                    print(self.num_list)
                    return
                else:
                    try:
                        self.num_list.append(int(n))
                    except ValueError:
                        raise NotNumber
            except NotNumber:
                print('Введено неверное значение!')
                continue


a_1 = ListCheck()
a_1.num_check()
