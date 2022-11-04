# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


from random import randint

test_list = [randint(100, 1000) / 100 for _ in range(10)]
print(f'Список: \n{test_list}')


def el_diff(my_list):
    new_list = [round(i % 1, 2) for i in my_list if i % 1 != 0]
    return f'Разница между максимальным и минимальным: \n{max(new_list) - min(new_list)}'


print(el_diff(test_list))
