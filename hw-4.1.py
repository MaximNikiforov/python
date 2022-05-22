# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

scr_name, working_hours, rate_per_hour, premium = argv


def wage():
    return print(f'Заработная плата сотрудника: {float(working_hours) * float(rate_per_hour) + float(premium):g}')


if __name__ == '__main__':
    wage()
