# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй,
# с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например,
# месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def date_split(cls, date):
        return [int(i) for i in date.split('-')]

    @staticmethod
    def date_check(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1900 < year <= 2100:
                    return f'Всё верно'
                else:
                    return f'Неверный год'
            else:
                return f'Неверный месяц'
        else:
            return f'Неверный день'

    def __str__(self):
        return f'Текущая дата : {".".join(map(str, Data.date_split(self.date)))} \n {Data.date_check(*Data.date_split(self.date))}'


d = Data('11-15-2020')
print(d)
print(Data('22-12-2010'))
