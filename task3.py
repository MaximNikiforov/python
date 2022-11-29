# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


from random import randint

test_list = [randint(0, 10) for _ in range(20)]
print(f'Дано: \n{test_list}')

print((lambda x: list(set(x)))(test_list))
