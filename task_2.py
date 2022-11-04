# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.


from random import randint

test_list = [randint(-10, 10) for _ in range(7)]
print(f'Список: \n{test_list}')


def el_sum(my_list):
    i = 0
    j = len(my_list)
    mult_list = []
    while i < j:
        mult_list.append(my_list[i] * my_list[j-1])
        i += 1
        j -= 1
    return f'Произведение пар чисел: \n{mult_list}'


print(el_sum(test_list))
