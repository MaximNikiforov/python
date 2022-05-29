# Реализовать класс Road (дорога).

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        print(f'Масса асфальта: {self._length * self._width * 25 * 5 / 1000:g} тонн')


m = Road(20, 5000)
m.mass()
