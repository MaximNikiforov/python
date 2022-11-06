# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


from random import randint

test_list = [randint(0, 10) for _ in range(20)]
print(f'Дано: \n{test_list}')


def non_repeating(my_list):
    result = list(set(my_list))
    return f'Результат: \n{result}'


print(non_repeating(test_list))
