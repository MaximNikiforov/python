# Реализовать класс Stationery (канцелярская принадлежность).

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'{self.title}. Запуск отрисовки'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{__class__.__name__} - {self.title}. Рисунок ручкой'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{__class__.__name__} - {self.title}. Рисунок карандашом'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{__class__.__name__} - {self.title}. Рисунок маркером'


s = Stationery('Бумага')
s_1 = Pen('Ручка')
s_2 = Pencil('Карандаш')
s_3 = Handle('Маркер')
print(s.draw())
print(s_1.draw())
print(s_2.draw())
print(s_3.draw())
