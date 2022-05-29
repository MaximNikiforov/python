# Создать класс TrafficLight (светофор).

from time import sleep


class TrafficLight:
    __color = {'Красный': 7, 'Жёлтый': 2, 'Зелёный': 10}

    @staticmethod
    def running():
        n_col = 0
        while n_col < 3:
            print(f'Светофор {list(TrafficLight.__color.keys())[n_col]}')
            sleep(TrafficLight.__color[list(TrafficLight.__color.keys())[n_col]])
            n_col += 1
        print(f'Светофор выключен')


a = TrafficLight()
a.running()
