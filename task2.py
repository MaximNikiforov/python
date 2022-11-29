# 3.Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

def input_numbers(input_text):
    a = True
    while a:
        try:
            number = int(input(f'{input_text}'))
            a = False
        except ValueError:
            print('Неверное число')
    return number


num = input_numbers('Введите число: ')

my_dict = {e: (lambda n: round(((1 + 1 / n) ** n), 3))(e) for e in range(1, num + 1)}

print(f'Последовательность чисел от 1 до {num}:  {my_dict}')
