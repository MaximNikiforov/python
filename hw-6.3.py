# Реализовать базовый класс Worker (работник).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'Полное имя: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход: {self._income.get("wage") + self._income.get("bonus")}$'


w_1 = Position('Tony', 'Stark', 'Ironman', 9000000000, 1000000000)
print(w_1.get_full_name())
print(w_1.get_total_income())
