# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


from random import randint

test_list = [randint(-10, 10) for _ in range(10)]
print(f'Список: \n{test_list}')


def el_sum(my_list):
    i = 1
    s = 0
    while i <= len(my_list):
        s += my_list[i]
        i += 2
    return f'Сумма элементов на нечётных позициях: \n{s}'


print(el_sum(test_list))
