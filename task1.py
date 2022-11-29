# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def input_numbers(input_text):
    a = True
    while a:
        try:
            number = int(input(f'{input_text}'))
            a = False
        except ValueError:
            print('Неверное число')
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = input_numbers('Введите число: ')

my_list = [mult(e) for e in range(1, num + 1)]

print(f'Произведения чисел от 1 до {num}:  {my_list}')
