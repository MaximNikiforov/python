# Реализуйте базовый класс Car.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if self.is_police is True:
            print(f'Полицейская {self.color} {self.name} завелась')
        else:
            print(f'{self.color} {self.name} завелась')

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn(self, direction):
        return f'{self.name} поворачивает {direction}.'

    def show_speed(self):
        return f'Скорость {self.name}: {self.speed} км/ч.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость {self.name}: {self.speed} км/ч. Превышение скорости!'
        else:
            return f'Скорость {self.name}: {self.speed} км/ч.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость {self.name}: {self.speed} км/ч. Превышение скорости!'
        else:
            return f'Скорость {self.name}: {self.speed} км/ч.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


c_1 = TownCar(90, 'Малиновая', 'Лада')
c_2 = SportCar(200, 'Красная', 'Феррари')
c_3 = WorkCar(30, 'Синий', 'Трактор')
c_4 = PoliceCar(100, 'Белая', 'Шкода')
print(c_1.go(), c_1.show_speed())
print(c_2.go(), c_2.stop())
print(c_3.turn('налево'), c_3.show_speed())
print(c_4.turn('направо'))
