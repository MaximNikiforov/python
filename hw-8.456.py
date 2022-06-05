# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные
# типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для
# приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники
# на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру
# (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип
# данных.


class Storage:
    def __init__(self):
        self._dict = {}

    def put_in(self, equipment):
        self._dict.setdefault(equipment.group_name(), {}).update(equipment.eq())
        print(f'{self._dict}')

    def take_from(self, typ, name):
        try:
            if self._dict[typ][name]:
                if self._dict[typ][name][0] > 0:
                    print(f'Забираем {typ} {name}')
                    self._dict[typ][name][0] -= 1
                    if self._dict[typ][name][0] == 0:
                        self._dict[typ].pop(name)
                        if self._dict[typ] == {}:
                            self._dict.pop(typ)
        except KeyError:
            print(f'{typ} {name} нет на складе!')
        print(f'{self._dict}')


class Equipment:
    def __init__(self, *args):
        self.args = {}
        for i in range(1, len(args)):
            self.args.setdefault(args[0], []).append(args[i])
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def eq(self):
        return self.args


class Printer(Equipment):
    def __init__(self, *args):
        super().__init__(*args)


class Scaner(Equipment):
    def __init__(self, *args):
        super().__init__(*args)


class Copier(Equipment):
    def __init__(self, *args):
        super().__init__(*args)


storage = Storage()
"""Первым аргументом указываем название, вторым аргументом количество, 
далее любое кол-во аргументов - характеристики"""
s_1 = Scaner('Epson', 1, 'A4', '400dpi', 'б/у')
s_2 = Scaner('Kodak', 2, 'A3', '600dpi')
p_1 = Printer('Brother', 4, 'A4', 'black')
c_1 = Copier('Canon', 1, 'A3', '25ppm')

storage.put_in(s_1)
storage.put_in(s_2)
storage.put_in(p_1)
storage.put_in(c_1)
storage.take_from('Scaner', 'Kodak')
storage.take_from('Scaner', 'Epson')
storage.take_from('Copier', 'Epson')
storage.take_from('Copier', 'Canon')
